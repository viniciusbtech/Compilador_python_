from __future__ import annotations

import pytest

from jss_compiler.errors import SyntaxErrorJSS
from jss_compiler.lexer import Lexer
from jss_compiler.parser import Parser


def parse(source: str):
    return Parser(Lexer(source).tokenize()).parse()


def test_ponto_e_virgula_ausente_antes_de_fecha_chave_usa_linha_da_expressao() -> None:
    source = """function void main() {
    let int numero = 10;
    console.log(numero)
}"""

    with pytest.raises(SyntaxErrorJSS) as exception:
        parse(source)

    assert "linha 3," in str(exception.value)
    assert "esperado ';' apos expressao" in str(exception.value)
