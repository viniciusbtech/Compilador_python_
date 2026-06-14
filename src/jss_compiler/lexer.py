"""Analisador léxico da linguagem Java Script Simplificado (JSS)."""

from __future__ import annotations

from .errors import LexicalError
from .tokens import Token, TokenType


class Lexer:
    """Converte o código-fonte JSS em uma sequência de tokens.

    O analisador é sensível a maiúsculas e minúsculas. Portanto, apenas a
    grafia exata de uma palavra reservada é reconhecida como tal. Por exemplo,
    ``let`` é palavra reservada, enquanto ``LET`` é um identificador.
    """

    KEYWORDS: dict[str, TokenType] = {
        "let": TokenType.LET,
        "const": TokenType.CONST,
        "function": TokenType.FUNCTION,
        "void": TokenType.VOID,
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "while": TokenType.WHILE,
        "for": TokenType.FOR,
        "break": TokenType.BREAK,
        "return": TokenType.RETURN,
        "class": TokenType.CLASS,
        "constructor": TokenType.CONSTRUCTOR,
        "new": TokenType.NEW,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "false": TokenType.FALSE,
        "null": TokenType.NULL,
 
        "input": TokenType.INPUT,

        "int": TokenType.TYPE_INT,
        "real": TokenType.TYPE_REAL,
        "str": TokenType.TYPE_STR,
        "bool": TokenType.TYPE_BOOL,
    }

    THREE_CHARACTER_TOKENS: dict[str, TokenType] = {
    "**=": TokenType.POWER_ASSIGN,
     }

    TWO_CHARACTER_TOKENS: dict[str, TokenType] = {
        "**": TokenType.POWER,
        "==": TokenType.EQUAL_EQUAL,
        "!=": TokenType.BANG_EQUAL,
        ">=": TokenType.GREATER_EQUAL,
        "<=": TokenType.LESS_EQUAL,
        "&&": TokenType.AND_AND,
        "||": TokenType.OR_OR,
        "++": TokenType.PLUS_PLUS,
        "--": TokenType.MINUS_MINUS,
        "+=": TokenType.PLUS_ASSIGN,
        "-=": TokenType.MINUS_ASSIGN,
        "*=": TokenType.STAR_ASSIGN,
        "/=": TokenType.SLASH_ASSIGN,
        "%=": TokenType.PERCENT_ASSIGN,
    }

    ONE_CHARACTER_TOKENS: dict[str, TokenType] = {
        "(": TokenType.LEFT_PAREN,
        ")": TokenType.RIGHT_PAREN,
        "{": TokenType.LEFT_BRACE,
        "}": TokenType.RIGHT_BRACE,
        "[": TokenType.LEFT_BRACKET,
        "]": TokenType.RIGHT_BRACKET,
        ";": TokenType.SEMICOLON,
        ",": TokenType.COMMA,
        ".": TokenType.DOT,

        "=": TokenType.ASSIGN,
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "*": TokenType.STAR,
        "/": TokenType.SLASH,
        "%": TokenType.PERCENT,
        ">": TokenType.GREATER,
        "<": TokenType.LESS,
        "!": TokenType.BANG,
    }

    VALID_ESCAPES = {"n", "t", "r", '"', "\\"}

    def __init__(self, source: str) -> None:
        self.source = source
        self.current = 0
        self.line = 1
        self.column = 1

    def tokenize(self) -> list[Token]:
        """Analisa todo o código-fonte e devolve seus tokens.

        Espaços, quebras de linha e comentários iniciados por ``//`` não são
        incluídos na lista. Um token EOF é acrescentado ao final.
        """
        tokens: list[Token] = []

        while not self._is_at_end():
            self._skip_ignored_characters()
            if self._is_at_end():
                break

            token = self._scan_token()
            tokens.append(token)

        tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return tokens

    def _scan_token(self) -> Token:
        start = self.current
        start_line = self.line
        start_column = self.column
        character = self._peek()

        if self._is_identifier_start(character):
            return self._identifier(start, start_line, start_column)

        if character.isdigit():
            return self._number(start, start_line, start_column)

        if character == '"':
            return self._string(start, start_line, start_column)
        
        triple = self.source[self.current : self.current + 3]

        if triple in self.THREE_CHARACTER_TOKENS:
            self._advance()
            self._advance()
            self._advance()
            return Token(
            type=self.THREE_CHARACTER_TOKENS[triple],
            lexeme=triple,
            line=start_line,
            column=start_column,
            )

        pair = self.source[self.current : self.current + 2]
        token_type = self.TWO_CHARACTER_TOKENS.get(pair)
        if token_type is not None:
            self._advance()
            self._advance()
            return Token(token_type, pair, start_line, start_column)

        token_type = self.ONE_CHARACTER_TOKENS.get(character)
        if token_type is not None:
            lexeme = self._advance()
            return Token(token_type, lexeme, start_line, start_column)

        raise LexicalError(
            f"caractere inválido {character!r}", start_line, start_column
        )

    def _skip_ignored_characters(self) -> None:
        while not self._is_at_end():
            character = self._peek()

            if character in {" ", "\t", "\r", "\n"}:
                self._advance()
                continue

            if character == "/" and self._peek_next() == "/":
                while not self._is_at_end() and self._peek() != "\n":
                    self._advance()
                continue

            return

    def _identifier(self, start: int, line: int, column: int) -> Token:
        while self._is_identifier_part(self._peek()):
            self._advance()

        lexeme = self.source[start : self.current]
        token_type = self.KEYWORDS.get(lexeme, TokenType.IDENTIFIER)
        return Token(token_type, lexeme, line, column)

    def _number(self, start: int, line: int, column: int) -> Token:
        while self._peek().isdigit():
            self._advance()

        is_real = False

        # Parte decimal: exige ao menos um dígito depois do ponto.
        if self._peek() == "." and self._peek_next().isdigit():
            is_real = True
            self._advance()
            while self._peek().isdigit():
                self._advance()

        # Notação científica: 10E2, 3.5e-4 etc.
        if self._peek() in {"e", "E"}:
            is_real = True
            exponent_line = self.line
            exponent_column = self.column
            self._advance()

            if self._peek() in {"+", "-"}:
                self._advance()

            if not self._peek().isdigit():
                raise LexicalError(
                    "expoente numérico inválido; era esperado um dígito",
                    exponent_line,
                    exponent_column,
                )

            while self._peek().isdigit():
                self._advance()

        if self._is_identifier_start(self._peek()):
            malformed = self.source[start : self.current + 1]
            raise LexicalError(
                f"identificador inválido iniciado por número: {malformed!r}",
                line,
                column,
            )

        lexeme = self.source[start : self.current]
        token_type = (
            TokenType.REAL_LITERAL if is_real else TokenType.INTEGER_LITERAL
        )
        return Token(token_type, lexeme, line, column)

    def _string(self, start: int, line: int, column: int) -> Token:
        self._advance()  # aspas iniciais

        while not self._is_at_end() and self._peek() != '"':
            if self._peek() == "\n":
                raise LexicalError("string não terminada", line, column)

            if self._peek() == "\\":
                escape_line = self.line
                escape_column = self.column
                self._advance()

                if self._is_at_end() or self._peek() == "\n":
                    raise LexicalError("string não terminada", line, column)

                escaped = self._peek()
                if escaped not in self.VALID_ESCAPES:
                    raise LexicalError(
                        f"sequência de escape inválida: \\{escaped}",
                        escape_line,
                        escape_column,
                    )

                self._advance()
                continue

            self._advance()

        if self._is_at_end():
            raise LexicalError("string não terminada", line, column)

        self._advance()  # aspas finais
        lexeme = self.source[start : self.current]
        return Token(TokenType.STRING_LITERAL, lexeme, line, column)

    def _advance(self) -> str:
        character = self.source[self.current]
        self.current += 1

        if character == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return character

    def _peek(self) -> str:
        if self._is_at_end():
            return "\0"
        return self.source[self.current]

    def _peek_next(self) -> str:
        next_position = self.current + 1
        if next_position >= len(self.source):
            return "\0"
        return self.source[next_position]

    def _is_at_end(self) -> bool:
        return self.current >= len(self.source)

    @staticmethod
    def _is_identifier_start(character: str) -> bool:
        return (
            character == "_"
            or "a" <= character <= "z"
            or "A" <= character <= "Z"
        )

    @classmethod
    def _is_identifier_part(cls, character: str) -> bool:
        return cls._is_identifier_start(character) or character.isdigit()
