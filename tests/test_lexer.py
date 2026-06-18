import pytest

from jss_compiler.errors import LexicalError
from jss_compiler.lexer import Lexer
from jss_compiler.tokens import TokenType


def token_types(source: str) -> list[TokenType]:
    return [token.type for token in Lexer(source).tokenize()]


def test_recognizes_keywords_and_types() -> None:
    source = (
        "let const function void if else while for break return class "
        "constructor new this true false null input console.log int real str bool"
    )

    assert token_types(source) == [
        TokenType.LET,
        TokenType.CONST,
        TokenType.FUNCTION,
        TokenType.VOID,
        TokenType.IF,
        TokenType.ELSE,
        TokenType.WHILE,
        TokenType.FOR,
        TokenType.BREAK,
        TokenType.RETURN,
        TokenType.CLASS,
        TokenType.CONSTRUCTOR,
        TokenType.NEW,
        TokenType.THIS,
        TokenType.TRUE,
        TokenType.FALSE,
        TokenType.NULL,
        TokenType.INPUT,
        TokenType.CONSOLE_LOG,
        TokenType.TYPE_INT,
        TokenType.TYPE_REAL,
        TokenType.TYPE_STR,
        TokenType.TYPE_BOOL,
        TokenType.EOF,
    ]


def test_is_case_sensitive() -> None:
    tokens = Lexer("let LET VaR").tokenize()

    assert [token.type for token in tokens] == [
        TokenType.LET,
        TokenType.IDENTIFIER,
        TokenType.IDENTIFIER,
        TokenType.EOF,
    ]
    assert [token.lexeme for token in tokens[:-1]] == ["let", "LET", "VaR"]


def test_recognizes_valid_identifiers() -> None:
    tokens = Lexer("nome _nome nome2 _2").tokenize()

    assert [token.type for token in tokens] == [
        TokenType.IDENTIFIER,
        TokenType.IDENTIFIER,
        TokenType.IDENTIFIER,
        TokenType.IDENTIFIER,
        TokenType.EOF,
    ]


def test_rejects_character_outside_identifier_alphabet() -> None:
    with pytest.raises(LexicalError, match="caractere inválido"):
        Lexer("ação").tokenize()


def test_rejects_identifier_beginning_with_digit() -> None:
    with pytest.raises(LexicalError, match="iniciado por número"):
        Lexer("2nome").tokenize()


def test_recognizes_integer_real_and_scientific_notation() -> None:
    tokens = Lexer("10 1.5 10E2 3.25e-4").tokenize()

    assert [token.type for token in tokens] == [
        TokenType.INTEGER_LITERAL,
        TokenType.REAL_LITERAL,
        TokenType.REAL_LITERAL,
        TokenType.REAL_LITERAL,
        TokenType.EOF,
    ]


def test_recognizes_string_and_escapes() -> None:
    tokens = Lexer(r'"Olá\n" "texto com \"aspas\""').tokenize()

    assert [token.type for token in tokens] == [
        TokenType.STRING_LITERAL,
        TokenType.STRING_LITERAL,
        TokenType.EOF,
    ]


def test_ignores_line_comment_and_tracks_line() -> None:
    tokens = Lexer("let int x; // comentário\nconst real y;").tokenize()

    const_token = next(token for token in tokens if token.type is TokenType.CONST)
    assert const_token.line == 2
    assert const_token.column == 1


def test_recognizes_operators_and_punctuation() -> None:
    source = (
        "+ - * / % ** == != > >= < <= && || ! ++ -- = += -= "
        "( ) { } [ ] ; , ."
    )

    assert token_types(source) == [
        TokenType.PLUS,
        TokenType.MINUS,
        TokenType.STAR,
        TokenType.SLASH,
        TokenType.PERCENT,
        TokenType.POWER,
        TokenType.EQUAL_EQUAL,
        TokenType.BANG_EQUAL,
        TokenType.GREATER,
        TokenType.GREATER_EQUAL,
        TokenType.LESS,
        TokenType.LESS_EQUAL,
        TokenType.AND_AND,
        TokenType.OR_OR,
        TokenType.BANG,
        TokenType.PLUS_PLUS,
        TokenType.MINUS_MINUS,
        TokenType.ASSIGN,
        TokenType.PLUS_ASSIGN,
        TokenType.MINUS_ASSIGN,
        TokenType.LEFT_PAREN,
        TokenType.RIGHT_PAREN,
        TokenType.LEFT_BRACE,
        TokenType.RIGHT_BRACE,
        TokenType.LEFT_BRACKET,
        TokenType.RIGHT_BRACKET,
        TokenType.SEMICOLON,
        TokenType.COMMA,
        TokenType.DOT,
        TokenType.EOF,
    ]


def test_reports_invalid_character_with_location() -> None:
    with pytest.raises(LexicalError) as exception:
        Lexer("let int x = 1;\n@").tokenize()

    assert "linha 2, coluna 1" in str(exception.value)
    assert "caractere inválido" in str(exception.value)


def test_reports_unterminated_string() -> None:
    with pytest.raises(LexicalError, match="string não terminada"):
        Lexer('"texto').tokenize()
