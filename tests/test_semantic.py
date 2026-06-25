from __future__ import annotations

import os
import subprocess
import sys
import tempfile
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

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".jss", encoding="utf-8", delete=False
    ) as tmp:
        tmp.write(codigo_fonte)
        tmp_path = tmp.name

    try:
        return subprocess.run(
            [sys.executable, str(MAIN_FILE), tmp_path],
            text=True,
            encoding="utf-8",
            capture_output=True,
            cwd=ROOT,
            env=ambiente,
            check=False,
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)


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


def test_funcoes_nativas_input_e_console_log_seguem_especificacao() -> None:
    analyze_source(
        """
function void main() {
    let int idade;
    let real altura;
    let str nome;
    input(idade, altura, nome);
    console.log();
    console.log("dados", nome, idade + 1, altura);
}
"""
    )


def test_input_requer_variaveis_numericas_ou_string() -> None:
    assert_semantic_error(
        """
function void main() {
    let int idade;
    input(idade + 1);
}
""",
        "lado esquerdo da atribuicao deve ser atribuivel",
    )
    assert_semantic_error(
        """
function void main() {
    const int idade = 1;
    input(idade);
}
""",
        "constante 'idade' nao pode ser alterada",
    )
    assert_semantic_error(
        """
function void main() {
    let bool ativo;
    input(ativo);
}
""",
        "input aceita apenas variaveis int, real ou str",
    )


def test_input_requer_lista_nao_vazia() -> None:
    assert_semantic_error(
        """
function void main() {
    input();
}
""",
        "input requer ao menos uma variavel",
    )


def test_comandos_de_controle_exigem_condicao_bool() -> None:
    analyze_source(
        """
function void main() {
    let int x = 1;
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
}
"""
    )
    assert_semantic_error(
        """
function void main() {
    if (1) {
        console.log();
    }
}
""",
        "condicao deve ser bool",
    )
    assert_semantic_error(
        """
function void main() {
    while ("sim") {
        break;
    }
}
""",
        "condicao deve ser bool",
    )
    assert_semantic_error(
        """
function void main() {
    let int x = 0;
    for (x = 0; x; x += 1) {
        break;
    }
}
""",
        "condicao deve ser bool",
    )


def test_for_aceita_declaracao_let_no_inicializador() -> None:
    analyze_source(
        """
function void main() {
    for (let int i = 0; i < 5; i = i + 1) {
        console.log(i);
    }
}
"""
    )


def test_operadores_aritmeticos_aplicam_conversoes_da_especificacao() -> None:
    analyze_source(
        """
function void main() {
    let real soma = 1 + 2.5;
    let real subtracao = 10.0 - 2;
    let real multiplicacao = 2 * 3.5;
    let real divisao = 5 / 2.0;
    let int resto = 5 % 2;
    let int potencia = 2 ** 3;
    let str texto = "valor=" + 10 + true;
}
"""
    )


def test_operadores_percentual_e_exponenciacao_exigem_int() -> None:
    assert_semantic_error(
        """
function void main() {
    let real x = 5.0 % 2.0;
}
""",
        "operacao requer int",
    )
    assert_semantic_error(
        """
function void main() {
    let real x = 2.0 ** 3.0;
}
""",
        "operacao requer int",
    )


def test_atribuicao_composta_respeita_tipo_do_destino() -> None:
    analyze_source(
        """
function void main() {
    let real total = 1.0;
    total += 2;
    let str texto = "valor=";
    texto += 10;
}
"""
    )
    assert_semantic_error(
        """
function void main() {
    let int total = 1;
    total += 2.5;
}
""",
        "tipo incompativel: esperado int, recebido real",
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


def test_rejeita_conversao_implicita_em_atribuicao_simples() -> None:
    assert_semantic_error(
        "let real x = 1;",
        "tipo incompativel: esperado real, recebido int",
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
