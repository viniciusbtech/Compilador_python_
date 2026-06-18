from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from jss_compiler.errors import SemanticError
from jss_compiler.frontend import analyze_source


ROOT = Path(__file__).resolve().parents[1]
MAIN_FILE = ROOT / "main.py"
SRC_DIR = ROOT / "src"


def assert_semantic_error(source: str, message: str) -> None:
    with pytest.raises(SemanticError, match=message):
        analyze_source(source)


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


def test_programa_semanticamente_valido() -> None:
    analyze_source(
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

let int [3] valores = [1, 2, 3];
const str titulo = "ponto";

function void main() {
    let Ponto p = new Ponto(1, 2);
    let real total = real(p.soma()) + 1.5;
    console.log(titulo + ": " + str(total));
    return;
}
"""
    )


def test_rejeita_redeclaracao_no_mesmo_escopo() -> None:
    assert_semantic_error(
        """
function void main() {
    let int x = 1;
    const real x = 2.0;
}
""",
        "ja declarado neste escopo",
    )


def test_permite_case_sensitive_em_identificadores() -> None:
    analyze_source(
        """
function void main() {
    let int var = 1;
    let int VAR = 2;
    console.log(var + VAR);
}
"""
    )


def test_rejeita_atribuicao_em_constante_e_vetor_constante() -> None:
    assert_semantic_error(
        """
function void main() {
    const int x = 1;
    x = 2;
}
""",
        "constante 'x' nao pode ser alterada",
    )
    assert_semantic_error(
        """
function void main() {
    const int [2] xs = [1, 2];
    xs[0] = 3;
}
""",
        "vetor constante 'xs' nao pode ser alterado",
    )


def test_rejeita_vetor_com_elementos_incompativeis() -> None:
    assert_semantic_error(
        "let int [2] xs = [1, \"dois\"];",
        "tipo incompativel: esperado int, recebido str",
    )


def test_operadores_e_casts_validam_tipos() -> None:
    analyze_source(
        """
function void main() {
    let real x = real(1) + 2.5;
    let str y = "valor=" + str(x);
    let bool ok = bool(1) || false;
}
"""
    )
    assert_semantic_error(
        """
function void main() {
    let bool x = 1 && true;
}
""",
        "operadores logicos requerem bool",
    )


def test_regras_de_classe_e_main() -> None:
    assert_semantic_error(
        """
class Ruim {
    void m() {}
    int x;
}
""",
        "atributos devem ser declarados antes de metodos",
    )
    analyze_source(
        """
class SemMetodo {
    int x;
    SemMetodo constructor() {}
}
"""
    )
    assert_semantic_error(
        """
class SemConstrutor {
    int x;
}
""",
        "classe deve possuir ao menos um construtor",
    )
    assert_semantic_error(
        """
class SemVariavel {
    SemVariavel constructor() {}
}
""",
        "classe deve possuir ao menos uma variavel",
    )
    assert_semantic_error(
        "function void main(int argc) {}",
        "funcao main nao deve possuir parametros",
    )


def test_rejeita_conversao_implicita_e_mistura_de_tipos() -> None:
    assert_semantic_error(
        "let real x = 1;",
        "tipo incompativel: esperado real, recebido int",
    )
    assert_semantic_error(
        "let real x = 1 + 2.5;",
        "tipos misturados nao sao permitidos: int e real",
    )


def test_permite_atribuicao_global_apos_declaracao() -> None:
    analyze_source(
        """
let int x = 1;
x = 2;
"""
    )


def test_rejeita_funcao_com_nome_ja_declarado() -> None:
    assert_semantic_error(
        """
let int soma;
function int soma() {
    return 1;
}
""",
        "ja declarado neste escopo",
    )


def test_cli_emite_erro_semantico_na_saida_padrao() -> None:
    resultado = executar_compilador(
        """
function void main() {
    const int x = 1;
    x = 2;
}
"""
    )

    assert resultado.returncode == 1
    assert resultado.stderr == ""
    assert "Erro sem" in resultado.stdout
    assert "linha 4" in resultado.stdout
    assert "constante 'x' nao pode ser alterada" in resultado.stdout
