from __future__ import annotations

import pytest

from jss_compiler.ast_nodes import (
    Assignment,
    BinaryOperation,
    Call,
    ClassDeclaration,
    FunctionDeclaration,
    IfStatement,
    VarDeclaration,
)
from jss_compiler.errors import SyntaxErrorJSS
from jss_compiler.lexer import Lexer
from jss_compiler.parser import Parser


def parse(source: str):
    return Parser(Lexer(source).tokenize()).parse()


def test_parse_declaracoes_globais_e_comandos_basicos() -> None:
    ast = parse(
        """
let int x;
const str nome = "Ana";

function void main() {
    let real media = 10.5;
    input(x);
    console.log(nome, media);
    if (x > 0) {
        x += 1;
    } else if (x == 0) {
        x = 2;
    } else {
        x = 3;
    }
    while (x < 10) {
        break;
    }
    for (x = 0; x < 3; x += 1) {
        console.log(x);
    }
    return;
}
"""
    )

    assert len(ast.declarations) == 3
    assert isinstance(ast.declarations[0], VarDeclaration)
    assert isinstance(ast.declarations[2], FunctionDeclaration)
    assert any(symbol.name == "main" and symbol.category == "funcao" for symbol in ast.symbols)


def test_parse_vetores_objetos_classes_e_metodos() -> None:
    ast = parse(
        """
class Ponto {
    int x;
    int y;
    Ponto constructor(int x, int y) {
        this.x = x;
        this.y = y;
    }
    int soma() {
        return this.x + this.y;
    }
}

let int [3] lista = [1, 2, 3];
let Ponto p = new Ponto(1, 2);
"""
    )

    assert isinstance(ast.declarations[0], ClassDeclaration)
    assert ast.declarations[1].type_node.is_array is True
    assert ast.declarations[1].declarators[0].array_values


def test_precedencia_multiplicacao_maior_que_soma() -> None:
    ast = parse("let int x = 1 + 2 * 3;")
    initializer = ast.declarations[0].declarators[0].initializer

    assert isinstance(initializer, BinaryOperation)
    assert initializer.operator.lexeme == "+"
    assert isinstance(initializer.right, BinaryOperation)
    assert initializer.right.operator.lexeme == "*"


def test_atribuicao_e_exponenciacao_sao_associativas_a_direita() -> None:
    ast = parse(
        """
function void main() {
    x = y = 10;
    z = 2 ** 3 ** 2;
}
"""
    )
    assignment_statement = ast.declarations[0].body.statements[0].expression
    power_statement = ast.declarations[0].body.statements[1].expression

    assert isinstance(assignment_statement, Assignment)
    assert isinstance(assignment_statement.value, Assignment)

    assert isinstance(power_statement, Assignment)
    assert isinstance(power_statement.value, BinaryOperation)
    assert power_statement.value.operator.lexeme == "**"
    assert isinstance(power_statement.value.right, BinaryOperation)
    assert power_statement.value.right.operator.lexeme == "**"


def test_casts_e_chamadas_nativas_sao_marcadas_na_ast() -> None:
    ast = parse(
        """
function void main() {
    let int x = int(10.5);
    console.log(str(x));
}
"""
    )

    cast_call = ast.declarations[0].body.statements[0].declarators[0].initializer
    console_call = ast.declarations[0].body.statements[1].expression

    assert isinstance(cast_call, Call)
    assert cast_call.native is True
    assert isinstance(console_call, Call)
    assert console_call.native is True


def test_rejeita_funcao_aninhada() -> None:
    with pytest.raises(SyntaxErrorJSS, match="funcao nao pode ser declarada dentro de bloco"):
        parse("function void main() { function void interna() {} }")


def test_rejeita_void_como_tipo_de_variavel() -> None:
    with pytest.raises(SyntaxErrorJSS, match="esperado tipo"):
        parse("let void x;")


def test_rejeita_ponto_e_virgula_ausente() -> None:
    with pytest.raises(SyntaxErrorJSS, match="esperado ';' apos declaracao"):
        parse("let int x")


def test_erro_parametros_informa_parentese_ausente_antes_do_bloco() -> None:
    with pytest.raises(SyntaxErrorJSS) as exception:
        parse("function void main( {")

    assert str(exception.value) == "Erro sintático na linha 1, coluna 21: esperado tipo ) antes de {"


def test_erro_no_fim_do_arquivo_usa_linha_do_ultimo_token_real() -> None:
    source = "let int a;\nlet int b;\nlet int c\n"

    with pytest.raises(SyntaxErrorJSS) as exception:
        parse(source)

    assert "Erro sintático na linha 3," in str(exception.value)
