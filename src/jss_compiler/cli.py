"""Interface de linha de comando do compilador JSS."""

from __future__ import annotations

import sys

from .errors import JSSCompilerError
from .frontend import analyze_source


def main() -> int:
    """Lê o programa JSS da entrada padrão e executa o front-end."""
    source = sys.stdin.read()

    if not source.strip():
        print("Erro: nenhum programa JSS foi fornecido na entrada padrão.")
        return 1

    try:
        analyze_source(source)
    except JSSCompilerError as error:
        print(error)
        return 1

    print("Programa válido.")
    return 0
