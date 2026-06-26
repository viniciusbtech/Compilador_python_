"""Gerador de LLVM IR usando llvmlite para a linguagem JSS."""

from __future__ import annotations

from typing import TYPE_CHECKING

import llvmlite.ir as ir

from .ast_nodes import (
    Assignment,
    AttributeAccess,
    BinaryOperation,
    Block,
    BreakStatement,
    Call,
    ClassDeclaration,
    ConstructorDeclaration,
    Declarator,
    ExpressionStatement,
    ForStatement,
    FunctionDeclaration,
    Identifier,
    IfStatement,
    IndexAccess,
    Literal,
    MethodDeclaration,
    NewObject,
    Node,
    Program,
    ReturnStatement,
    TypeNode,
    UnaryOperation,
    VarDeclaration,
    WhileStatement,
)
from .semantic import ClassInfo, Scope, SemanticAnalyzer, SemanticSymbol, TypeInfo
from .tokens import TokenType

# ---------------------------------------------------------------------------
# Tipos LLVM correspondentes aos tipos JSS
# ---------------------------------------------------------------------------

_INT  = ir.IntType(32)
_BOOL = ir.IntType(1)
_REAL = ir.DoubleType()
_VOID = ir.VoidType()
_STR  = ir.IntType(8).as_pointer()


def _eval_static_size(node: Node | None) -> int:
    """Avalia tamanho estático de array — deve ser Literal inteiro na AST."""
    if isinstance(node, Literal) and node.literal_type == "int":
        return int(node.value)
    return 1


def _llvm_type_from_type_node(type_node: TypeNode) -> ir.Type:
    """Traduz TypeNode da AST para ir.Type preservando tamanhos reais de arrays."""
    base = _base_type(type_node.name)
    if not type_node.is_array:
        return base
    size1 = _eval_static_size(type_node.array_size)
    if type_node.array_size2 is not None:
        size2 = _eval_static_size(type_node.array_size2)
        return ir.ArrayType(ir.ArrayType(base, size2), size1)
    return ir.ArrayType(base, size1)


def _llvm_type(type_info: TypeInfo) -> ir.Type:
    """Converte TypeInfo (tabela de símbolos) para ir.Type — usado em contextos sem AST."""
    if type_info.is_array:
        base = _base_type(type_info.name)
        if type_info.ndim == 2:
            return ir.ArrayType(ir.ArrayType(base, 0), 0)
        return ir.ArrayType(base, 0)
    return _base_type(type_info.name)


def _base_type(name: str) -> ir.Type:
    return {"int": _INT, "real": _REAL, "bool": _BOOL, "str": _STR, "void": _VOID}.get(
        name, _INT
    )


def _default_value(t: ir.Type) -> ir.Constant:
    if isinstance(t, ir.DoubleType):
        return ir.Constant(t, 0.0)
    if isinstance(t, ir.IntType):
        return ir.Constant(t, 0)
    return ir.Constant(t, None)


# ---------------------------------------------------------------------------
# Gerador principal
# ---------------------------------------------------------------------------

class LLVMGenerator:
    """Constrói um módulo LLVM IR a partir da AST JSS usando llvmlite."""

    def __init__(self, program: Program, analyzer: SemanticAnalyzer) -> None:
        self._program   = program
        self._analyzer  = analyzer
        self._module    = ir.Module(name="jss_module")
        self._module.triple = "x86_64-pc-windows-msvc"

        # Estado do gerador durante a travessia
        self._builder:          ir.IRBuilder | None = None
        self._current_scope:    Scope | None = None
        self._current_class:    ClassInfo | None = None
        self._locals:           dict[str, ir.AllocaInstr] = {}
        self._globals:          dict[str, ir.GlobalVariable] = {}
        self._break_stack:      list[ir.Block] = []
        self._struct_types:     dict[str, ir.LiteralStructType] = {}
        self._pow_i32:          ir.Function | None = None  # __jss_pow_i32 (gerado sob demanda)

        # Declarações de funções externas (runtime C)
        self._printf = ir.Function(
            self._module,
            ir.FunctionType(_INT, [_STR], var_arg=True),
            name="printf",
        )
        self._scanf = ir.Function(
            self._module,
            ir.FunctionType(_INT, [_STR], var_arg=True),
            name="scanf",
        )
        self._malloc = ir.Function(
            self._module,
            ir.FunctionType(_STR, [ir.IntType(64)]),
            name="malloc",
        )

    # ------------------------------------------------------------------
    # Ponto de entrada
    # ------------------------------------------------------------------

    def generate(self) -> str:
        # 1. Tipos de classes (structs)
        for name, class_info in self._analyzer.classes.items():
            field_types = [_base_type(s.type_info.name) for s in class_info.attributes.values()]
            struct = self._module.context.get_identified_type(name)
            struct.set_body(*field_types)
            self._struct_types[name] = struct

        # 2. Variáveis globais
        for name, sym in self._analyzer.global_scope.symbols.items():
            if sym.category in {"variavel", "constante"}:
                var_decl = self._find_var_declaration(name)
                llvm_t = _llvm_type_from_type_node(var_decl.type_node) if var_decl else _llvm_type(sym.type_info)
                gvar = ir.GlobalVariable(self._module, llvm_t, name=name)
                if sym.type_info.is_array:
                    gvar.initializer = ir.Constant(llvm_t, None)  # zeroinitializer
                else:
                    lit_init = self._find_global_literal_init(name, sym.type_info)
                    gvar.initializer = lit_init if lit_init is not None else _default_value(llvm_t)
                gvar.linkage = "internal"
                self._globals[name] = gvar

        # 3. Coleta statements globais (tudo que não é var/função/classe)
        global_stmts = [
            decl for decl in self._program.declarations
            if not isinstance(decl, (VarDeclaration, FunctionDeclaration, ClassDeclaration))
        ]

        has_user_main = any(
            isinstance(d, FunctionDeclaration) and d.name == "main"
            for d in self._program.declarations
        )

        # Caso 1 — statements globais → sempre vão para __jss_global_init
        if global_stmts:
            self._gen_global_init(global_stmts)

        # 4. Funções e classes do usuário
        # function main() do JSS → gerado como @__jss_user_main
        for decl in self._program.declarations:
            if isinstance(decl, FunctionDeclaration):
                self._declare_function(decl)
        for decl in self._program.declarations:
            if isinstance(decl, FunctionDeclaration):
                self._gen_function(decl)
            elif isinstance(decl, ClassDeclaration):
                self._gen_class(decl)

        # 5. Gera @main real do executável (entry point para clang/SO)
        self._gen_entry_main(
            has_global_init=bool(global_stmts),
            has_user_main=has_user_main,
        )

        return str(self._module)

    # ------------------------------------------------------------------
    # Declaração antecipada de funções (para forward calls)
    # ------------------------------------------------------------------

    def _declare_function(
        self,
        decl: FunctionDeclaration | MethodDeclaration,
        class_prefix: str = "",
    ) -> ir.Function:
        ret_t  = _base_type(decl.return_type.name)
        param_types = [_llvm_type(TypeInfo(p.type_node.name, p.type_node.is_array)) for p in decl.params]
        if class_prefix:
            struct_ptr = self._struct_types[class_prefix].as_pointer()
            param_types = [struct_ptr] + param_types
        if not class_prefix and decl.name == "main":
            fn_name = "__jss_user_main"
        elif class_prefix:
            fn_name = f"{class_prefix}.{decl.name}"
        else:
            fn_name = decl.name
        existing = self._module.globals.get(fn_name)
        if existing:
            return existing  # type: ignore[return-value]
        fntype = ir.FunctionType(ret_t, param_types)
        return ir.Function(self._module, fntype, name=fn_name)

    # ------------------------------------------------------------------
    # Funções
    # ------------------------------------------------------------------

    def _gen_function(
        self,
        decl: FunctionDeclaration | MethodDeclaration,
        class_prefix: str = "",
    ) -> None:
        if not class_prefix and decl.name == "main":
            fn_name = "__jss_user_main"
        elif class_prefix:
            fn_name = f"{class_prefix}.{decl.name}"
        else:
            fn_name = decl.name
        fn = self._module.globals.get(fn_name)
        if fn is None:
            fn = self._declare_function(decl, class_prefix)

        entry = fn.append_basic_block("entry")
        self._builder = ir.IRBuilder(entry)

        prev_scope  = self._current_scope
        prev_locals = self._locals
        self._current_scope = decl.body.scope
        self._locals = {}

        # alloca para variáveis locais (pré-passagem)
        self._alloca_locals(decl.body)

        # Parâmetros
        param_offset = 0
        if class_prefix:
            param_offset = 1  # primeiro parâmetro é 'self'
            self_ptr = fn.args[0]
            self_alloca = self._builder.alloca(self_ptr.type, name="self")
            self._builder.store(self_ptr, self_alloca)
            self._locals["self"] = self_alloca

        for i, param in enumerate(decl.params):
            arg = fn.args[i + param_offset]
            param_t = _llvm_type(TypeInfo(param.type_node.name, param.type_node.is_array))
            alloca = self._builder.alloca(param_t, name=param.name)
            self._builder.store(arg, alloca)
            self._locals[param.name] = alloca

        # Corpo
        for stmt in decl.body.statements:
            self._gen_statement(stmt)

        # Terminador padrão para void
        if not self._builder.block.is_terminated:
            if isinstance(fn.ftype.return_type, ir.VoidType):
                self._builder.ret_void()
            else:
                self._builder.ret(_default_value(fn.ftype.return_type))

        self._current_scope = prev_scope
        self._locals = prev_locals

    def _gen_class(self, decl: ClassDeclaration) -> None:
        prev_class = self._current_class
        self._current_class = self._analyzer.classes[decl.name]

        for member in decl.members:
            if isinstance(member, MethodDeclaration):
                self._declare_function(member, class_prefix=decl.name)
        for member in decl.members:
            if isinstance(member, MethodDeclaration):
                self._gen_function(member, class_prefix=decl.name)
            elif isinstance(member, ConstructorDeclaration):
                self._gen_constructor(member, decl.name)

        self._current_class = prev_class

    def _gen_global_init(self, stmts: list[Node]) -> None:
        """Gera @__jss_global_init com os statements globais do programa."""
        fntype = ir.FunctionType(_VOID, [])
        fn = ir.Function(self._module, fntype, name="__jss_global_init")
        entry = fn.append_basic_block("entry")
        self._builder = ir.IRBuilder(entry)

        prev_scope  = self._current_scope
        prev_locals = self._locals
        self._current_scope = self._analyzer.global_scope
        self._locals = {}

        # Pré-passagem: alloca de vars locais declaradas nos statements globais
        for stmt in stmts:
            if isinstance(stmt, (IfStatement, WhileStatement, ForStatement)):
                self._alloca_block_deep(stmt)

        for stmt in stmts:
            self._gen_statement(stmt)

        if not self._builder.block.is_terminated:
            self._builder.ret_void()

        self._current_scope = prev_scope
        self._locals = prev_locals

    def _gen_entry_main(self, has_global_init: bool, has_user_main: bool) -> None:
        """Gera @main real do executável (entry point para clang/SO), retorna i32."""
        fntype = ir.FunctionType(_INT, [])
        fn = ir.Function(self._module, fntype, name="main")
        entry = fn.append_basic_block("entry")
        self._builder = ir.IRBuilder(entry)

        # Caso 1 — executa statements globais via __jss_global_init
        if has_global_init:
            init_fn = self._module.globals.get("__jss_global_init")
            if init_fn is not None:
                self._builder.call(init_fn, [])

        # Caso 2 — chama a main do usuário (renomeada para __jss_user_main)
        if has_user_main:
            user_main_fn = self._module.globals.get("__jss_user_main")
            if user_main_fn is not None:
                self._builder.call(user_main_fn, [])

        self._builder.ret(ir.Constant(_INT, 0))

    def _gen_constructor(self, decl: ConstructorDeclaration, class_name: str) -> None:
        struct = self._struct_types[class_name]
        struct_ptr_t = struct.as_pointer()
        param_types = [_llvm_type(TypeInfo(p.type_node.name, p.type_node.is_array)) for p in decl.params]
        fntype = ir.FunctionType(struct_ptr_t, param_types)
        fn_name = f"{class_name}.constructor"
        fn = ir.Function(self._module, fntype, name=fn_name)

        entry = fn.append_basic_block("entry")
        self._builder = ir.IRBuilder(entry)
        prev_locals = self._locals
        self._locals = {}

        # Aloca struct no heap
        size = struct.get_abi_size(self._module.data_layout) if hasattr(struct, "get_abi_size") else 8
        size_val = ir.Constant(ir.IntType(64), size)
        raw = self._builder.call(self._malloc, [size_val], name="raw")
        obj_ptr = self._builder.bitcast(raw, struct_ptr_t, name="obj")
        self_alloca = self._builder.alloca(struct_ptr_t, name="self")
        self._builder.store(obj_ptr, self_alloca)
        self._locals["self"] = self_alloca

        for i, param in enumerate(decl.params):
            arg = fn.args[i]
            param_t = _llvm_type(TypeInfo(param.type_node.name, param.type_node.is_array))
            alloca = self._builder.alloca(param_t, name=param.name)
            self._builder.store(arg, alloca)
            self._locals[param.name] = alloca

        prev_scope = self._current_scope
        self._current_scope = decl.body.scope
        self._alloca_locals(decl.body)
        for stmt in decl.body.statements:
            self._gen_statement(stmt)
        self._current_scope = prev_scope

        if not self._builder.block.is_terminated:
            result = self._builder.load(self_alloca, name="ret_obj")
            self._builder.ret(result)

        self._locals = prev_locals

    # ------------------------------------------------------------------
    # Pré-passagem: alloca de variáveis locais
    # ------------------------------------------------------------------

    def _alloca_locals(self, block: Block) -> None:
        for stmt in block.statements:
            if isinstance(stmt, VarDeclaration):
                llvm_t = _llvm_type_from_type_node(stmt.type_node)
                for d in stmt.declarators:
                    if d.name not in self._locals:
                        self._locals[d.name] = self._builder.alloca(llvm_t, name=d.name)  # type: ignore[union-attr]
            elif isinstance(stmt, (IfStatement, WhileStatement, ForStatement)):
                self._alloca_block_deep(stmt)

    def _alloca_block_deep(self, stmt: Node) -> None:
        if isinstance(stmt, IfStatement):
            self._alloca_locals(stmt.then_branch)
            if isinstance(stmt.else_branch, Block):
                self._alloca_locals(stmt.else_branch)
            elif isinstance(stmt.else_branch, IfStatement):
                self._alloca_block_deep(stmt.else_branch)
        elif isinstance(stmt, WhileStatement):
            self._alloca_locals(stmt.body)
        elif isinstance(stmt, ForStatement):
            if isinstance(stmt.initializer, VarDeclaration):
                llvm_t = _llvm_type_from_type_node(stmt.initializer.type_node)
                for d in stmt.initializer.declarators:
                    if d.name not in self._locals:
                        self._locals[d.name] = self._builder.alloca(llvm_t, name=d.name)  # type: ignore[union-attr]
            self._alloca_locals(stmt.body)

    # ------------------------------------------------------------------
    # Statements
    # ------------------------------------------------------------------

    def _gen_statement(self, stmt: Node) -> None:
        if self._builder and self._builder.block.is_terminated:
            return
        if isinstance(stmt, VarDeclaration):
            self._gen_var_decl(stmt)
        elif isinstance(stmt, ExpressionStatement):
            self._gen_expr(stmt.expression)
        elif isinstance(stmt, IfStatement):
            self._gen_if(stmt)
        elif isinstance(stmt, WhileStatement):
            self._gen_while(stmt)
        elif isinstance(stmt, ForStatement):
            self._gen_for(stmt)
        elif isinstance(stmt, ReturnStatement):
            self._gen_return(stmt)
        elif isinstance(stmt, BreakStatement):
            self._gen_break()
        elif isinstance(stmt, Block):
            prev = self._current_scope
            self._current_scope = stmt.scope
            for s in stmt.statements:
                self._gen_statement(s)
            self._current_scope = prev

    def _gen_var_decl(self, decl: VarDeclaration) -> None:
        base = TypeInfo(decl.type_node.name, decl.type_node.is_array,
                        2 if decl.type_node.array_size2 is not None else 1)
        for d in decl.declarators:
            alloca = self._locals.get(d.name)
            if alloca is None:
                continue
            if d.initializer is not None:
                val = self._gen_expr(d.initializer)
                val = self._coerce(val, self._type_of(d.initializer), base)
                self._builder.store(val, alloca)  # type: ignore[union-attr]
            elif d.array_values:
                for i, v_node in enumerate(d.array_values):
                    v = self._gen_expr(v_node)
                    v = self._coerce(v, self._type_of(v_node), TypeInfo(decl.type_node.name))
                    ptr = self._builder.gep(alloca, [ir.Constant(_INT, 0), ir.Constant(_INT, i)], inbounds=True)  # type: ignore[union-attr]
                    self._builder.store(v, ptr)  # type: ignore[union-attr]

    def _gen_if(self, stmt: IfStatement) -> None:
        fn = self._builder.function  # type: ignore[union-attr]
        then_bb  = fn.append_basic_block("if_then")
        else_bb  = fn.append_basic_block("if_else")
        merge_bb = fn.append_basic_block("if_merge")

        cond = self._gen_expr(stmt.condition)
        self._builder.cbranch(cond, then_bb, else_bb)  # type: ignore[union-attr]

        # then
        self._builder = ir.IRBuilder(then_bb)
        prev = self._current_scope
        self._current_scope = stmt.then_branch.scope
        for s in stmt.then_branch.statements:
            self._gen_statement(s)
        self._current_scope = prev
        if not self._builder.block.is_terminated:
            self._builder.branch(merge_bb)

        # else
        self._builder = ir.IRBuilder(else_bb)
        if stmt.else_branch is not None:
            if isinstance(stmt.else_branch, Block):
                self._current_scope = stmt.else_branch.scope
                for s in stmt.else_branch.statements:
                    self._gen_statement(s)
                self._current_scope = prev
            elif isinstance(stmt.else_branch, IfStatement):
                self._gen_if(stmt.else_branch)
        if not self._builder.block.is_terminated:
            self._builder.branch(merge_bb)

        self._builder = ir.IRBuilder(merge_bb)

    def _gen_while(self, stmt: WhileStatement) -> None:
        fn = self._builder.function  # type: ignore[union-attr]
        cond_bb = fn.append_basic_block("while_cond")
        body_bb = fn.append_basic_block("while_body")
        end_bb  = fn.append_basic_block("while_end")

        self._builder.branch(cond_bb)  # type: ignore[union-attr]

        self._builder = ir.IRBuilder(cond_bb)
        cond = self._gen_expr(stmt.condition)
        self._builder.cbranch(cond, body_bb, end_bb)

        self._builder = ir.IRBuilder(body_bb)
        self._break_stack.append(end_bb)
        prev = self._current_scope
        self._current_scope = stmt.body.scope
        for s in stmt.body.statements:
            self._gen_statement(s)
        self._current_scope = prev
        self._break_stack.pop()
        if not self._builder.block.is_terminated:
            self._builder.branch(cond_bb)

        self._builder = ir.IRBuilder(end_bb)

    def _gen_for(self, stmt: ForStatement) -> None:
        fn = self._builder.function  # type: ignore[union-attr]
        cond_bb = fn.append_basic_block("for_cond")
        body_bb = fn.append_basic_block("for_body")
        end_bb  = fn.append_basic_block("for_end")

        if stmt.initializer is not None:
            if isinstance(stmt.initializer, VarDeclaration):
                self._gen_var_decl(stmt.initializer)
            else:
                self._gen_expr(stmt.initializer)

        self._builder.branch(cond_bb)  # type: ignore[union-attr]
        self._builder = ir.IRBuilder(cond_bb)

        if stmt.condition is not None:
            cond = self._gen_expr(stmt.condition)
            self._builder.cbranch(cond, body_bb, end_bb)
        else:
            self._builder.branch(body_bb)

        self._builder = ir.IRBuilder(body_bb)
        self._break_stack.append(end_bb)
        prev = self._current_scope
        self._current_scope = stmt.body.scope
        for s in stmt.body.statements:
            self._gen_statement(s)
        self._current_scope = prev
        self._break_stack.pop()

        if not self._builder.block.is_terminated:
            if stmt.increment is not None:
                self._gen_expr(stmt.increment)
            self._builder.branch(cond_bb)

        self._builder = ir.IRBuilder(end_bb)

    def _gen_return(self, stmt: ReturnStatement) -> None:
        if stmt.value is None:
            self._builder.ret_void()  # type: ignore[union-attr]
        else:
            val = self._gen_expr(stmt.value)
            fn_ret = self._builder.function.ftype.return_type  # type: ignore[union-attr]
            val = self._coerce(val, self._type_of(stmt.value), self._llvm_to_typeinfo(fn_ret))
            self._builder.ret(val)  # type: ignore[union-attr]

    def _gen_break(self) -> None:
        if self._break_stack:
            self._builder.branch(self._break_stack[-1])  # type: ignore[union-attr]

    # ------------------------------------------------------------------
    # Curto-circuito — && e ||
    # ------------------------------------------------------------------

    def _gen_logical_and(self, node: BinaryOperation) -> ir.Value:
        """A && B: avalia B apenas se A for true."""
        fn = self._builder.function  # type: ignore[union-attr]
        rhs_bb = fn.append_basic_block("and_rhs")
        end_bb = fn.append_basic_block("and_end")

        # Avalia lado esquerdo
        lt = self._type_of(node.left)
        lv = self._gen_expr(node.left)
        lv = self._coerce(lv, lt, TypeInfo("bool"))
        left_block = self._builder.block  # type: ignore[union-attr]
        # false → pula RHS direto para end
        if not self._builder.block.is_terminated:  # type: ignore[union-attr]
            self._builder.cbranch(lv, rhs_bb, end_bb)  # type: ignore[union-attr]

        # Avalia lado direito (só executa se left == true)
        self._builder = ir.IRBuilder(rhs_bb)
        rt = self._type_of(node.right)
        rv = self._gen_expr(node.right)
        rv = self._coerce(rv, rt, TypeInfo("bool"))
        rhs_end_block = self._builder.block
        if not self._builder.block.is_terminated:
            self._builder.branch(end_bb)

        # PHI: false (do left_block) ou rv (do rhs_end_block)
        self._builder = ir.IRBuilder(end_bb)
        phi = self._builder.phi(_BOOL, name="andtmp")
        phi.add_incoming(ir.Constant(_BOOL, 0), left_block)
        phi.add_incoming(rv, rhs_end_block)
        return phi

    def _gen_logical_or(self, node: BinaryOperation) -> ir.Value:
        """A || B: avalia B apenas se A for false."""
        fn = self._builder.function  # type: ignore[union-attr]
        rhs_bb = fn.append_basic_block("or_rhs")
        end_bb = fn.append_basic_block("or_end")

        # Avalia lado esquerdo
        lt = self._type_of(node.left)
        lv = self._gen_expr(node.left)
        lv = self._coerce(lv, lt, TypeInfo("bool"))
        left_block = self._builder.block  # type: ignore[union-attr]
        # true → pula RHS direto para end
        if not self._builder.block.is_terminated:  # type: ignore[union-attr]
            self._builder.cbranch(lv, end_bb, rhs_bb)  # type: ignore[union-attr]

        # Avalia lado direito (só executa se left == false)
        self._builder = ir.IRBuilder(rhs_bb)
        rt = self._type_of(node.right)
        rv = self._gen_expr(node.right)
        rv = self._coerce(rv, rt, TypeInfo("bool"))
        rhs_end_block = self._builder.block
        if not self._builder.block.is_terminated:
            self._builder.branch(end_bb)

        # PHI: true (do left_block) ou rv (do rhs_end_block)
        self._builder = ir.IRBuilder(end_bb)
        phi = self._builder.phi(_BOOL, name="ortmp")
        phi.add_incoming(ir.Constant(_BOOL, 1), left_block)
        phi.add_incoming(rv, rhs_end_block)
        return phi

    # ------------------------------------------------------------------
    # Potência inteira — __jss_pow_i32
    # ------------------------------------------------------------------

    def _ensure_pow_i32(self) -> ir.Function:
        """Garante que @__jss_pow_i32 existe no módulo e retorna a função."""
        existing = self._module.globals.get("__jss_pow_i32")
        if existing is not None:
            return existing  # type: ignore[return-value]

        # define i32 @__jss_pow_i32(i32 %base, i32 %exp)
        fntype = ir.FunctionType(_INT, [_INT, _INT])
        fn = ir.Function(self._module, fntype, name="__jss_pow_i32")
        base_arg, exp_arg = fn.args

        saved_builder = self._builder

        entry_bb  = fn.append_basic_block("entry")
        cond_bb   = fn.append_basic_block("cond")
        body_bb   = fn.append_basic_block("body")
        exit_bb   = fn.append_basic_block("exit")

        b = ir.IRBuilder(entry_bb)
        # expoente <= 0: resultado = 1 (0^0 = 1 por convenção)
        result_ptr = b.alloca(_INT, name="result")
        i_ptr      = b.alloca(_INT, name="i")
        b.store(ir.Constant(_INT, 1), result_ptr)
        b.store(ir.Constant(_INT, 0), i_ptr)
        b.branch(cond_bb)

        b = ir.IRBuilder(cond_bb)
        i_val   = b.load(i_ptr, name="i")
        # se exp_arg <= 0, não entra no loop (resultado já é 1)
        cond = b.icmp_signed("<", i_val, exp_arg)
        b.cbranch(cond, body_bb, exit_bb)

        b = ir.IRBuilder(body_bb)
        res = b.load(result_ptr, name="res")
        new_res = b.mul(res, base_arg, name="new_res")
        b.store(new_res, result_ptr)
        i_cur = b.load(i_ptr, name="i_cur")
        b.store(b.add(i_cur, ir.Constant(_INT, 1)), i_ptr)
        b.branch(cond_bb)

        b = ir.IRBuilder(exit_bb)
        final = b.load(result_ptr, name="final")
        b.ret(final)

        self._builder = saved_builder
        self._pow_i32 = fn
        return fn

    def _gen_power(self, lv: ir.Value, rv: ir.Value, lt: TypeInfo, rt: TypeInfo) -> ir.Value:
        """Gera instrução de potência — por enquanto suporta int ** int."""
        pow_fn = self._ensure_pow_i32()
        return self._builder.call(pow_fn, [lv, rv])  # type: ignore[union-attr]

    # ------------------------------------------------------------------
    # Expressões — retornam ir.Value
    # ------------------------------------------------------------------

    def _gen_expr(self, node: Node) -> ir.Value:
        if isinstance(node, Literal):
            return self._gen_literal(node)
        if isinstance(node, Identifier):
            return self._gen_identifier(node)
        if isinstance(node, BinaryOperation):
            return self._gen_binary(node)
        if isinstance(node, UnaryOperation):
            return self._gen_unary(node)
        if isinstance(node, Assignment):
            return self._gen_assignment(node)
        if isinstance(node, Call):
            return self._gen_call(node)
        if isinstance(node, IndexAccess):
            return self._gen_index_access(node)
        if isinstance(node, AttributeAccess):
            return self._gen_attribute_access(node)
        if isinstance(node, NewObject):
            return self._gen_new_object(node)
        raise NotImplementedError(f"Expressão não suportada: {type(node).__name__}")

    def _gen_literal(self, node: Literal) -> ir.Value:
        if node.literal_type == "int":
            return ir.Constant(_INT, int(node.value))
        if node.literal_type == "real":
            return ir.Constant(_REAL, float(node.value))
        if node.literal_type == "bool":
            return ir.Constant(_BOOL, int(bool(node.value)))
        if node.literal_type == "str":
            return self._make_string_constant(str(node.value))
        if node.literal_type == "null":
            return ir.Constant(_INT, 0)
        raise NotImplementedError(f"Literal não suportado: {node.literal_type}")

    def _make_string_global(self, value: str) -> ir.GlobalVariable:
        """Cria constante global [N x i8] para uma string literal."""
        encoded = (value + "\0").encode("utf-8")
        arr_t   = ir.ArrayType(ir.IntType(8), len(encoded))
        gvar    = ir.GlobalVariable(self._module, arr_t, name=self._module.get_unique_name("str"))
        gvar.global_constant = True
        gvar.initializer     = ir.Constant(arr_t, bytearray(encoded))
        gvar.linkage         = "private"
        return gvar

    def _string_global_ptr_constant(self, gvar: ir.GlobalVariable) -> ir.Constant:
        """Retorna GEP constante i8* para usar como inicializador de variável global str."""
        zero = ir.Constant(_INT, 0)
        return gvar.gep([zero, zero])  # type: ignore[return-value]

    def _make_string_constant(self, value: str) -> ir.Value:
        """Retorna ponteiro i8* para string — usa builder.gep (dentro de função)."""
        gvar = self._make_string_global(value)
        zero = ir.Constant(_INT, 0)
        return self._builder.gep(gvar, [zero, zero], inbounds=True, name="strptr")  # type: ignore[union-attr]

    def _gen_identifier(self, node: Identifier) -> ir.Value:
        ptr = self._ptr_of_name(node.name)
        if ptr is not None:
            return self._builder.load(ptr, name=node.name)  # type: ignore[union-attr]
        return ir.Constant(_INT, 0)

    def _gen_binary(self, node: BinaryOperation) -> ir.Value:
        b   = self._builder
        op  = node.operator.type

        # Curto-circuito: && e || interceptam antes de avaliar ambos os lados
        if op == TokenType.AND_AND:
            return self._gen_logical_and(node)
        if op == TokenType.OR_OR:
            return self._gen_logical_or(node)

        lt  = self._type_of(node.left)
        rt  = self._type_of(node.right)

        lv  = self._gen_expr(node.left)
        rv  = self._gen_expr(node.right)

        # Promoção int → real
        is_real = lt.name == "real" or rt.name == "real"
        if is_real:
            if lt.name == "int":
                lv = b.sitofp(lv, _REAL)  # type: ignore[union-attr]
            if rt.name == "int":
                rv = b.sitofp(rv, _REAL)  # type: ignore[union-attr]

        if op == TokenType.PLUS:
            return b.fadd(lv, rv) if is_real else b.add(lv, rv)  # type: ignore[union-attr]
        if op == TokenType.MINUS:
            return b.fsub(lv, rv) if is_real else b.sub(lv, rv)  # type: ignore[union-attr]
        if op == TokenType.STAR:
            return b.fmul(lv, rv) if is_real else b.mul(lv, rv)  # type: ignore[union-attr]
        if op == TokenType.SLASH:
            return b.fdiv(lv, rv) if is_real else b.sdiv(lv, rv)  # type: ignore[union-attr]
        if op == TokenType.PERCENT:
            return b.srem(lv, rv)  # type: ignore[union-attr]
        if op == TokenType.POWER:
            return self._gen_power(lv, rv, lt, rt)

        # Comparações
        cmp_map_int  = {
            TokenType.EQUAL_EQUAL: "==", TokenType.BANG_EQUAL: "!=",
            TokenType.GREATER: ">",      TokenType.GREATER_EQUAL: ">=",
            TokenType.LESS: "<",         TokenType.LESS_EQUAL: "<=",
        }
        cmp_map_real = {
            TokenType.EQUAL_EQUAL: "==", TokenType.BANG_EQUAL: "!=",
            TokenType.GREATER: ">",      TokenType.GREATER_EQUAL: ">=",
            TokenType.LESS: "<",         TokenType.LESS_EQUAL: "<=",
        }
        if op in cmp_map_int:
            if is_real:
                return b.fcmp_ordered(cmp_map_real[op], lv, rv)  # type: ignore[union-attr]
            return b.icmp_signed(cmp_map_int[op], lv, rv)  # type: ignore[union-attr]

        return ir.Constant(_INT, 0)

    def _gen_unary(self, node: UnaryOperation) -> ir.Value:
        b   = self._builder
        op  = node.operator.type
        ot  = self._type_of(node.operand)
        ov  = self._gen_expr(node.operand)

        if op == TokenType.MINUS:
            return b.fneg(ov) if ot.name == "real" else b.neg(ov)  # type: ignore[union-attr]
        if op == TokenType.BANG:
            return b.not_(ov)  # type: ignore[union-attr]
        if op in {TokenType.PLUS_PLUS, TokenType.MINUS_MINUS}:
            one = ir.Constant(_REAL, 1.0) if ot.name == "real" else ir.Constant(_INT, 1)
            new_val = b.fadd(ov, one) if ot.name == "real" else (  # type: ignore[union-attr]
                b.add(ov, one) if op == TokenType.PLUS_PLUS else b.sub(ov, one)  # type: ignore[union-attr]
            )
            ptr = self._ptr_of(node.operand)
            if ptr is not None:
                b.store(new_val, ptr)  # type: ignore[union-attr]
            return ov if node.postfix else new_val

        return ov

    def _gen_assignment(self, node: Assignment) -> ir.Value:
        val    = self._gen_expr(node.value)
        target = self._type_of(node.target)
        val    = self._coerce(val, self._type_of(node.value), target)
        op     = node.operator.type

        if op != TokenType.ASSIGN:
            cur = self._gen_expr(node.target)
            is_real = target.name == "real"
            compound = {
                TokenType.PLUS_ASSIGN:    (lambda a, b: self._builder.fadd(a, b) if is_real else self._builder.add(a, b)),  # type: ignore[union-attr]
                TokenType.MINUS_ASSIGN:   (lambda a, b: self._builder.fsub(a, b) if is_real else self._builder.sub(a, b)),  # type: ignore[union-attr]
                TokenType.STAR_ASSIGN:    (lambda a, b: self._builder.fmul(a, b) if is_real else self._builder.mul(a, b)),  # type: ignore[union-attr]
                TokenType.SLASH_ASSIGN:   (lambda a, b: self._builder.fdiv(a, b) if is_real else self._builder.sdiv(a, b)),  # type: ignore[union-attr]
                TokenType.PERCENT_ASSIGN: (lambda a, b: self._builder.srem(a, b)),  # type: ignore[union-attr]
                TokenType.POWER_ASSIGN:   (lambda a, b: self._builder.call(self._ensure_pow_i32(), [a, b])),  # type: ignore[union-attr]
            }
            val = compound[op](cur, val)

        ptr = self._ptr_of(node.target)
        if ptr is not None:
            self._builder.store(val, ptr)  # type: ignore[union-attr]
        return val

    def _gen_call(self, node: Call) -> ir.Value:
        if node.native:
            return self._gen_native_call(node)

        if isinstance(node.callee, Identifier):
            fn = self._module.globals.get(node.callee.name)
            if fn is None:
                return ir.Constant(_INT, 0)
            args = [self._coerce_arg(a, t) for a, t in zip(node.arguments, fn.ftype.args)]
            return self._builder.call(fn, args)  # type: ignore[union-attr]

        if isinstance(node.callee, AttributeAccess):
            obj_val = self._gen_expr(node.callee.object_expr)
            obj_type = self._type_of(node.callee.object_expr)
            fn_name = f"{obj_type.name}.{node.callee.attribute}"
            fn = self._module.globals.get(fn_name)
            if fn is None:
                return ir.Constant(_INT, 0)
            args = [obj_val] + [self._coerce_arg(a, t) for a, t in zip(node.arguments, fn.ftype.args[1:])]
            return self._builder.call(fn, args)  # type: ignore[union-attr]

        return ir.Constant(_INT, 0)

    def _gen_native_call(self, node: Call) -> ir.Value:
        callee_name = node.callee.name if isinstance(node.callee, Identifier) else ""

        if callee_name == "console.log":
            # Etapa 1: avalia todos os argumentos e coleta (valor_llvm, type_info)
            evaluated: list[tuple[ir.Value, TypeInfo]] = []
            for arg in node.arguments:
                val = self._gen_expr(arg)
                t   = self._type_of(arg)
                # bool → "true"/"false" via select
                if t.name == "bool":
                    true_ptr  = self._make_string_constant("true")
                    false_ptr = self._make_string_constant("false")
                    val = self._builder.select(val, true_ptr, false_ptr)  # type: ignore[union-attr]
                    t   = TypeInfo("str")
                evaluated.append((val, t))

            # Etapa 2: monta formato composto com especificadores separados por espaço + \n no final
            _FMT_SPEC = {"int": "%d", "real": "%f", "str": "%s"}
            specs = [_FMT_SPEC.get(t.name, "%d") for _, t in evaluated]
            fmt_str = " ".join(specs) + "\n"

            # Etapa 3: cria constante global com o formato composto
            fmt_ptr = self._make_string_constant(fmt_str)

            # Etapa 4: um único call printf(fmt, arg1, arg2, ...)
            call_args = [fmt_ptr] + [val for val, _ in evaluated]
            self._builder.call(self._printf, call_args)  # type: ignore[union-attr]
            return ir.Constant(_INT, 0)

        if callee_name == "input":
            for arg in node.arguments:
                t   = self._type_of(arg)
                fmt = self._fmt_string(t, newline=False)
                ptr = self._ptr_of(arg)
                if ptr is not None:
                    self._builder.call(self._scanf, [fmt, ptr])  # type: ignore[union-attr]
            return ir.Constant(_INT, 0)

        if callee_name in {"int", "real", "bool"} and node.arguments:
            src     = self._gen_expr(node.arguments[0])
            src_t   = self._type_of(node.arguments[0])
            dest_t  = TypeInfo(callee_name)
            return self._coerce(src, src_t, dest_t)

        return ir.Constant(_INT, 0)

    def _gen_index_access(self, node: IndexAccess) -> ir.Value:
        ptr = self._ptr_of(node)
        if ptr is None:
            return ir.Constant(_INT, 0)
        return self._builder.load(ptr)  # type: ignore[union-attr]

    def _gen_attribute_access(self, node: AttributeAccess) -> ir.Value:
        ptr = self._ptr_of(node)
        if ptr is None:
            return ir.Constant(_INT, 0)
        return self._builder.load(ptr)  # type: ignore[union-attr]

    def _gen_new_object(self, node: NewObject) -> ir.Value:
        fn_name = f"{node.class_name}.constructor"
        fn = self._module.globals.get(fn_name)
        if fn is None:
            return ir.Constant(_INT, 0)
        args = [self._coerce_arg(a, t) for a, t in zip(node.arguments, fn.ftype.args)]
        return self._builder.call(fn, args)  # type: ignore[union-attr]

    # ------------------------------------------------------------------
    # Coerção de tipos
    # ------------------------------------------------------------------

    def _coerce(self, val: ir.Value, from_t: TypeInfo, to_t: TypeInfo) -> ir.Value:
        if from_t.name == to_t.name:
            return val
        b = self._builder
        if from_t.name == "int" and to_t.name == "real":
            return b.sitofp(val, _REAL)  # type: ignore[union-attr]
        if from_t.name == "real" and to_t.name == "int":
            return b.fptosi(val, _INT)  # type: ignore[union-attr]
        if from_t.name == "int" and to_t.name == "bool":
            return b.icmp_signed("!=", val, ir.Constant(_INT, 0))  # type: ignore[union-attr]
        if from_t.name == "bool" and to_t.name == "int":
            return b.zext(val, _INT)  # type: ignore[union-attr]
        if from_t.name == "bool" and to_t.name == "real":
            i = b.zext(val, _INT)  # type: ignore[union-attr]
            return b.sitofp(i, _REAL)  # type: ignore[union-attr]
        return val

    def _coerce_arg(self, arg_node: Node, expected_llvm: ir.Type) -> ir.Value:
        val   = self._gen_expr(arg_node)
        src_t = self._type_of(arg_node)
        dst_t = self._llvm_to_typeinfo(expected_llvm)
        return self._coerce(val, src_t, dst_t)

    # ------------------------------------------------------------------
    # Ponteiros para lvalue (endereço de uma variável/elemento)
    # ------------------------------------------------------------------

    def _ptr_of(self, node: Node) -> ir.Value | None:
        if isinstance(node, Identifier):
            return self._ptr_of_name(node.name)
        if isinstance(node, IndexAccess):
            return self._ptr_of_index_access(node)
        if isinstance(node, AttributeAccess):
            obj_val  = self._gen_expr(node.object_expr)
            obj_t    = self._type_of(node.object_expr)
            ci       = self._analyzer.classes.get(obj_t.name)
            if ci is None:
                return None
            idx      = list(ci.attributes.keys()).index(node.attribute)
            zero     = ir.Constant(_INT, 0)
            field_i  = ir.Constant(_INT, idx)
            return self._builder.gep(obj_val, [zero, field_i], inbounds=True)  # type: ignore[union-attr]
        return None

    def _ptr_of_index_access(self, node: IndexAccess) -> ir.Value | None:
        """Coleta índices encadeados e gera um único GEP (1D e 2D)."""
        indices: list[Node] = []
        current: Node = node
        while isinstance(current, IndexAccess):
            indices.append(current.index)
            current = current.collection
        indices.reverse()  # ordem: exterior → interior = esquerda → direita

        if not isinstance(current, Identifier):
            return None
        coll_ptr = self._ptr_of_name(current.name)
        if coll_ptr is None:
            return None

        zero = ir.Constant(_INT, 0)
        idx_vals = [self._gen_expr(i) for i in indices]
        return self._builder.gep(coll_ptr, [zero] + idx_vals, inbounds=True)  # type: ignore[union-attr]

    def _ptr_of_name(self, name: str) -> ir.Value | None:
        if name in self._locals:
            return self._locals[name]
        if name in self._globals:
            return self._globals[name]
        return None

    # ------------------------------------------------------------------
    # Helpers de tipo
    # ------------------------------------------------------------------

    def _resolve(self, name: str) -> SemanticSymbol | None:
        if self._current_scope:
            return self._current_scope.resolve(name)
        return self._analyzer.global_scope.resolve(name)

    def _type_of(self, node: Node) -> TypeInfo:
        if isinstance(node, Literal):
            return TypeInfo(node.literal_type)
        if isinstance(node, Identifier):
            sym = self._resolve(node.name)
            return sym.type_info if sym else TypeInfo("int")
        if isinstance(node, BinaryOperation):
            lt = self._type_of(node.left)
            rt = self._type_of(node.right)
            cmp_ops = {
                TokenType.EQUAL_EQUAL, TokenType.BANG_EQUAL,
                TokenType.GREATER, TokenType.GREATER_EQUAL,
                TokenType.LESS, TokenType.LESS_EQUAL,
                TokenType.AND_AND, TokenType.OR_OR,
            }
            if node.operator.type in cmp_ops:
                return TypeInfo("bool")
            if lt.name == "real" or rt.name == "real":
                return TypeInfo("real")
            return lt
        if isinstance(node, UnaryOperation):
            return self._type_of(node.operand)
        if isinstance(node, IndexAccess):
            ct = self._type_of(node.collection)
            return TypeInfo(ct.name)
        if isinstance(node, AttributeAccess):
            obj_t = self._type_of(node.object_expr)
            ci    = self._analyzer.classes.get(obj_t.name)
            if ci:
                sym = ci.attributes.get(node.attribute) or ci.methods.get(node.attribute)
                if sym:
                    return sym.type_info
        if isinstance(node, Call):
            if node.native:
                callee = node.callee.name if isinstance(node.callee, Identifier) else ""
                if callee in {"int", "real", "bool", "str"}:
                    return TypeInfo(callee)
                return TypeInfo("void")
            if isinstance(node.callee, Identifier):
                sym = self._resolve(node.callee.name)
                if sym:
                    return sym.type_info
        if isinstance(node, NewObject):
            return TypeInfo(node.class_name)
        if isinstance(node, Assignment):
            return self._type_of(node.target)
        return TypeInfo("int")

    def _find_var_declaration(self, name: str) -> VarDeclaration | None:
        """Busca a VarDeclaration global que declara a variável pelo nome."""
        for decl in self._program.declarations:
            if isinstance(decl, VarDeclaration):
                for d in decl.declarators:
                    if d.name == name:
                        return decl
        return None

    def _find_global_literal_init(self, name: str, type_info: TypeInfo) -> ir.Constant | None:
        """Busca o inicializador literal de uma variável global na AST."""
        for decl in self._program.declarations:
            if isinstance(decl, VarDeclaration):
                for d in decl.declarators:
                    if d.name == name and isinstance(d.initializer, Literal):
                        return self._literal_constant(d.initializer, type_info)
        return None

    def _literal_constant(self, node: Literal, type_info: TypeInfo) -> ir.Constant:
        """Converte um nó Literal da AST em ir.Constant do llvmlite."""
        if node.literal_type == "int":
            return ir.Constant(_INT, int(node.value))
        if node.literal_type == "real":
            return ir.Constant(_REAL, float(node.value))
        if node.literal_type == "bool":
            return ir.Constant(_BOOL, int(bool(node.value)))
        if node.literal_type == "str":
            gvar = self._make_string_global(str(node.value))
            return self._string_global_ptr_constant(gvar)
        return _default_value(_llvm_type(type_info))

    def _llvm_to_typeinfo(self, t: ir.Type) -> TypeInfo:
        if t == _INT:
            return TypeInfo("int")
        if t == _REAL:
            return TypeInfo("real")
        if t == _BOOL:
            return TypeInfo("bool")
        if t == _STR:
            return TypeInfo("str")
        return TypeInfo("int")

    def _fmt_string(self, t: TypeInfo, newline: bool) -> ir.Value:
        suffix = "\\n" if newline else ""
        fmts   = {"int": f"%d{suffix}", "real": f"%f{suffix}", "bool": f"%d{suffix}", "str": f"%s{suffix}"}
        raw    = fmts.get(t.name, f"%d{suffix}")
        return self._make_string_constant(raw.replace("\\n", "\n"))


# ---------------------------------------------------------------------------
# Função pública
# ---------------------------------------------------------------------------

def generate_llvm(program: Program, analyzer: SemanticAnalyzer) -> str:
    """Gera LLVM IR usando llvmlite e retorna o texto do módulo."""
    return LLVMGenerator(program, analyzer).generate()
