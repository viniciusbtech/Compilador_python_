"""Interface de linha de comando do compilador JSS."""

from __future__ import annotations

import argparse
import sys

from .errors import JSSCompilerError
from .frontend import analyze_source


def main() -> int:
    """Recebe o caminho do arquivo JSS como argumento e executa o front-end."""
    parser = argparse.ArgumentParser(description="Compilador JSS")
    parser.add_argument("arquivo", help="Arquivo fonte .jss a ser compilado")
    args = parser.parse_args()

    try:
        with open(args.arquivo, encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Erro: arquivo '{args.arquivo}' não encontrado.")
        return 1

    if not source.strip():
        print(f"Erro: arquivo '{args.arquivo}' está vazio.")
        return 1

    try:
        analyze_source(source)
    except JSSCompilerError as error:
        print(error)
        return 1

    print("Programa válido.")
    return 0
