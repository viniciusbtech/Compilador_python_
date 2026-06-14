"""Bateria complementar de testes do analisador léxico JSS."""

from __future__ import annotations

import pytest

from jss_compiler.errors import LexicalError
from jss_compiler.lexer import Lexer
from jss_compiler.tokens import Token, TokenType


def tokens_sem_eof(source: str) -> list[Token]:
    return [
        token
        for token in Lexer(source).tokenize()
        if token.type is not TokenType.EOF
    ]


def tipos_sem_eof(source: str) -> list[TokenType]:
    return [token.type for token in tokens_sem_eof(source)]


def lexemas_sem_eof(source: str) -> list[str]:
    return [token.lexeme for token in tokens_sem_eof(source)]


def test_reconhece_todas_as_palavras_reservadas_incluindo_input() -> None:
    source = (
        "let const function void if else while for break return class "
        "constructor new this true false null input"
    )

    assert tipos_sem_eof(source) == [
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
    ]


def test_reconhece_todos_os_tipos_primitivos() -> None:
    assert tipos_sem_eof("int real str bool") == [
        TokenType.TYPE_INT,
        TokenType.TYPE_REAL,
        TokenType.TYPE_STR,
        TokenType.TYPE_BOOL,
    ]


def test_linguagem_e_case_sensitive() -> None:
    assert tipos_sem_eof("let Let LET int Int INPUT input") == [
        TokenType.LET,
        TokenType.IDENTIFIER,
        TokenType.IDENTIFIER,
        TokenType.TYPE_INT,
        TokenType.IDENTIFIER,
        TokenType.IDENTIFIER,
        TokenType.INPUT,
    ]


def test_reconhece_identificadores_validos() -> None:
    source = "a nome _nome nome2 _2 media_final Ponto"
    assert tipos_sem_eof(source) == [TokenType.IDENTIFIER] * 7
    assert lexemas_sem_eof(source) == source.split()


def test_palavra_reservada_nao_e_classificada_como_identificador() -> None:
    tokens = tokens_sem_eof("if idade")
    assert tokens[0].type is TokenType.IF
    assert tokens[1].type is TokenType.IDENTIFIER


def test_reconhece_inteiros() -> None:
    assert tipos_sem_eof("0 1 25 1000") == [TokenType.INTEGER_LITERAL] * 4


def test_sinal_negativo_e_token_separado_do_numero() -> None:
    assert tipos_sem_eof("-10") == [
        TokenType.MINUS,
        TokenType.INTEGER_LITERAL,
    ]


def test_reconhece_reais_decimais() -> None:
    assert tipos_sem_eof("0.0 1.5 10.8") == [TokenType.REAL_LITERAL] * 3


def test_reconhece_notacao_cientifica() -> None:
    assert tipos_sem_eof("10E2 10e+2 3.5e-4") == [TokenType.REAL_LITERAL] * 3


@pytest.mark.parametrize("source", ["10E", "10e+", "10.5E-"])
def test_rejeita_expoente_sem_digitos(source: str) -> None:
    with pytest.raises(LexicalError, match="expoente numérico inválido"):
        Lexer(source).tokenize()


def test_rejeita_identificador_iniciado_por_numero() -> None:
    with pytest.raises(LexicalError, match="identificador inválido iniciado por número"):
        Lexer("2nome").tokenize()


def test_numero_com_ponto_final_vira_inteiro_e_ponto() -> None:
    assert tipos_sem_eof("10.") == [
        TokenType.INTEGER_LITERAL,
        TokenType.DOT,
    ]


def test_reconhece_string_simples() -> None:
    tokens = tokens_sem_eof('"Olá"')
    assert tokens[0].type is TokenType.STRING_LITERAL
    assert tokens[0].lexeme == '"Olá"'


def test_reconhece_escapes_permitidos_em_string() -> None:
    source = r'"linha\ncoluna\taspas\"barra\\"'
    assert tipos_sem_eof(source) == [TokenType.STRING_LITERAL]


def test_rejeita_escape_invalido() -> None:
    with pytest.raises(LexicalError, match="sequência de escape inválida"):
        Lexer(r'"texto\q"').tokenize()


def test_rejeita_string_sem_aspas_finais() -> None:
    with pytest.raises(LexicalError, match="string não terminada"):
        Lexer('"texto').tokenize()


def test_rejeita_string_quebrada_em_duas_linhas() -> None:
    with pytest.raises(LexicalError, match="string não terminada"):
        Lexer('"primeira linha\nsegunda linha"').tokenize()


def test_ignora_comentario_de_linha() -> None:
    source = "let int x; // comentário ignorado\nconst real y;"
    assert tipos_sem_eof(source) == [
        TokenType.LET,
        TokenType.TYPE_INT,
        TokenType.IDENTIFIER,
        TokenType.SEMICOLON,
        TokenType.CONST,
        TokenType.TYPE_REAL,
        TokenType.IDENTIFIER,
        TokenType.SEMICOLON,
    ]


def test_comentario_atualiza_a_linha_do_token_seguinte() -> None:
    tokens = tokens_sem_eof("// linha 1\n// linha 2\nlet")
    assert tokens[0].type is TokenType.LET
    assert (tokens[0].line, tokens[0].column) == (3, 1)


def test_reconhece_pontuacao() -> None:
    assert tipos_sem_eof("( ) { } [ ] ; , .") == [
        TokenType.LEFT_PAREN,
        TokenType.RIGHT_PAREN,
        TokenType.LEFT_BRACE,
        TokenType.RIGHT_BRACE,
        TokenType.LEFT_BRACKET,
        TokenType.RIGHT_BRACKET,
        TokenType.SEMICOLON,
        TokenType.COMMA,
        TokenType.DOT,
    ]


def test_reconhece_operadores_de_um_caractere() -> None:
    assert tipos_sem_eof("+ - * / % = > < !") == [
        TokenType.PLUS,
        TokenType.MINUS,
        TokenType.STAR,
        TokenType.SLASH,
        TokenType.PERCENT,
        TokenType.ASSIGN,
        TokenType.GREATER,
        TokenType.LESS,
        TokenType.BANG,
    ]


def test_reconhece_operadores_de_dois_caracteres() -> None:
    assert tipos_sem_eof("** == != >= <= && || ++ -- += -= *= /= %=") == [
        TokenType.POWER,
        TokenType.EQUAL_EQUAL,
        TokenType.BANG_EQUAL,
        TokenType.GREATER_EQUAL,
        TokenType.LESS_EQUAL,
        TokenType.AND_AND,
        TokenType.OR_OR,
        TokenType.PLUS_PLUS,
        TokenType.MINUS_MINUS,
        TokenType.PLUS_ASSIGN,
        TokenType.MINUS_ASSIGN,
        TokenType.STAR_ASSIGN,
        TokenType.SLASH_ASSIGN,
        TokenType.PERCENT_ASSIGN,
    ]


def test_reconhece_operador_de_tres_caracteres() -> None:
    tokens = tokens_sem_eof("x **= 2;")
    assert [token.type for token in tokens] == [
        TokenType.IDENTIFIER,
        TokenType.POWER_ASSIGN,
        TokenType.INTEGER_LITERAL,
        TokenType.SEMICOLON,
    ]
    assert tokens[1].lexeme == "**="


def test_aplica_regra_do_maior_lexema() -> None:
    assert tipos_sem_eof("* ** *= **=") == [
        TokenType.STAR,
        TokenType.POWER,
        TokenType.STAR_ASSIGN,
        TokenType.POWER_ASSIGN,
    ]


def test_diferencia_divisao_atribuicao_e_comentario() -> None:
    source = "a / b; a /= b; // comentário\na / b;"
    assert tipos_sem_eof(source) == [
        TokenType.IDENTIFIER,
        TokenType.SLASH,
        TokenType.IDENTIFIER,
        TokenType.SEMICOLON,
        TokenType.IDENTIFIER,
        TokenType.SLASH_ASSIGN,
        TokenType.IDENTIFIER,
        TokenType.SEMICOLON,
        TokenType.IDENTIFIER,
        TokenType.SLASH,
        TokenType.IDENTIFIER,
        TokenType.SEMICOLON,
    ]


def test_input_possui_token_proprio() -> None:
    assert tipos_sem_eof("input(numero);") == [
        TokenType.INPUT,
        TokenType.LEFT_PAREN,
        TokenType.IDENTIFIER,
        TokenType.RIGHT_PAREN,
        TokenType.SEMICOLON,
    ]


def test_console_log_e_reconhecido_com_identificadores_e_ponto() -> None:
    assert tipos_sem_eof('console.log("Olá");') == [
        TokenType.IDENTIFIER,
        TokenType.DOT,
        TokenType.IDENTIFIER,
        TokenType.LEFT_PAREN,
        TokenType.STRING_LITERAL,
        TokenType.RIGHT_PAREN,
        TokenType.SEMICOLON,
    ]


def test_registra_linha_e_coluna_dos_tokens() -> None:
    tokens = tokens_sem_eof("let int x;\n    const real y;")
    assert (tokens[0].line, tokens[0].column) == (1, 1)
    const_token = next(token for token in tokens if token.type is TokenType.CONST)
    assert (const_token.line, const_token.column) == (2, 5)


def test_erro_de_caractere_invalido_informa_linha_e_coluna() -> None:
    with pytest.raises(LexicalError) as exception:
        Lexer("let int x;\n  @").tokenize()

    message = str(exception.value)
    assert "linha 2, coluna 3" in message
    assert "caractere inválido '@'" in message


def test_entrada_vazia_produz_apenas_eof() -> None:
    tokens = Lexer("").tokenize()
    assert len(tokens) == 1
    assert tokens[0].type is TokenType.EOF
    assert (tokens[0].line, tokens[0].column) == (1, 1)


def test_programa_lexicamente_valido() -> None:
    source = """
function void main() {
    let int numero = 10;
    let real media = 8.5;
    const str mensagem = "Resultado";
    input(numero);
    console.log(mensagem, numero, media);
}
"""

    tokens = Lexer(source).tokenize()
    assert tokens[-1].type is TokenType.EOF
    assert any(token.type is TokenType.FUNCTION for token in tokens)
    assert any(token.type is TokenType.INPUT for token in tokens)
    assert any(token.type is TokenType.STRING_LITERAL for token in tokens)
