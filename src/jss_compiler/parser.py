"""Analisador sintatico por descida recursiva da linguagem JSS."""

from __future__ import annotations

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


TYPE_TOKENS = {
    TokenType.TYPE_INT,
    TokenType.TYPE_REAL,
    TokenType.TYPE_STR,
    TokenType.TYPE_BOOL,
    TokenType.IDENTIFIER,
}

RETURN_TYPE_TOKENS = TYPE_TOKENS | {TokenType.VOID}

ASSIGNMENT_TOKENS = {
    TokenType.ASSIGN,
    TokenType.PLUS_ASSIGN,
    TokenType.MINUS_ASSIGN,
    TokenType.STAR_ASSIGN,
    TokenType.SLASH_ASSIGN,
    TokenType.PERCENT_ASSIGN,
    TokenType.POWER_ASSIGN,
}

SYNCHRONIZATION_TOKENS = {
    TokenType.SEMICOLON,
    TokenType.RIGHT_BRACE,
    TokenType.FUNCTION,
    TokenType.LET,
    TokenType.CONST,
    TokenType.IF,
    TokenType.WHILE,
    TokenType.FOR,
    TokenType.RETURN,
    TokenType.CLASS,
}


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.current = 0
        self.errors: list[SyntaxErrorJSS] = []
        self.symbols: list[Symbol] = []
        self.scope_stack = ["global"]
        self.class_names = self._collect_class_names()

    def parse(self) -> Program:
        """Valida os tokens e devolve a AST do programa JSS."""
        declarations: list[Node] = []

        while not self._is_at_end():
            try:
                declarations.append(self._declaration_global())
            except SyntaxErrorJSS as error:
                self.errors.append(error)
                self._synchronize()

        if self.errors:
            raise self.errors[0]

        first = declarations[0] if declarations else self._peek()
        return Program(
            line=first.line,
            column=first.column,
            declarations=declarations,
            symbols=self.symbols,
        )

    def _declaration_global(self) -> Node:
        if self._match(TokenType.LET):
            return self._variable_declaration(self._previous(), constant=False)
        if self._match(TokenType.CONST):
            return self._variable_declaration(self._previous(), constant=True)
        if self._match(TokenType.FUNCTION):
            return self._function_declaration(self._previous())
        if self._match(TokenType.CLASS):
            return self._class_declaration(self._previous())
        if self._looks_like_global_declaration_without_keyword():
            token = self._peek()
            raise RawSyntaxErrorJSS(
                (
                    "Erro sintático na linha "
                    f"{token.line}: declaração inválida. Esperado 'let', "
                    "'const', 'function' ou 'class', mas encontrado "
                    f"'{token.lexeme}'."
                ),
                token.line,
                token.column,
            )
        if self._looks_like_unknown_global_assignment():
            token = self._peek()
            raise RawSyntaxErrorJSS(
                (
                    "Erro sintático na linha "
                    f"{token.line}: declaração inválida. Esperado 'let', "
                    "'const', 'function' ou 'class', mas encontrado "
                    f"'{token.lexeme}'."
                ),
                token.line,
                token.column,
            )

        expression = self._expression()
        self._consume_semicolon("esperado ';' apos expressao")
        return ExpressionStatement(line=expression.line, column=expression.column, expression=expression)

    def _variable_declaration(self, start: Token, constant: bool) -> VarDeclaration:
        type_node = self._type(allow_void=False)
        if self._match(TokenType.LEFT_BRACKET):
            size = self._expression()
            self._consume(TokenType.RIGHT_BRACKET, "esperado ']' apos tamanho do vetor")
            type_node.is_array = True
            type_node.array_size = size

        declarators = [self._declarator(type_node.is_array)]
        while self._match(TokenType.COMMA):
            declarators.append(self._declarator(type_node.is_array))

        self._consume_semicolon("esperado ';' apos declaracao")

        declaration = VarDeclaration(
            line=start.line,
            column=start.column,
            type_node=type_node,
            declarators=declarators,
            constant=constant,
        )
        category = "constante" if constant else "variavel"
        for declarator in declarators:
            symbol_type = type_node.name + ("[]" if type_node.is_array or declarator.array_size else "")
            self._register_symbol(declarator.name, category, symbol_type, declarator)
        return declaration

    def _declarator(self, type_is_array: bool = False) -> Declarator:
        if self._check_reserved_word():
            token = self._peek()
            raise self._error(
                token,
                f"nome de variavel invalido: '{token.lexeme}' e palavra reservada",
            )
        name = self._consume(TokenType.IDENTIFIER, "esperado identificador").lexeme
        token = self._previous()
        array_size = None
        initializer = None
        values: list[Node] = []

        if self._match(TokenType.LEFT_BRACKET):
            if type_is_array:
                raise self._error(self._previous(), "matriz multidimensional nao permitida")
            array_size = self._expression()
            self._consume(TokenType.RIGHT_BRACKET, "esperado ']' apos indice/tamanho do vetor")

        if self._match(TokenType.ASSIGN):
            if self._match(TokenType.LEFT_BRACKET):
                if not self._check(TokenType.RIGHT_BRACKET):
                    values.append(self._expression())
                    while self._match(TokenType.COMMA):
                        values.append(self._expression())
                self._consume(TokenType.RIGHT_BRACKET, "esperado ']' apos lista de expressoes")
            else:
                initializer = self._expression()

        return Declarator(
            line=token.line,
            column=token.column,
            name=name,
            initializer=initializer,
            array_size=array_size,
            array_values=values,
        )

    def _function_declaration(self, start: Token) -> FunctionDeclaration:
        if self._check(TokenType.IDENTIFIER) and self._check_next(TokenType.LEFT_PAREN):
            raise self._error(start, "function sem tipo de retorno")
        return_type = self._type(allow_void=True)
        name = self._consume(TokenType.IDENTIFIER, "esperado nome da funcao").lexeme
        name_token = self._previous()
        params = self._parameters()

        self._register_symbol(name, "funcao", return_type.name, name_token)
        self.scope_stack.append(f"funcao:{name}")
        for param in params:
            self._register_symbol(param.name, "parametro", param.type_node.name, param)
        body = self._block()
        self.scope_stack.pop()

        return FunctionDeclaration(
            line=start.line,
            column=start.column,
            return_type=return_type,
            name=name,
            params=params,
            body=body,
        )

    def _class_declaration(self, start: Token) -> ClassDeclaration:
        name = self._consume(TokenType.IDENTIFIER, "esperado nome da classe").lexeme
        name_token = self._previous()
        self._register_symbol(name, "classe", name, name_token)
        self._consume(TokenType.LEFT_BRACE, "esperado '{' apos nome da classe")

        members: list[Node] = []
        self.scope_stack.append(f"classe:{name}")
        while not self._check(TokenType.RIGHT_BRACE) and not self._is_at_end():
            members.append(self._class_member(name))
        self.scope_stack.pop()

        self._consume(TokenType.RIGHT_BRACE, "esperado '}' apos corpo da classe")
        return ClassDeclaration(line=start.line, column=start.column, name=name, members=members)

    def _class_member(self, class_name: str) -> Node:
        if self._check(TokenType.IDENTIFIER) and self._check_next(TokenType.CONSTRUCTOR):
            return self._constructor_declaration()

        if not self._check_any(RETURN_TYPE_TOKENS):
            token = self._peek()
            raise self._error(token, "membro de classe invalido")

        start = self._peek()
        type_node = self._type(allow_void=True)
        name = self._consume(TokenType.IDENTIFIER, "esperado nome do membro").lexeme
        name_token = self._previous()

        if self._check(TokenType.LEFT_PAREN):
            params = self._parameters()
            self._register_symbol(name, "metodo", type_node.name, name_token)
            self.scope_stack.append(f"metodo:{name}")
            for param in params:
                self._register_symbol(param.name, "parametro", param.type_node.name, param)
            body = self._block()
            self.scope_stack.pop()
            return MethodDeclaration(
                line=start.line,
                column=start.column,
                return_type=type_node,
                name=name,
                params=params,
                body=body,
            )

        if type_node.name == "void":
            raise self._error(start, "void so pode ser usado como retorno")
        self._consume_semicolon("esperado ';' apos atributo")
        self._register_symbol(name, "atributo", type_node.name, name_token)
        return AttributeDeclaration(
            line=start.line,
            column=start.column,
            type_node=type_node,
            name=name,
        )

    def _constructor_declaration(self) -> ConstructorDeclaration:
        class_name = self._consume(TokenType.IDENTIFIER, "esperado nome da classe no construtor").lexeme
        start = self._previous()
        self._consume(TokenType.CONSTRUCTOR, "esperado palavra 'constructor'")
        params = self._parameters()

        self._register_symbol(class_name, "constructor", class_name, start)
        self.scope_stack.append(f"constructor:{class_name}")
        for param in params:
            self._register_symbol(param.name, "parametro", param.type_node.name, param)
        body = self._block()
        self.scope_stack.pop()

        return ConstructorDeclaration(
            line=start.line,
            column=start.column,
            class_name=class_name,
            params=params,
            body=body,
        )

    def _parameters(self) -> list[Parameter]:
        self._consume(TokenType.LEFT_PAREN, "esperado '('")
        params: list[Parameter] = []
        if not self._check(TokenType.RIGHT_PAREN):
            if self._check(TokenType.LEFT_BRACE):
                token = self._peek()
                raise self._error(token, "esperado tipo ) antes de {")
            params.append(self._parameter())
            while self._match(TokenType.COMMA):
                if self._check(TokenType.LEFT_BRACE):
                    token = self._peek()
                    raise self._error(token, "esperado tipo ) antes de {")
                params.append(self._parameter())
        self._consume(TokenType.RIGHT_PAREN, "esperado ')' apos parametros")
        return params

    def _parameter(self) -> Parameter:
        type_node = self._type(allow_void=False)
        name = self._consume(TokenType.IDENTIFIER, "esperado nome do parametro").lexeme
        token = self._previous()
        return Parameter(line=token.line, column=token.column, type_node=type_node, name=name)

    def _type(self, allow_void: bool) -> TypeNode:
        if allow_void and self._match(TokenType.VOID):
            token = self._previous()
            return TypeNode(line=token.line, column=token.column, name="void")

        if self._match(TokenType.TYPE_INT, TokenType.TYPE_REAL, TokenType.TYPE_STR, TokenType.TYPE_BOOL, TokenType.IDENTIFIER):
            token = self._previous()
            return TypeNode(line=token.line, column=token.column, name=token.lexeme)

        token = self._peek()
        expected = "tipo ou void" if allow_void else "tipo"
        raise self._error(token, f"esperado {expected}")

    def _block(self) -> Block:
        start = self._consume(TokenType.LEFT_BRACE, "esperado '{' para iniciar bloco")
        statements: list[Node] = []
        self.scope_stack.append("bloco")
        while not self._check(TokenType.RIGHT_BRACE) and not self._is_at_end():
            statements.append(self._statement())
        self.scope_stack.pop()
        self._consume(TokenType.RIGHT_BRACE, "esperado '}' apos bloco")
        return Block(line=start.line, column=start.column, statements=statements)

    def _statement(self) -> Node:
        if self._match(TokenType.LET):
            return self._variable_declaration(self._previous(), constant=False)
        if self._match(TokenType.CONST):
            return self._variable_declaration(self._previous(), constant=True)
        if self._match(TokenType.IF):
            return self._if_statement(self._previous())
        if self._match(TokenType.WHILE):
            return self._while_statement(self._previous())
        if self._match(TokenType.FOR):
            return self._for_statement(self._previous())
        if self._match(TokenType.RETURN):
            return self._return_statement(self._previous())
        if self._match(TokenType.BREAK):
            return self._break_statement(self._previous())
        if self._check(TokenType.LEFT_BRACE):
            return self._block()
        if self._match(TokenType.FUNCTION):
            token = self._previous()
            raise self._error(token, "funcao nao pode ser declarada dentro de bloco")
        if self._check_any({TokenType.TYPE_INT, TokenType.TYPE_REAL, TokenType.TYPE_STR, TokenType.TYPE_BOOL}):
            self._reject_invalid_type_statement()

        expression = self._expression()
        self._consume_semicolon("esperado ';' apos expressao")
        return ExpressionStatement(line=expression.line, column=expression.column, expression=expression)

    def _reject_invalid_type_statement(self) -> None:
        type_token = self._peek()
        next_token = self.tokens[self.current + 1] if self.current + 1 < len(self.tokens) else type_token
        if next_token.type is TokenType.LEFT_PAREN:
            return
        if next_token.type not in {TokenType.SEMICOLON, TokenType.IDENTIFIER}:
            raise RawSyntaxErrorJSS(
                (
                    "Erro de Sintaxe: Esperava ';' ou um identificador após "
                    f"'{type_token.lexeme}', mas encontrou '{next_token.lexeme}'."
                ),
                next_token.line,
                next_token.column,
            )

    def _if_statement(self, start: Token) -> IfStatement:
        self._consume(TokenType.LEFT_PAREN, "esperado '(' apos if")
        condition = self._expression()
        self._consume(TokenType.RIGHT_PAREN, "esperado ')' apos condicao do if")
        then_branch = self._block()
        else_branch: Block | IfStatement | None = None

        if self._match(TokenType.ELSE):
            if self._match(TokenType.IF):
                else_branch = self._if_statement(self._previous())
            else:
                else_branch = self._block()

        return IfStatement(
            line=start.line,
            column=start.column,
            condition=condition,
            then_branch=then_branch,
            else_branch=else_branch,
        )

    def _while_statement(self, start: Token) -> WhileStatement:
        self._consume(TokenType.LEFT_PAREN, "esperado '(' apos while")
        condition = self._expression()
        self._consume(TokenType.RIGHT_PAREN, "esperado ')' apos condicao do while")
        return WhileStatement(line=start.line, column=start.column, condition=condition, body=self._block())

    def _for_statement(self, start: Token) -> ForStatement:
        self._consume(TokenType.LEFT_PAREN, "esperado '(' apos for")
        if self._match(TokenType.LET):
            initializer = self._variable_declaration(self._previous(), constant=False)
        elif self._match(TokenType.CONST):
            initializer = self._variable_declaration(self._previous(), constant=True)
        else:
            initializer = None if self._check(TokenType.SEMICOLON) else self._expression()
            self._consume_semicolon("esperado ';' apos inicializacao do for")
        condition = None if self._check(TokenType.SEMICOLON) else self._expression()
        self._consume_semicolon("esperado ';' apos condicao do for")
        increment = None if self._check(TokenType.RIGHT_PAREN) else self._expression()
        self._consume(TokenType.RIGHT_PAREN, "esperado ')' apos incremento do for")
        return ForStatement(
            line=start.line,
            column=start.column,
            initializer=initializer,
            condition=condition,
            increment=increment,
            body=self._block(),
        )

    def _return_statement(self, start: Token) -> ReturnStatement:
        value = None if self._check(TokenType.SEMICOLON) else self._expression()
        self._consume_semicolon("esperado ';' apos return")
        return ReturnStatement(line=start.line, column=start.column, value=value)

    def _break_statement(self, start: Token) -> BreakStatement:
        self._consume_semicolon("esperado ';' apos break")
        return BreakStatement(line=start.line, column=start.column)

    def _expression(self) -> Node:
        return self._assignment()

    def _assignment(self) -> Node:
        expression = self._logical_or()
        if self._match(*ASSIGNMENT_TOKENS):
            operator = self._previous()
            value = self._assignment()
            return Assignment(
                line=operator.line,
                column=operator.column,
                target=expression,
                operator=operator,
                value=value,
            )
        return expression

    def _logical_or(self) -> Node:
        return self._left_associative(self._logical_and, TokenType.OR_OR)

    def _logical_and(self) -> Node:
        return self._left_associative(self._equality_relational, TokenType.AND_AND)

    def _equality_relational(self) -> Node:
        return self._left_associative(
            self._addition,
            TokenType.EQUAL_EQUAL,
            TokenType.BANG_EQUAL,
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
        )

    def _addition(self) -> Node:
        return self._left_associative(self._multiplication, TokenType.PLUS, TokenType.MINUS)

    def _multiplication(self) -> Node:
        return self._left_associative(
            self._exponentiation,
            TokenType.STAR,
            TokenType.SLASH,
            TokenType.PERCENT,
        )

    def _exponentiation(self) -> Node:
        expression = self._unary()
        if self._match(TokenType.POWER):
            operator = self._previous()
            right = self._exponentiation()
            return BinaryOperation(
                line=operator.line,
                column=operator.column,
                left=expression,
                operator=operator,
                right=right,
            )
        return expression

    def _unary(self) -> Node:
        if self._match(
            TokenType.BANG,
            TokenType.PLUS,
            TokenType.MINUS,
            TokenType.PLUS_PLUS,
            TokenType.MINUS_MINUS,
        ):
            operator = self._previous()
            return UnaryOperation(
                line=operator.line,
                column=operator.column,
                operator=operator,
                operand=self._unary(),
            )
        return self._postfix()

    def _postfix(self) -> Node:
        expression = self._primary()

        while True:
            if self._match(TokenType.LEFT_PAREN):
                if self._is_class_constructor_without_new(expression):
                    raise RawSyntaxErrorJSS(
                        (
                            "Erro sintatico na linha "
                            f"{expression.line}: criação de objeto deve usar 'new'."
                        ),
                        expression.line,
                        expression.column,
                    )
                arguments = self._arguments_after_open_paren()
                expression = Call(
                    line=expression.line,
                    column=expression.column,
                    callee=expression,
                    arguments=arguments,
                    native=self._is_native_callee(expression),
                )
                continue

            if self._match(TokenType.LEFT_BRACKET):
                index = self._expression()
                self._consume(TokenType.RIGHT_BRACKET, "esperado ']' apos indice")
                expression = IndexAccess(
                    line=expression.line,
                    column=expression.column,
                    collection=expression,
                    index=index,
                )
                continue

            if self._match(TokenType.DOT):
                attribute = self._consume(TokenType.IDENTIFIER, "esperado atributo apos '.'")
                expression = AttributeAccess(
                    line=expression.line,
                    column=expression.column,
                    object_expr=expression,
                    attribute=attribute.lexeme,
                )
                continue

            return expression

    def _primary(self) -> Node:
        if self._match(TokenType.INTEGER_LITERAL):
            token = self._previous()
            return Literal(token.line, token.column, int(token.lexeme), "int")
        if self._match(TokenType.REAL_LITERAL):
            token = self._previous()
            return Literal(token.line, token.column, float(token.lexeme), "real")
        if self._match(TokenType.STRING_LITERAL):
            token = self._previous()
            return Literal(token.line, token.column, token.lexeme, "str")
        if self._match(TokenType.TRUE, TokenType.FALSE):
            token = self._previous()
            return Literal(token.line, token.column, token.type is TokenType.TRUE, "bool")
        if self._match(TokenType.NULL):
            token = self._previous()
            return Literal(token.line, token.column, None, "null")
        if self._match(TokenType.IDENTIFIER, TokenType.INPUT, TokenType.CONSOLE_LOG):
            token = self._previous()
            return Identifier(token.line, token.column, token.lexeme)
        if self._match(TokenType.TYPE_INT, TokenType.TYPE_REAL, TokenType.TYPE_BOOL, TokenType.TYPE_STR):
            token = self._previous()
            if not self._check(TokenType.LEFT_PAREN):
                raise self._error(token, "tipo primitivo so pode aparecer em expressao como cast")
            return Identifier(token.line, token.column, token.lexeme)
        if self._match(TokenType.THIS):
            token = self._previous()
            return This(token.line, token.column)
        if self._match(TokenType.NEW):
            return self._new_object(self._previous())
        if self._match(TokenType.LEFT_PAREN):
            expression = self._expression()
            self._consume(TokenType.RIGHT_PAREN, "esperado ')' apos expressao")
            return expression

        token = self._peek()
        raise self._error(token, "esperado expressao")

    def _new_object(self, start: Token) -> NewObject:
        class_name = self._consume(TokenType.IDENTIFIER, "esperado nome da classe apos new").lexeme
        self._consume(TokenType.LEFT_PAREN, "esperado '(' apos nome da classe")
        return NewObject(
            line=start.line,
            column=start.column,
            class_name=class_name,
            arguments=self._arguments_after_open_paren(),
        )

    def _arguments_after_open_paren(self) -> list[Node]:
        arguments: list[Node] = []
        if not self._check(TokenType.RIGHT_PAREN):
            arguments.append(self._expression())
            while self._match(TokenType.COMMA):
                arguments.append(self._expression())
        self._consume(TokenType.RIGHT_PAREN, "esperado ')' apos argumentos")
        return arguments

    def _left_associative(self, operand_parser, *operators: TokenType) -> Node:
        expression = operand_parser()
        while self._match(*operators):
            operator = self._previous()
            right = operand_parser()
            expression = BinaryOperation(
                line=operator.line,
                column=operator.column,
                left=expression,
                operator=operator,
                right=right,
            )
        return expression

    def _register_symbol(self, name: str, category: str, type_name: str | None, node_or_token) -> None:
        self.symbols.append(
            Symbol(
                name=name,
                category=category,
                type_name=type_name,
                scope="/".join(self.scope_stack),
                line=node_or_token.line,
                column=node_or_token.column,
            )
        )

    @staticmethod
    def _is_native_callee(expression: Node) -> bool:
        if isinstance(expression, Identifier):
            return expression.name in {"input", "int", "real", "bool", "str", "console.log"}
        if isinstance(expression, AttributeAccess) and isinstance(expression.object_expr, Identifier):
            return expression.object_expr.name == "console" and expression.attribute == "log"
        return False

    def _is_class_constructor_without_new(self, expression: Node) -> bool:
        if not isinstance(expression, Identifier):
            return False
        return expression.name in self.class_names

    def _collect_class_names(self) -> set[str]:
        names: set[str] = set()
        for index, token in enumerate(self.tokens[:-1]):
            if token.type is TokenType.CLASS and self.tokens[index + 1].type is TokenType.IDENTIFIER:
                names.add(self.tokens[index + 1].lexeme)
        return names

    def _match(self, *types: TokenType) -> bool:
        for token_type in types:
            if self._check(token_type):
                self._advance()
                return True
        return False

    def _consume(self, token_type: TokenType, message: str) -> Token:
        if self._check(token_type):
            return self._advance()
        raise self._error(self._peek(), message)

    def _consume_semicolon(self, message: str) -> Token:
        if self._check(TokenType.SEMICOLON):
            return self._advance()
        token = self._previous() if self.current > 0 else self._peek()
        raise self._error(token, message)

    def _check(self, token_type: TokenType) -> bool:
        if self._is_at_end():
            return token_type is TokenType.EOF
        return self._peek().type is token_type

    def _check_any(self, types: set[TokenType]) -> bool:
        return self._peek().type in types

    def _check_next(self, token_type: TokenType) -> bool:
        if self.current + 1 >= len(self.tokens):
            return False
        return self.tokens[self.current + 1].type is token_type

    def _looks_like_global_declaration_without_keyword(self) -> bool:
        return self._check(TokenType.IDENTIFIER) and self._check_next(TokenType.IDENTIFIER)

    def _looks_like_unknown_global_assignment(self) -> bool:
        if not self._check(TokenType.IDENTIFIER):
            return False
        if self.current + 1 >= len(self.tokens):
            return False
        if self.tokens[self.current + 1].type not in ASSIGNMENT_TOKENS:
            return False
        name = self._peek().lexeme
        return not any(symbol.name == name and symbol.scope == "global" for symbol in self.symbols)

    def _check_reserved_word(self) -> bool:
        token = self._peek()
        return token.type not in {TokenType.IDENTIFIER, TokenType.EOF} and token.lexeme.isalpha()

    def _advance(self) -> Token:
        if not self._is_at_end():
            self.current += 1
        return self._previous()

    def _is_at_end(self) -> bool:
        return self._peek().type is TokenType.EOF

    def _peek(self) -> Token:
        return self.tokens[self.current]

    def _previous(self) -> Token:
        return self.tokens[self.current - 1]

    def _error(self, token: Token, message: str) -> SyntaxErrorJSS:
        if token.type is TokenType.EOF and self.current > 0:
            token = self._previous()
        return SyntaxErrorJSS(message, token.line, token.column)

    def _synchronize(self) -> None:
        if not self._is_at_end():
            self._advance()

        while not self._is_at_end():
            if self._previous().type is TokenType.SEMICOLON:
                return
            if self._peek().type in SYNCHRONIZATION_TOKENS:
                return
            self._advance()
