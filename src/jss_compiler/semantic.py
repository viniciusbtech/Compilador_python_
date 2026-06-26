"""Analisador semantico da linguagem JSS."""

from __future__ import annotations

from dataclasses import dataclass, field

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
    This,
    TypeNode,
    UnaryOperation,
    VarDeclaration,
    WhileStatement,
)
from .errors import SemanticError
from .lexer import Lexer
from .tokens import TokenType


PRIMITIVE_TYPES = {"int", "real", "str", "bool"}
CAST_FUNCTIONS = PRIMITIVE_TYPES
NUMERIC_TYPES = {"int", "real"}
RESERVED_WORDS = set(Lexer.KEYWORDS)


@dataclass(slots=True)
class TypeInfo:
    name: str
    is_array: bool = False
    ndim: int = 1

    def display(self) -> str:
        if not self.is_array:
            return self.name
        return f"{self.name}{'[]' * self.ndim}"


@dataclass(slots=True)
class SemanticSymbol:
    name: str
    category: str
    type_info: TypeInfo
    constant: bool
    node: Node
    params: list[TypeInfo] = field(default_factory=list)


@dataclass(slots=True)
class ClassInfo:
    declaration: ClassDeclaration
    attributes: dict[str, SemanticSymbol] = field(default_factory=dict)
    methods: dict[str, SemanticSymbol] = field(default_factory=dict)
    constructor_params: list[TypeInfo] | None = None


class Scope:
    def __init__(self, name: str, parent: Scope | None = None) -> None:
        self.name = name
        self.parent = parent
        self.symbols: dict[str, SemanticSymbol] = {}

    def define(self, symbol: SemanticSymbol) -> None:
        if symbol.name in self.symbols:
            raise SemanticError(
                f"identificador '{symbol.name}' ja declarado neste escopo",
                symbol.node.line,
                symbol.node.column,
            )
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> SemanticSymbol | None:
        scope: Scope | None = self
        while scope is not None:
            symbol = scope.symbols.get(name)
            if symbol is not None:
                return symbol
            scope = scope.parent
        return None


class SemanticAnalyzer:
    def __init__(self) -> None:
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope
        self.classes: dict[str, ClassInfo] = {}
        self.current_function: FunctionDeclaration | MethodDeclaration | None = None
        self.current_class: ClassInfo | None = None
        self.loop_depth = 0

    def analyze(self, program: Program) -> None:
        self._declare_global_symbols(program)
        for declaration in program.declarations:
            self._check_declaration(declaration)

    def _declare_global_symbols(self, program: Program) -> None:
        for declaration in program.declarations:
            if isinstance(declaration, ClassDeclaration):
                self._ensure_not_reserved(declaration.name, declaration)
                symbol = SemanticSymbol(
                    declaration.name,
                    "classe",
                    TypeInfo(declaration.name),
                    True,
                    declaration,
                )
                self.global_scope.define(symbol)
                self.classes[declaration.name] = ClassInfo(declaration)

        for declaration in program.declarations:
            if isinstance(declaration, FunctionDeclaration):
                self._ensure_not_reserved(declaration.name, declaration)
                if declaration.name == "main" and declaration.params:
                    raise SemanticError(
                        "funcao main nao deve possuir parametros",
                        declaration.line,
                        declaration.column,
                    )
                params = [self._type_from_node(param.type_node) for param in declaration.params]
                symbol = SemanticSymbol(
                    declaration.name,
                    "funcao",
                    self._type_from_node(declaration.return_type),
                    True,
                    declaration,
                    params,
                )
                self.global_scope.define(symbol)
            elif isinstance(declaration, VarDeclaration):
                self._declare_variables(declaration, self.global_scope, check_values=False)

    def _check_declaration(self, declaration: Node) -> None:
        if isinstance(declaration, VarDeclaration):
            self._check_variable_values(declaration)
        elif isinstance(declaration, FunctionDeclaration):
            self._check_function(declaration)
        elif isinstance(declaration, ClassDeclaration):
            self._check_class(declaration)
        else:
            self._check_statement(declaration)

    def _check_function(self, declaration: FunctionDeclaration | MethodDeclaration) -> None:
        previous_function = self.current_function
        previous_scope = self.current_scope
        self.current_function = declaration
        function_scope = Scope(f"funcao:{declaration.name}", self.global_scope)
        self.current_scope = function_scope
        for param in declaration.params:
            self._ensure_not_reserved(param.name, param)
            function_scope.define(
                SemanticSymbol(
                    param.name,
                    "parametro",
                    self._type_from_node(param.type_node),
                    False,
                    param,
                )
            )
        self._check_block(declaration.body, create_scope=False)
        return_type = self._type_from_node(declaration.return_type)
        if return_type.name != "void" and not self._block_always_returns(declaration.body):
            raise SemanticError(
                f"funcao '{declaration.name}' nao garante retorno em todos os caminhos",
                declaration.line,
                declaration.column,
            )
        self.current_scope = previous_scope
        self.current_function = previous_function

    def _check_class(self, declaration: ClassDeclaration) -> None:
        class_info = self.classes[declaration.name]
        saw_non_attribute = False

        for member in declaration.members:
            if isinstance(member, AttributeDeclaration):
                if saw_non_attribute:
                    raise SemanticError(
                        "atributos devem ser declarados antes de metodos",
                        member.line,
                        member.column,
                    )
                self._ensure_not_reserved(member.name, member)
                self._ensure_valid_type(member.type_node)
                if member.name in class_info.attributes:
                    raise SemanticError(
                        f"atributo '{member.name}' ja declarado na classe",
                        member.line,
                        member.column,
                    )
                class_info.attributes[member.name] = SemanticSymbol(
                    member.name,
                    "atributo",
                    self._type_from_node(member.type_node),
                    False,
                    member,
                )
                continue

            saw_non_attribute = True
            if isinstance(member, MethodDeclaration):
                self._ensure_not_reserved(member.name, member)
                if member.name in class_info.methods:
                    raise SemanticError(
                        f"metodo '{member.name}' ja declarado na classe",
                        member.line,
                        member.column,
                    )
                class_info.methods[member.name] = SemanticSymbol(
                    member.name,
                    "metodo",
                    self._type_from_node(member.return_type),
                    True,
                    member,
                    [self._type_from_node(param.type_node) for param in member.params],
                )
            elif isinstance(member, ConstructorDeclaration):
                if member.class_name != declaration.name:
                    raise SemanticError(
                        "construtor deve usar o mesmo nome da classe",
                        member.line,
                        member.column,
                    )
                if class_info.constructor_params is not None:
                    raise SemanticError(
                        "classe deve possuir apenas um construtor",
                        member.line,
                        member.column,
                    )
                class_info.constructor_params = [
                    self._type_from_node(param.type_node) for param in member.params
                ]

        if not class_info.attributes:
            raise SemanticError(
                "classe deve possuir ao menos uma variavel",
                declaration.line,
                declaration.column,
            )
        if class_info.constructor_params is None:
            raise SemanticError(
                "classe deve possuir ao menos um construtor",
                declaration.line,
                declaration.column,
            )

        previous_class = self.current_class
        self.current_class = class_info
        for member in declaration.members:
            if isinstance(member, MethodDeclaration):
                self._check_function(member)
            elif isinstance(member, ConstructorDeclaration):
                self._check_constructor(member)
        self.current_class = previous_class

    def _check_constructor(self, declaration: ConstructorDeclaration) -> None:
        previous_scope = self.current_scope
        constructor_scope = Scope(f"constructor:{declaration.class_name}", self.global_scope)
        self.current_scope = constructor_scope
        for param in declaration.params:
            self._ensure_not_reserved(param.name, param)
            constructor_scope.define(
                SemanticSymbol(
                    param.name,
                    "parametro",
                    self._type_from_node(param.type_node),
                    False,
                    param,
                )
            )
        self._check_block(declaration.body, create_scope=False)
        self.current_scope = previous_scope

    def _check_block(self, block: Block, create_scope: bool = True) -> None:
        previous_scope = self.current_scope
        if create_scope:
            self.current_scope = Scope("bloco", previous_scope)
        block.scope = self.current_scope
        for statement in block.statements:
            self._check_statement(statement)
        self.current_scope = previous_scope

    def _check_statement(self, statement: Node) -> None:
        if isinstance(statement, VarDeclaration):
            self._declare_variables(statement, self.current_scope, check_values=True)
        elif isinstance(statement, Block):
            self._check_block(statement)
        elif isinstance(statement, ExpressionStatement):
            self._expression_type(statement.expression)
        elif isinstance(statement, IfStatement):
            self._expect_bool(statement.condition)
            self._check_block(statement.then_branch)
            if isinstance(statement.else_branch, Block):
                self._check_block(statement.else_branch)
            elif isinstance(statement.else_branch, IfStatement):
                self._check_statement(statement.else_branch)
        elif isinstance(statement, WhileStatement):
            self._expect_bool(statement.condition)
            self.loop_depth += 1
            self._check_block(statement.body)
            self.loop_depth -= 1
        elif isinstance(statement, ForStatement):
            self.current_scope = Scope("for", self.current_scope)
            if statement.initializer is not None:
                if isinstance(statement.initializer, VarDeclaration):
                    self._declare_variables(statement.initializer, self.current_scope, check_values=True)
                else:
                    self._expression_type(statement.initializer)
            if statement.condition is not None:
                self._expect_bool(statement.condition)
            if statement.increment is not None:
                self._expression_type(statement.increment)
            self.loop_depth += 1
            self._check_block(statement.body)
            self.loop_depth -= 1
            self.current_scope = self.current_scope.parent or self.global_scope
        elif isinstance(statement, ReturnStatement):
            self._check_return(statement)
        elif isinstance(statement, BreakStatement):
            if self.loop_depth == 0:
                raise SemanticError("break so pode ser usado dentro de laco", statement.line, statement.column)

    def _declare_variables(self, declaration: VarDeclaration, scope: Scope, check_values: bool) -> None:
        self._ensure_valid_type(declaration.type_node)
        base_type = self._type_from_node(declaration.type_node)
        if check_values and declaration.type_node.array_size2 is not None:
            size2_type = self._expression_type(declaration.type_node.array_size2)
            if size2_type.name != "int" or size2_type.is_array:
                raise SemanticError(
                    "tamanho de matriz deve ser int",
                    declaration.type_node.array_size2.line,
                    declaration.type_node.array_size2.column,
                )
        for declarator in declaration.declarators:
            self._ensure_not_reserved(declarator.name, declarator)
            is_array = declaration.type_node.is_array or declarator.array_size is not None
            ndim = 2 if declaration.type_node.array_size2 is not None else 1
            type_info = TypeInfo(base_type.name, is_array, ndim)
            scope.define(
                SemanticSymbol(
                    declarator.name,
                    "constante" if declaration.constant else "variavel",
                    type_info,
                    declaration.constant,
                    declarator,
                )
            )
            if check_values:
                self._check_declarator_value(declarator, type_info)

    def _check_variable_values(self, declaration: VarDeclaration) -> None:
        for declarator in declaration.declarators:
            symbol = self.current_scope.resolve(declarator.name)
            if symbol is not None:
                self._check_declarator_value(declarator, symbol.type_info)

    def _check_declarator_value(self, declarator: Declarator, type_info: TypeInfo) -> None:
        if declarator.array_size is not None:
            size_type = self._expression_type(declarator.array_size)
            if size_type.name != "int" or size_type.is_array:
                raise SemanticError("tamanho de vetor deve ser int", declarator.array_size.line, declarator.array_size.column)

        if declarator.array_values:
            if not type_info.is_array:
                raise SemanticError(
                    "lista de valores so pode inicializar vetores",
                    declarator.line,
                    declarator.column,
                )
            for value in declarator.array_values:
                value_type = self._expression_type(value)
                self._require_assignable(TypeInfo(type_info.name), value_type, value)
            return

        if declarator.initializer is not None:
            value_type = self._expression_type(declarator.initializer)
            self._require_assignable(type_info, value_type, declarator.initializer)

    def _check_return(self, statement: ReturnStatement) -> None:
        if self.current_function is None:
            raise SemanticError("return so pode ser usado dentro de funcao ou metodo", statement.line, statement.column)
        expected = self._type_from_node(self.current_function.return_type)
        if expected.name == "void":
            if statement.value is not None:
                raise SemanticError("funcao void nao deve retornar valor", statement.line, statement.column)
            return
        if statement.value is None:
            raise SemanticError("return deve possuir valor", statement.line, statement.column)
        actual = self._expression_type(statement.value)
        self._require_assignable(expected, actual, statement.value)

    def _expression_type(self, expression: Node) -> TypeInfo:
        if isinstance(expression, Literal):
            return TypeInfo(expression.literal_type)
        if isinstance(expression, Identifier):
            symbol = self.current_scope.resolve(expression.name)
            if symbol is None:
                raise SemanticError(
                    f"identificador '{expression.name}' nao declarado",
                    expression.line,
                    expression.column,
                )
            return symbol.type_info
        if isinstance(expression, This):
            if self.current_class is None:
                raise SemanticError("'this' so pode ser usado dentro de classe", expression.line, expression.column)
            return TypeInfo(self.current_class.declaration.name)
        if isinstance(expression, NewObject):
            class_info = self.classes.get(expression.class_name)
            if class_info is None:
                raise SemanticError(
                    f"classe '{expression.class_name}' nao declarada",
                    expression.line,
                    expression.column,
                )
            params = class_info.constructor_params or []
            self._check_arguments(params, expression.arguments, expression)
            return TypeInfo(expression.class_name)
        if isinstance(expression, AttributeAccess):
            return self._attribute_type(expression)
        if isinstance(expression, IndexAccess):
            collection_type = self._expression_type(expression.collection)
            index_type = self._expression_type(expression.index)
            if index_type.name != "int" or index_type.is_array:
                raise SemanticError("indice de vetor deve ser int", expression.index.line, expression.index.column)
            if not collection_type.is_array:
                raise SemanticError("acesso por indice requer vetor", expression.line, expression.column)
            if collection_type.ndim == 2:
                return TypeInfo(collection_type.name, is_array=True, ndim=1)
            return TypeInfo(collection_type.name)
        if isinstance(expression, Call):
            return self._call_type(expression)
        if isinstance(expression, UnaryOperation):
            return self._unary_type(expression)
        if isinstance(expression, BinaryOperation):
            return self._binary_type(expression)
        if isinstance(expression, Assignment):
            return self._assignment_type(expression)
        raise SemanticError("expressao semantica nao suportada", expression.line, expression.column)

    def _attribute_type(self, expression: AttributeAccess) -> TypeInfo:
        object_type = self._expression_type(expression.object_expr)
        class_info = self.classes.get(object_type.name)
        if class_info is None or object_type.is_array:
            raise SemanticError("acesso a atributo requer objeto", expression.line, expression.column)
        attribute = class_info.attributes.get(expression.attribute)
        if attribute is None:
            method = class_info.methods.get(expression.attribute)
            if method is not None:
                return method.type_info
            raise SemanticError(
                f"membro '{expression.attribute}' nao declarado na classe '{object_type.name}'",
                expression.line,
                expression.column,
            )
        return attribute.type_info

    def _call_type(self, expression: Call) -> TypeInfo:
        if expression.native:
            return self._native_call_type(expression)

        if isinstance(expression.callee, Identifier):
            symbol = self.current_scope.resolve(expression.callee.name)
            if symbol is None or symbol.category != "funcao":
                raise SemanticError(
                    f"funcao '{expression.callee.name}' nao declarada",
                    expression.callee.line,
                    expression.callee.column,
                )
            self._check_arguments(symbol.params, expression.arguments, expression)
            return symbol.type_info

        if isinstance(expression.callee, AttributeAccess):
            object_type = self._expression_type(expression.callee.object_expr)
            class_info = self.classes.get(object_type.name)
            method = class_info.methods.get(expression.callee.attribute) if class_info else None
            if method is None:
                raise SemanticError(
                    f"metodo '{expression.callee.attribute}' nao declarado",
                    expression.callee.line,
                    expression.callee.column,
                )
            self._check_arguments(method.params, expression.arguments, expression)
            return method.type_info

        raise SemanticError("chamada requer funcao ou metodo", expression.line, expression.column)

    _CAST_ALLOWED_SOURCES: dict[str, frozenset[str]] = {
        "int":  frozenset({"int", "real", "bool"}),
        "real": frozenset({"int", "real", "bool"}),
        "bool": frozenset({"bool", "int", "real"}),
        "str":  frozenset({"str", "int", "real", "bool"}),
    }

    def _native_call_type(self, expression: Call) -> TypeInfo:
        if isinstance(expression.callee, Identifier) and expression.callee.name in CAST_FUNCTIONS:
            if len(expression.arguments) != 1:
                raise SemanticError(
                    f"cast {expression.callee.name}() deve receber exatamente um argumento",
                    expression.line,
                    expression.column,
                )
            source_type = self._expression_type(expression.arguments[0])
            if source_type.is_array or source_type.name == "void":
                raise SemanticError("cast nativo nao aceita vetor ou void", expression.line, expression.column)
            target_name = expression.callee.name
            allowed = self._CAST_ALLOWED_SOURCES[target_name]
            if source_type.name not in allowed:
                raise SemanticError(
                    f"cast {target_name}() nao aceita origem {source_type.name}",
                    expression.line,
                    expression.column,
                )
            return TypeInfo(target_name)

        if isinstance(expression.callee, Identifier) and expression.callee.name == "input":
            if not expression.arguments:
                raise SemanticError("input requer ao menos uma variavel", expression.line, expression.column)
            for argument in expression.arguments:
                argument_type = self._ensure_assignable_target(argument)
                if argument_type.is_array or argument_type.name not in {"int", "real", "str"}:
                    raise SemanticError(
                        "input aceita apenas variaveis int, real ou str",
                        argument.line,
                        argument.column,
                    )
            return TypeInfo("void")

        if isinstance(expression.callee, Identifier) and expression.callee.name == "console.log":
            for argument in expression.arguments:
                self._expression_type(argument)
            return TypeInfo("void")

        if (
            isinstance(expression.callee, AttributeAccess)
            and isinstance(expression.callee.object_expr, Identifier)
            and expression.callee.object_expr.name == "console"
            and expression.callee.attribute == "log"
        ):
            for argument in expression.arguments:
                self._expression_type(argument)
            return TypeInfo("void")

        raise SemanticError("chamada nativa invalida", expression.line, expression.column)

    def _unary_type(self, expression: UnaryOperation) -> TypeInfo:
        operand_type = self._expression_type(expression.operand)
        operator = expression.operator.type
        if operator is TokenType.BANG:
            if operand_type.name != "bool" or operand_type.is_array:
                raise SemanticError("operador ! requer bool", expression.line, expression.column)
            return TypeInfo("bool")
        if operator in {TokenType.PLUS, TokenType.MINUS}:
            self._require_numeric(operand_type, expression.operand)
            return operand_type
        if operator in {TokenType.PLUS_PLUS, TokenType.MINUS_MINUS}:
            self._ensure_assignable_target(expression.operand)
            self._require_numeric(operand_type, expression.operand)
            return operand_type
        raise SemanticError("operador unario invalido", expression.line, expression.column)

    def _binary_type(self, expression: BinaryOperation) -> TypeInfo:
        left = self._expression_type(expression.left)
        right = self._expression_type(expression.right)
        operator = expression.operator.type

        if operator is TokenType.PLUS:
            if left.is_array or right.is_array:
                raise SemanticError("operador + nao aceita vetores", expression.line, expression.column)
            if left.name == "str" or right.name == "str":
                if left.name != "str" or right.name != "str":
                    raise SemanticError(
                        f"concatenacao requer operandos str, recebido {left.name} e {right.name}",
                        expression.line, expression.column,
                    )
                return TypeInfo("str")
            self._require_numeric(left, expression.left)
            self._require_numeric(right, expression.right)
            return self._numeric_result_type(left, right)

        if operator in {TokenType.MINUS, TokenType.STAR, TokenType.SLASH}:
            self._require_numeric(left, expression.left)
            self._require_numeric(right, expression.right)
            return self._numeric_result_type(left, right)

        if operator in {TokenType.PERCENT, TokenType.POWER}:
            self._require_int(left, expression.left)
            self._require_int(right, expression.right)
            return TypeInfo("int")

        if operator in {TokenType.AND_AND, TokenType.OR_OR}:
            if left.name != "bool" or right.name != "bool" or left.is_array or right.is_array:
                raise SemanticError("operadores logicos requerem bool", expression.line, expression.column)
            return TypeInfo("bool")

        if operator in {
            TokenType.EQUAL_EQUAL,
            TokenType.BANG_EQUAL,
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
        }:
            if not self._types_compatible_for_comparison(left, right):
                raise SemanticError("operandos incompativeis em comparacao", expression.line, expression.column)
            return TypeInfo("bool")

        raise SemanticError("operador binario invalido", expression.line, expression.column)

    def _assignment_type(self, expression: Assignment) -> TypeInfo:
        target_type = self._ensure_assignable_target(expression.target)
        value_type = self._expression_type(expression.value)
        operator = expression.operator.type

        if operator is TokenType.ASSIGN:
            self._require_assignable(target_type, value_type, expression.value)
            return target_type

        fake_operator = {
            TokenType.PLUS_ASSIGN: TokenType.PLUS,
            TokenType.MINUS_ASSIGN: TokenType.MINUS,
            TokenType.STAR_ASSIGN: TokenType.STAR,
            TokenType.SLASH_ASSIGN: TokenType.SLASH,
            TokenType.PERCENT_ASSIGN: TokenType.PERCENT,
            TokenType.POWER_ASSIGN: TokenType.POWER,
        }[operator]
        result = self._compound_result_type(target_type, value_type, fake_operator, expression)
        self._require_assignable(target_type, result, expression.value)
        return target_type

    def _compound_result_type(
        self,
        target_type: TypeInfo,
        value_type: TypeInfo,
        operator: TokenType,
        expression: Assignment,
    ) -> TypeInfo:
        if operator is TokenType.PLUS and (target_type.name == "str" or value_type.name == "str"):
            if target_type.is_array or value_type.is_array:
                raise SemanticError("atribuicao composta nao aceita vetores", expression.line, expression.column)
            if target_type.name != "str" or value_type.name != "str":
                raise SemanticError(
                    f"concatenacao requer operandos str, recebido {target_type.name} e {value_type.name}",
                    expression.line, expression.column,
                )
            return TypeInfo("str")

        if operator in {TokenType.PERCENT, TokenType.POWER}:
            self._require_int(target_type, expression.target)
            self._require_int(value_type, expression.value)
            return TypeInfo("int")

        self._require_numeric(target_type, expression.target)
        self._require_numeric(value_type, expression.value)
        return self._numeric_result_type(target_type, value_type)

    def _ensure_assignable_target(self, target: Node) -> TypeInfo:
        if isinstance(target, Identifier):
            symbol = self.current_scope.resolve(target.name)
            if symbol is None:
                raise SemanticError(f"identificador '{target.name}' nao declarado", target.line, target.column)
            if symbol.constant:
                raise SemanticError(f"constante '{target.name}' nao pode ser alterada", target.line, target.column)
            return symbol.type_info

        if isinstance(target, IndexAccess):
            if isinstance(target.collection, Identifier):
                symbol = self.current_scope.resolve(target.collection.name)
                if symbol is not None and symbol.constant:
                    raise SemanticError(
                        f"vetor constante '{target.collection.name}' nao pode ser alterado",
                        target.line,
                        target.column,
                    )
            collection_type = self._expression_type(target.collection)
            index_type = self._expression_type(target.index)
            if index_type.name != "int" or index_type.is_array:
                raise SemanticError("indice de vetor deve ser int", target.index.line, target.index.column)
            if not collection_type.is_array:
                raise SemanticError("atribuicao por indice requer vetor", target.line, target.column)
            if collection_type.ndim == 2:
                return TypeInfo(collection_type.name, is_array=True, ndim=1)
            return TypeInfo(collection_type.name)

        if isinstance(target, AttributeAccess):
            return self._attribute_type(target)

        raise SemanticError("lado esquerdo da atribuicao deve ser atribuivel", target.line, target.column)

    def _check_arguments(self, expected: list[TypeInfo], actual_nodes: list[Node], call: Node) -> None:
        if len(expected) != len(actual_nodes):
            raise SemanticError(
                f"quantidade de argumentos invalida: esperado {len(expected)}, recebido {len(actual_nodes)}",
                call.line,
                call.column,
            )
        for expected_type, actual_node in zip(expected, actual_nodes):
            actual_type = self._expression_type(actual_node)
            self._require_assignable(expected_type, actual_type, actual_node)

    def _expect_bool(self, expression: Node) -> None:
        expression_type = self._expression_type(expression)
        if expression_type.name != "bool" or expression_type.is_array:
            raise SemanticError("condicao deve ser bool", expression.line, expression.column)

    def _require_numeric(self, type_info: TypeInfo, node: Node) -> None:
        if type_info.name not in NUMERIC_TYPES or type_info.is_array:
            raise SemanticError("operacao aritmetica requer int ou real", node.line, node.column)

    def _require_int(self, type_info: TypeInfo, node: Node) -> None:
        if type_info.name != "int" or type_info.is_array:
            raise SemanticError("operacao requer int", node.line, node.column)

    @staticmethod
    def _numeric_result_type(left: TypeInfo, right: TypeInfo) -> TypeInfo:
        if left.name == "real" or right.name == "real":
            return TypeInfo("real")
        return TypeInfo("int")

    def _require_same_type(self, left: TypeInfo, right: TypeInfo, node: Node) -> None:
        if left.name != right.name or left.is_array != right.is_array:
            raise SemanticError(
                f"tipos misturados nao sao permitidos: {left.display()} e {right.display()}",
                node.line,
                node.column,
            )

    def _block_always_returns(self, block: Block) -> bool:
        for stmt in block.statements:
            if isinstance(stmt, ReturnStatement):
                return True
            if isinstance(stmt, Block) and self._block_always_returns(stmt):
                return True
            if isinstance(stmt, IfStatement) and stmt.else_branch is not None:
                then_ok = self._block_always_returns(stmt.then_branch)
                if isinstance(stmt.else_branch, Block):
                    else_ok = self._block_always_returns(stmt.else_branch)
                else:
                    else_ok = self._block_always_returns(Block(stmt.else_branch.line, stmt.else_branch.column, [stmt.else_branch]))
                if then_ok and else_ok:
                    return True
        return False

    def _require_assignable(self, target: TypeInfo, value: TypeInfo, value_node: Node) -> None:
        if target.is_array != value.is_array:
            raise SemanticError(
                f"tipo incompativel: esperado {target.display()}, recebido {value.display()}",
                value_node.line,
                value_node.column,
            )
        if target.name == value.name:
            return
        if value.name == "null" and target.name not in PRIMITIVE_TYPES:
            return
        if target.name == "real" and value.name == "int" and not target.is_array and not value.is_array:
            return
        raise SemanticError(
            f"tipo incompativel: esperado {target.display()}, recebido {value.display()}",
            value_node.line,
            value_node.column,
        )

    def _types_compatible_for_comparison(self, left: TypeInfo, right: TypeInfo) -> bool:
        if left.is_array or right.is_array:
            return left.is_array == right.is_array and left.name == right.name
        if left.name == right.name:
            return True
        return False

    def _type_from_node(self, type_node: TypeNode) -> TypeInfo:
        self._ensure_valid_type(type_node)
        ndim = 2 if type_node.array_size2 is not None else 1
        return TypeInfo(type_node.name, type_node.is_array, ndim)

    def _ensure_valid_type(self, type_node: TypeNode) -> None:
        if type_node.name == "void":
            return
        if type_node.name in PRIMITIVE_TYPES:
            return
        if type_node.name not in self.classes:
            raise SemanticError(f"tipo '{type_node.name}' nao declarado", type_node.line, type_node.column)

    def _ensure_not_reserved(self, name: str, node: Node) -> None:
        if name in RESERVED_WORDS:
            raise SemanticError(
                f"identificador '{name}' nao pode usar palavra reservada",
                node.line,
                node.column,
            )


def analyze_semantics(program: Program) -> "SemanticAnalyzer":
    analyzer = SemanticAnalyzer()
    analyzer.analyze(program)
    return analyzer
