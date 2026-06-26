"""Converte a árvore de parsing ANTLR4 nos nós AST existentes (ast_nodes.py)."""

from __future__ import annotations

from antlr4 import TerminalNode  # type: ignore[import-untyped]

from .antlr_generated.JSSLexer import JSSLexer
from .antlr_generated.JSSParser import JSSParser
from .antlr_generated.JSSVisitor import JSSVisitor
from .ast_nodes import (
    Assignment,
    AttributeAccess,
    AttributeDeclaration,
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
    Parameter,
    Program,
    ReturnStatement,
    Symbol,
    This,
    TypeNode,
    UnaryOperation,
    VarDeclaration,
    WhileStatement,
)
from .errors import RawSyntaxErrorJSS, SyntaxErrorJSS
from .tokens import Token, TokenType

# Mapeamento de tipo ANTLR → TokenType JSS (usado para operadores em nós AST)
_ANTLR_TO_JSS: dict[int, TokenType] = {
    JSSLexer.ASSIGN:          TokenType.ASSIGN,
    JSSLexer.PLUS_ASSIGN:     TokenType.PLUS_ASSIGN,
    JSSLexer.MINUS_ASSIGN:    TokenType.MINUS_ASSIGN,
    JSSLexer.STAR_ASSIGN:     TokenType.STAR_ASSIGN,
    JSSLexer.SLASH_ASSIGN:    TokenType.SLASH_ASSIGN,
    JSSLexer.PERCENT_ASSIGN:  TokenType.PERCENT_ASSIGN,
    JSSLexer.POWER_ASSIGN:    TokenType.POWER_ASSIGN,
    JSSLexer.PLUS:            TokenType.PLUS,
    JSSLexer.MINUS:           TokenType.MINUS,
    JSSLexer.STAR:            TokenType.STAR,
    JSSLexer.SLASH:           TokenType.SLASH,
    JSSLexer.PERCENT:         TokenType.PERCENT,
    JSSLexer.POWER:           TokenType.POWER,
    JSSLexer.EQUAL_EQUAL:     TokenType.EQUAL_EQUAL,
    JSSLexer.BANG_EQUAL:      TokenType.BANG_EQUAL,
    JSSLexer.GREATER:         TokenType.GREATER,
    JSSLexer.GREATER_EQUAL:   TokenType.GREATER_EQUAL,
    JSSLexer.LESS:            TokenType.LESS,
    JSSLexer.LESS_EQUAL:      TokenType.LESS_EQUAL,
    JSSLexer.AND_AND:         TokenType.AND_AND,
    JSSLexer.OR_OR:           TokenType.OR_OR,
    JSSLexer.BANG:            TokenType.BANG,
    JSSLexer.PLUS_PLUS:       TokenType.PLUS_PLUS,
    JSSLexer.MINUS_MINUS:     TokenType.MINUS_MINUS,
}

_TYPE_NAME: dict[int, str] = {
    JSSLexer.TYPE_INT:  "int",
    JSSLexer.TYPE_REAL: "real",
    JSSLexer.TYPE_STR:  "str",
    JSSLexer.TYPE_BOOL: "bool",
}


def _is_tok(child: object, token_type: int) -> bool:
    return isinstance(child, TerminalNode) and child.symbol.type == token_type


def _make_jss_token(terminal: TerminalNode, token_type: TokenType) -> Token:
    sym = terminal.symbol
    return Token(type=token_type, lexeme=sym.text, line=sym.line, column=sym.column + 1)


class ASTBuilder(JSSVisitor):
    """Visitor que percorre a ParseTree ANTLR e produz os nós de ast_nodes.py."""

    def __init__(self) -> None:
        self._class_names: set[str] = set()

    # ── Programa ──────────────────────────────────────────────────────────────

    def visitProgram(self, ctx: JSSParser.ProgramContext) -> Program:
        # Primeira passagem: coletar nomes de classes para detectar uso sem 'new'
        for decl_ctx in ctx.declaration():
            if decl_ctx.classDecl():
                self._class_names.add(decl_ctx.classDecl().IDENTIFIER().getText())

        declarations: list[Node] = [self.visit(d) for d in ctx.declaration()]
        first = declarations[0] if declarations else None
        line = first.line if first else 1
        col = first.column if first else 1
        return Program(line=line, column=col, declarations=declarations, symbols=[])

    # ── Declarações ───────────────────────────────────────────────────────────

    def visitDeclaration(self, ctx: JSSParser.DeclarationContext) -> Node:
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx: JSSParser.VarDeclContext) -> VarDeclaration:
        return self._build_var_decl(ctx, constant=False)

    def visitConstDecl(self, ctx: JSSParser.ConstDeclContext) -> VarDeclaration:
        return self._build_var_decl(ctx, constant=True)

    def _build_var_decl(self, ctx, constant: bool) -> VarDeclaration:
        tok = ctx.start
        type_node = self.visitType_(ctx.type_())

        if ctx.arrayTypeDim():
            dim = ctx.arrayTypeDim()
            exprs = dim.expr()
            type_node.is_array = True
            type_node.array_size = self.visit(exprs[0])
            if len(exprs) > 1:
                type_node.array_size2 = self.visit(exprs[1])

        declarators = [
            self._build_declarator(d, type_node.is_array)
            for d in ctx.declarator()
        ]
        return VarDeclaration(
            line=tok.line, column=tok.column + 1,
            type_node=type_node, declarators=declarators, constant=constant,
        )

    def _build_declarator(
        self, ctx: JSSParser.DeclaratorContext, type_is_array: bool
    ) -> Declarator:
        name_term = ctx.IDENTIFIER()
        name_sym = name_term.symbol
        line, col = name_sym.line, name_sym.column + 1

        array_size: Node | None = None
        initializer: Node | None = None
        values: list[Node] = []

        # Percorre filhos manualmente para distinguir [size] do inicializador
        children = [ctx.getChild(i) for i in range(ctx.getChildCount())]
        i = 1  # pula IDENTIFIER (índice 0)

        if i < len(children) and _is_tok(children[i], JSSLexer.LEFT_BRACKET):
            if type_is_array:
                raise SyntaxErrorJSS("matriz multidimensional nao permitida", line, col)
            i += 1  # LEFT_BRACKET
            array_size = self.visit(children[i])
            i += 1  # expr
            i += 1  # RIGHT_BRACKET

        if i < len(children) and _is_tok(children[i], JSSLexer.ASSIGN):
            i += 1  # '='
            if i < len(children) and _is_tok(children[i], JSSLexer.LEFT_BRACKET):
                # Inicializador de array: '[' expr (',' expr)* ']'
                i += 1  # '['
                while i < len(children) and not _is_tok(children[i], JSSLexer.RIGHT_BRACKET):
                    if _is_tok(children[i], JSSLexer.COMMA):
                        i += 1
                        continue
                    values.append(self.visit(children[i]))
                    i += 1
            else:
                initializer = self.visit(children[i])

        return Declarator(
            line=line, column=col,
            name=name_sym.text,
            initializer=initializer,
            array_size=array_size,
            array_values=values,
        )

    # ── Tipos ─────────────────────────────────────────────────────────────────

    def visitType_(self, ctx: JSSParser.Type_Context) -> TypeNode:
        tok = ctx.start
        name = _TYPE_NAME.get(tok.type, tok.text)
        return TypeNode(line=tok.line, column=tok.column + 1, name=name)

    def visitReturnType(self, ctx: JSSParser.ReturnTypeContext) -> TypeNode:
        if ctx.VOID():
            sym = ctx.VOID().symbol
            return TypeNode(line=sym.line, column=sym.column + 1, name="void")
        type_node = self.visitType_(ctx.type_())
        if ctx.arrayTypeDim():
            dim = ctx.arrayTypeDim()
            exprs = dim.expr()
            type_node.is_array = True
            type_node.array_size = self.visit(exprs[0])
            if len(exprs) > 1:
                type_node.array_size2 = self.visit(exprs[1])
        return type_node

    # ── Funções ───────────────────────────────────────────────────────────────

    def visitFunctionDecl(self, ctx: JSSParser.FunctionDeclContext) -> FunctionDeclaration:
        tok = ctx.start
        return_type = self.visitReturnType(ctx.returnType())
        name_sym = ctx.IDENTIFIER().symbol
        params = self._build_params(ctx.parameters())
        body = self.visitBlock(ctx.block())
        return FunctionDeclaration(
            line=tok.line, column=tok.column + 1,
            return_type=return_type, name=name_sym.text, params=params, body=body,
        )

    def _build_params(self, ctx: JSSParser.ParametersContext) -> list[Parameter]:
        return [self.visitParameter(p) for p in ctx.parameter()]

    def visitParameter(self, ctx: JSSParser.ParameterContext) -> Parameter:
        type_node = self.visitType_(ctx.type_())
        if ctx.arrayTypeDim():
            dim = ctx.arrayTypeDim()
            exprs = dim.expr()
            type_node.is_array = True
            type_node.array_size = self.visit(exprs[0])
            if len(exprs) > 1:
                type_node.array_size2 = self.visit(exprs[1])
        name_sym = ctx.IDENTIFIER().symbol
        return Parameter(line=type_node.line, column=type_node.column,
                         type_node=type_node, name=name_sym.text)

    # ── Classes ───────────────────────────────────────────────────────────────

    def visitClassDecl(self, ctx: JSSParser.ClassDeclContext) -> ClassDeclaration:
        tok = ctx.start
        name = ctx.IDENTIFIER().getText()
        members: list[Node] = [self.visitClassMember(m) for m in ctx.classMember()]
        return ClassDeclaration(line=tok.line, column=tok.column + 1, name=name, members=members)

    def visitClassMember(self, ctx: JSSParser.ClassMemberContext) -> Node:
        if ctx.constructorDecl():
            return self.visitConstructorDecl(ctx.constructorDecl())
        if ctx.parameters():  # método: returnType IDENTIFIER parameters block
            return self._build_method(ctx)
        # atributo: type_ arrayTypeDim? IDENTIFIER SEMICOLON
        type_node = self.visitType_(ctx.type_())
        if ctx.arrayTypeDim():
            dim = ctx.arrayTypeDim()
            exprs = dim.expr()
            type_node.is_array = True
            type_node.array_size = self.visit(exprs[0])
            if len(exprs) > 1:
                type_node.array_size2 = self.visit(exprs[1])
        name_sym = ctx.IDENTIFIER().symbol
        return AttributeDeclaration(
            line=type_node.line, column=type_node.column,
            type_node=type_node, name=name_sym.text,
        )

    def _build_method(self, ctx: JSSParser.ClassMemberContext) -> MethodDeclaration:
        return_type = self.visitReturnType(ctx.returnType())
        name_sym = ctx.IDENTIFIER().symbol
        params = self._build_params(ctx.parameters())
        body = self.visitBlock(ctx.block())
        return MethodDeclaration(
            line=return_type.line, column=return_type.column,
            return_type=return_type, name=name_sym.text, params=params, body=body,
        )

    def visitConstructorDecl(
        self, ctx: JSSParser.ConstructorDeclContext
    ) -> ConstructorDeclaration:
        class_name_sym = ctx.IDENTIFIER().symbol
        params = self._build_params(ctx.parameters())
        body = self.visitBlock(ctx.block())
        return ConstructorDeclaration(
            line=class_name_sym.line, column=class_name_sym.column + 1,
            class_name=class_name_sym.text, params=params, body=body,
        )

    # ── Blocos e comandos ─────────────────────────────────────────────────────

    def visitBlock(self, ctx: JSSParser.BlockContext) -> Block:
        tok = ctx.start
        stmts: list[Node] = [self.visit(s) for s in ctx.statement()]
        return Block(line=tok.line, column=tok.column + 1, statements=stmts)

    def visitStatement(self, ctx: JSSParser.StatementContext) -> Node:
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx: JSSParser.IfStmtContext) -> IfStatement:
        tok = ctx.start
        condition = self.visit(ctx.expr())
        then_branch = self.visitBlock(ctx.block(0))
        else_branch: Node | None = None
        if ctx.block(1):
            else_branch = self.visitBlock(ctx.block(1))
        elif ctx.ifStmt():
            else_branch = self.visitIfStmt(ctx.ifStmt())
        return IfStatement(
            line=tok.line, column=tok.column + 1,
            condition=condition, then_branch=then_branch, else_branch=else_branch,
        )

    def visitWhileStmt(self, ctx: JSSParser.WhileStmtContext) -> WhileStatement:
        tok = ctx.start
        condition = self.visit(ctx.expr())
        body = self.visitBlock(ctx.block())
        return WhileStatement(line=tok.line, column=tok.column + 1,
                              condition=condition, body=body)

    def visitForStmt(self, ctx: JSSParser.ForStmtContext) -> ForStatement:
        tok = ctx.start
        init = self.visitForInit(ctx.forInit())
        exprs = ctx.expr()
        condition = self.visit(exprs[0]) if exprs else None
        increment = self.visit(exprs[1]) if len(exprs) > 1 else None
        body = self.visitBlock(ctx.block())
        return ForStatement(
            line=tok.line, column=tok.column + 1,
            initializer=init, condition=condition, increment=increment, body=body,
        )

    def visitForInit(self, ctx: JSSParser.ForInitContext) -> Node | None:
        if ctx.varDecl():
            return self.visitVarDecl(ctx.varDecl())
        if ctx.constDecl():
            return self.visitConstDecl(ctx.constDecl())
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitReturnStmt(self, ctx: JSSParser.ReturnStmtContext) -> ReturnStatement:
        tok = ctx.start
        value = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStatement(line=tok.line, column=tok.column + 1, value=value)

    def visitBreakStmt(self, ctx: JSSParser.BreakStmtContext) -> BreakStatement:
        tok = ctx.start
        return BreakStatement(line=tok.line, column=tok.column + 1)

    def visitExprStmt(self, ctx: JSSParser.ExprStmtContext) -> ExpressionStatement:
        expr = self.visit(ctx.expr())
        return ExpressionStatement(line=expr.line, column=expr.column, expression=expr)

    # ── Expressões ────────────────────────────────────────────────────────────

    def visitExpr(self, ctx: JSSParser.ExprContext) -> Node:
        return self.visitAssignment(ctx.assignment())

    def visitAssignment(self, ctx: JSSParser.AssignmentContext) -> Node:
        left = self.visitLogicalOr(ctx.logicalOr())
        if ctx.assignOp():
            op_ctx = ctx.assignOp()
            op_term = op_ctx.getChild(0)
            op_tok = _make_jss_token(op_term, _ANTLR_TO_JSS[op_term.symbol.type])
            right = self.visitAssignment(ctx.assignment())
            return Assignment(line=left.line, column=left.column,
                              target=left, operator=op_tok, value=right)
        return left

    def visitLogicalOr(self, ctx: JSSParser.LogicalOrContext) -> Node:
        return self._left_binary(ctx, self.visitLogicalAnd)

    def visitLogicalAnd(self, ctx: JSSParser.LogicalAndContext) -> Node:
        return self._left_binary(ctx, self.visitEqualityRel)

    def visitEqualityRel(self, ctx: JSSParser.EqualityRelContext) -> Node:
        return self._left_binary(ctx, self.visitAddition)

    def visitAddition(self, ctx: JSSParser.AdditionContext) -> Node:
        return self._left_binary(ctx, self.visitMultiplication)

    def visitMultiplication(self, ctx: JSSParser.MultiplicationContext) -> Node:
        return self._left_binary(ctx, self.visitExponentiation)

    def _left_binary(self, ctx, visit_child) -> Node:
        """Constrói uma árvore binária associativa à esquerda a partir dos filhos do contexto."""
        children = [ctx.getChild(i) for i in range(ctx.getChildCount())]
        result = visit_child(children[0])
        i = 1
        while i < len(children):
            op_term = children[i]
            right_ctx = children[i + 1]
            op_tok = _make_jss_token(op_term, _ANTLR_TO_JSS[op_term.symbol.type])
            right = visit_child(right_ctx)
            result = BinaryOperation(
                line=result.line, column=result.column,
                left=result, operator=op_tok, right=right,
            )
            i += 2
        return result

    def visitExponentiation(self, ctx: JSSParser.ExponentiationContext) -> Node:
        left = self.visitUnary(ctx.unary())
        if ctx.exponentiation():
            op_sym = ctx.POWER().symbol
            op_tok = Token(type=TokenType.POWER, lexeme="**",
                           line=op_sym.line, column=op_sym.column + 1)
            right = self.visitExponentiation(ctx.exponentiation())
            return BinaryOperation(line=left.line, column=left.column,
                                   left=left, operator=op_tok, right=right)
        return left

    def visitUnary(self, ctx: JSSParser.UnaryContext) -> Node:
        if ctx.postfix():
            return self.visitPostfix(ctx.postfix())
        op_term = ctx.getChild(0)
        op_tok = _make_jss_token(op_term, _ANTLR_TO_JSS[op_term.symbol.type])
        operand = self.visitUnary(ctx.unary())
        return UnaryOperation(line=op_tok.line, column=op_tok.column,
                              operator=op_tok, operand=operand)

    def visitPostfix(self, ctx: JSSParser.PostfixContext) -> Node:
        primary_ctx = ctx.primary()
        node = self.visit(primary_ctx)
        ops = ctx.postfixOp()

        for i, op in enumerate(ops):
            if op.LEFT_PAREN():  # chamada
                args = self._build_args(op.argumentList())
                native = i == 0 and self._is_native_callee(primary_ctx)
                if (
                    not native
                    and isinstance(node, Identifier)
                    and node.name in self._class_names
                ):
                    raise RawSyntaxErrorJSS(
                        f"Erro sintatico na linha {node.line}: criação de objeto deve usar 'new'.",
                        node.line, node.column,
                    )
                node = Call(line=node.line, column=node.column,
                            callee=node, arguments=args, native=native)
            elif op.LEFT_BRACKET():  # índice
                index = self.visit(op.expr())
                node = IndexAccess(line=node.line, column=node.column,
                                   collection=node, index=index)
            elif op.PLUS_PLUS() or op.MINUS_MINUS():  # pós-incremento / pós-decremento
                op_term = op.getChild(0)
                op_tok = _make_jss_token(op_term, _ANTLR_TO_JSS[op_term.symbol.type])
                node = UnaryOperation(line=node.line, column=node.column,
                                      operator=op_tok, operand=node, postfix=True)
            else:  # DOT IDENTIFIER — acesso a atributo
                attr_sym = op.IDENTIFIER().symbol
                node = AttributeAccess(line=node.line, column=node.column,
                                       object_expr=node, attribute=attr_sym.text)
        return node

    def _is_native_callee(self, primary_ctx) -> bool:
        return isinstance(
            primary_ctx,
            (JSSParser.PrimaryConsoleLogContext, JSSParser.PrimaryInputContext),
        )

    def _build_args(self, ctx: JSSParser.ArgumentListContext | None) -> list[Node]:
        if ctx is None:
            return []
        return [self.visit(e) for e in ctx.expr()]

    # ── Primários ─────────────────────────────────────────────────────────────

    def visitLitInt(self, ctx: JSSParser.LitIntContext) -> Literal:
        tok = ctx.INTEGER_LITERAL().symbol
        return Literal(line=tok.line, column=tok.column + 1,
                       value=int(tok.text), literal_type="int")

    def visitLitReal(self, ctx: JSSParser.LitRealContext) -> Literal:
        tok = ctx.REAL_LITERAL().symbol
        return Literal(line=tok.line, column=tok.column + 1,
                       value=float(tok.text), literal_type="real")

    def visitLitStr(self, ctx: JSSParser.LitStrContext) -> Literal:
        tok = ctx.STRING_LITERAL().symbol
        value = self._unescape(tok.text[1:-1])  # remove aspas externas
        return Literal(line=tok.line, column=tok.column + 1,
                       value=value, literal_type="str")

    def visitLitTrue(self, ctx: JSSParser.LitTrueContext) -> Literal:
        tok = ctx.TRUE().symbol
        return Literal(line=tok.line, column=tok.column + 1, value=True, literal_type="bool")

    def visitLitFalse(self, ctx: JSSParser.LitFalseContext) -> Literal:
        tok = ctx.FALSE().symbol
        return Literal(line=tok.line, column=tok.column + 1, value=False, literal_type="bool")

    def visitLitNull(self, ctx: JSSParser.LitNullContext) -> Literal:
        tok = ctx.NULL().symbol
        return Literal(line=tok.line, column=tok.column + 1, value=None, literal_type="null")

    def visitPrimaryThis(self, ctx: JSSParser.PrimaryThisContext) -> This:
        tok = ctx.THIS().symbol
        return This(line=tok.line, column=tok.column + 1)

    def visitPrimaryId(self, ctx: JSSParser.PrimaryIdContext) -> Identifier:
        tok = ctx.IDENTIFIER().symbol
        return Identifier(line=tok.line, column=tok.column + 1, name=tok.text)

    def visitPrimaryInput(self, ctx: JSSParser.PrimaryInputContext) -> Identifier:
        tok = ctx.INPUT().symbol
        return Identifier(line=tok.line, column=tok.column + 1, name="input")

    def visitPrimaryConsoleLog(self, ctx: JSSParser.PrimaryConsoleLogContext) -> Identifier:
        tok = ctx.CONSOLE_LOG().symbol
        return Identifier(line=tok.line, column=tok.column + 1, name="console.log")

    def visitPrimaryNew(self, ctx: JSSParser.PrimaryNewContext) -> NewObject:
        new_sym = ctx.NEW().symbol
        class_name = ctx.IDENTIFIER().getText()
        args = self._build_args(ctx.argumentList())
        return NewObject(line=new_sym.line, column=new_sym.column + 1,
                         class_name=class_name, arguments=args)

    def visitPrimaryParen(self, ctx: JSSParser.PrimaryParenContext) -> Node:
        return self.visit(ctx.expr())

    def visitPrimaryCast(self, ctx: JSSParser.PrimaryCastContext) -> Call:
        type_sym = ctx.getChild(0).symbol  # token TYPE_INT / TYPE_REAL / ...
        name = _TYPE_NAME[type_sym.type]
        callee = Identifier(line=type_sym.line, column=type_sym.column + 1, name=name)
        args = self._build_args(ctx.argumentList())
        return Call(line=type_sym.line, column=type_sym.column + 1,
                    callee=callee, arguments=args, native=True)

    # ── Auxiliares ────────────────────────────────────────────────────────────

    def _unescape(self, raw: str) -> str:
        result: list[str] = []
        i = 0
        while i < len(raw):
            if raw[i] == "\\" and i + 1 < len(raw):
                esc = raw[i + 1]
                result.append({"n": "\n", "t": "\t", "r": "\r",
                                '"': '"', "\\": "\\"}.get(esc, esc))
                i += 2
            else:
                result.append(raw[i])
                i += 1
        return "".join(result)
