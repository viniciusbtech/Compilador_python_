"""Testes de execucao do compilador para entradas invalidas."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
MAIN_FILE = ROOT / "main.py"
SRC_DIR = ROOT / "src"


CASOS_DE_ERRO = [
    pytest.param(
        "let int x = 10 @ 2;",
        "Erro léxico na linha 1, coluna 16: caractere inválido '@'",
        id="caractere-invalido-arroba",
    ),
    pytest.param(
        'let str s = "texto',
        "Erro léxico na linha 1, coluna 13: string não terminada",
        id="string-nao-terminada",
    ),
    pytest.param(
        "let real x = 10E;",
        (
            "Erro léxico na linha 1, coluna 16: "
            "expoente numérico inválido; era esperado um dígito"
        ),
        id="expoente-sem-digito",
    ),
    pytest.param(
        "let int 2nome = 1;",
        (
            "Erro léxico na linha 1, coluna 9: "
            "identificador inválido iniciado por número: '2n'"
        ),
        id="identificador-iniciado-por-numero",
    ),
    pytest.param(
        'let str s = "abc\\q";',
        (
            "Erro léxico na linha 1, coluna 17: "
            "sequência de escape inválida: \\q"
        ),
        id="escape-invalido",
    ),
    pytest.param(
        "let bool x = true & false;",
        "Erro léxico na linha 1, coluna 19: caractere inválido '&'",
        id="operador-e-incompleto",
    ),
    pytest.param(
        "let bool x = true | false;",
        "Erro léxico na linha 1, coluna 19: caractere inválido '|'",
        id="operador-ou-incompleto",
    ),
    pytest.param(
        "let str s = 'abc';",
        'Erro léxico na linha 1, coluna 13: caractere inválido "\'"',
        id="string-com-aspas-simples",
    ),
    pytest.param(
        "let str s = `abc`;",
        "Erro léxico na linha 1, coluna 13: caractere inválido '`'",
        id="template-string-nao-suportada",
    ),
    pytest.param(
        "function void main() {\n    int let x = 10;\n}",
        "Erro sintático na linha 2, coluna 9: token inesperado 'let'",
        id="let-apos-tipo-primitivo",
    ),
]


def executar_compilador(codigo_fonte: str) -> subprocess.CompletedProcess[str]:
    ambiente = os.environ.copy()
    pythonpath_atual = ambiente.get("PYTHONPATH", "")
    ambiente["PYTHONPATH"] = (
        str(SRC_DIR)
        if not pythonpath_atual
        else str(SRC_DIR) + os.pathsep + pythonpath_atual
    )
    ambiente["PYTHONUTF8"] = "1"

    return subprocess.run(
        [sys.executable, str(MAIN_FILE)],
        input=codigo_fonte,
        text=True,
        encoding="utf-8",
        capture_output=True,
        cwd=ROOT,
        env=ambiente,
        check=False,
    )


@pytest.mark.parametrize(("codigo_fonte", "erro_esperado"), CASOS_DE_ERRO)
def test_execucao_deve_retornar_erro_lexico(
    codigo_fonte: str,
    erro_esperado: str,
) -> None:
    resultado = executar_compilador(codigo_fonte)

    assert resultado.returncode == 1
    assert resultado.stdout.strip() == erro_esperado
    assert resultado.stderr == ""


def test_entrada_vazia_deve_retornar_erro() -> None:
    resultado = executar_compilador("")

    assert resultado.returncode == 1
    assert resultado.stdout.strip() == "Erro: nenhum programa JSS foi fornecido na entrada padrão."
    assert resultado.stderr == ""
