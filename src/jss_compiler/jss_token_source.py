"""Ponte entre a lista de Token JSS e o CommonTokenStream do ANTLR4."""

from __future__ import annotations

from antlr4 import Token as AntlrToken  # type: ignore[import-untyped]
from antlr4.Token import CommonToken  # type: ignore[import-untyped]

from .antlr_generated.JSSLexer import JSSLexer
from .tokens import Token, TokenType

# Mapeamento de TokenType (JSS) → constante de tipo do JSSLexer (ANTLR)
_JSS_TO_ANTLR: dict[TokenType, int] = {
    TokenType.EOF:            AntlrToken.EOF,
    TokenType.LET:            JSSLexer.LET,
    TokenType.CONST:          JSSLexer.CONST,
    TokenType.FUNCTION:       JSSLexer.FUNCTION,
    TokenType.VOID:           JSSLexer.VOID,
    TokenType.IF:             JSSLexer.IF,
    TokenType.ELSE:           JSSLexer.ELSE,
    TokenType.WHILE:          JSSLexer.WHILE,
    TokenType.FOR:            JSSLexer.FOR,
    TokenType.BREAK:          JSSLexer.BREAK,
    TokenType.RETURN:         JSSLexer.RETURN,
    TokenType.CLASS:          JSSLexer.CLASS,
    TokenType.CONSTRUCTOR:    JSSLexer.CONSTRUCTOR,
    TokenType.NEW:            JSSLexer.NEW,
    TokenType.THIS:           JSSLexer.THIS,
    TokenType.TRUE:           JSSLexer.TRUE,
    TokenType.FALSE:          JSSLexer.FALSE,
    TokenType.NULL:           JSSLexer.NULL,
    TokenType.INPUT:          JSSLexer.INPUT,
    TokenType.CONSOLE_LOG:    JSSLexer.CONSOLE_LOG,
    TokenType.TYPE_INT:       JSSLexer.TYPE_INT,
    TokenType.TYPE_REAL:      JSSLexer.TYPE_REAL,
    TokenType.TYPE_STR:       JSSLexer.TYPE_STR,
    TokenType.TYPE_BOOL:      JSSLexer.TYPE_BOOL,
    TokenType.INTEGER_LITERAL: JSSLexer.INTEGER_LITERAL,
    TokenType.REAL_LITERAL:   JSSLexer.REAL_LITERAL,
    TokenType.STRING_LITERAL: JSSLexer.STRING_LITERAL,
    TokenType.IDENTIFIER:     JSSLexer.IDENTIFIER,
    TokenType.POWER_ASSIGN:   JSSLexer.POWER_ASSIGN,
    TokenType.AND_AND_ASSIGN: JSSLexer.AND_AND_ASSIGN,
    TokenType.OR_OR_ASSIGN:   JSSLexer.OR_OR_ASSIGN,
    TokenType.POWER:          JSSLexer.POWER,
    TokenType.EQUAL_EQUAL:    JSSLexer.EQUAL_EQUAL,
    TokenType.BANG_EQUAL:     JSSLexer.BANG_EQUAL,
    TokenType.GREATER_EQUAL:  JSSLexer.GREATER_EQUAL,
    TokenType.LESS_EQUAL:     JSSLexer.LESS_EQUAL,
    TokenType.AND_AND:        JSSLexer.AND_AND,
    TokenType.OR_OR:          JSSLexer.OR_OR,
    TokenType.PLUS_PLUS:      JSSLexer.PLUS_PLUS,
    TokenType.MINUS_MINUS:    JSSLexer.MINUS_MINUS,
    TokenType.PLUS_ASSIGN:    JSSLexer.PLUS_ASSIGN,
    TokenType.MINUS_ASSIGN:   JSSLexer.MINUS_ASSIGN,
    TokenType.STAR_ASSIGN:    JSSLexer.STAR_ASSIGN,
    TokenType.SLASH_ASSIGN:   JSSLexer.SLASH_ASSIGN,
    TokenType.PERCENT_ASSIGN: JSSLexer.PERCENT_ASSIGN,
    TokenType.ASSIGN:         JSSLexer.ASSIGN,
    TokenType.PLUS:           JSSLexer.PLUS,
    TokenType.MINUS:          JSSLexer.MINUS,
    TokenType.STAR:           JSSLexer.STAR,
    TokenType.SLASH:          JSSLexer.SLASH,
    TokenType.PERCENT:        JSSLexer.PERCENT,
    TokenType.BANG:           JSSLexer.BANG,
    TokenType.GREATER:        JSSLexer.GREATER,
    TokenType.LESS:           JSSLexer.LESS,
    TokenType.LEFT_PAREN:     JSSLexer.LEFT_PAREN,
    TokenType.RIGHT_PAREN:    JSSLexer.RIGHT_PAREN,
    TokenType.LEFT_BRACE:     JSSLexer.LEFT_BRACE,
    TokenType.RIGHT_BRACE:    JSSLexer.RIGHT_BRACE,
    TokenType.LEFT_BRACKET:   JSSLexer.LEFT_BRACKET,
    TokenType.RIGHT_BRACKET:  JSSLexer.RIGHT_BRACKET,
    TokenType.SEMICOLON:      JSSLexer.SEMICOLON,
    TokenType.COMMA:          JSSLexer.COMMA,
    TokenType.DOT:            JSSLexer.DOT,
}


class JSSTokenSource:
    """Fonte de tokens ANTLR alimentada pela lista de Token do lexer JSS."""

    # Atributos exigidos pela interface TokenSource do ANTLR
    line: int = 0
    column: int = -1

    def __init__(self, jss_tokens: list[Token]) -> None:
        self._tokens = jss_tokens
        self._pos = 0
        self.inputStream = None  # exigido por CommonToken

    def nextToken(self) -> AntlrToken:
        if self._pos >= len(self._tokens):
            tok = CommonToken(source=(self, self.inputStream), type=AntlrToken.EOF)
            tok.line = 1
            tok.column = 0
            return tok

        jss = self._tokens[self._pos]
        self._pos += 1
        antlr_type = _JSS_TO_ANTLR.get(jss.type, AntlrToken.INVALID_TYPE)

        tok = CommonToken(source=(self, self.inputStream), type=antlr_type)
        tok.text = jss.lexeme
        tok.line = jss.line
        tok.column = jss.column - 1  # ANTLR usa coluna 0-based; JSS usa 1-based
        tok.channel = AntlrToken.DEFAULT_CHANNEL
        return tok

    def getSourceName(self) -> str:
        return "<jss-lexer>"
