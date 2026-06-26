"""Interface de linha de comando do compilador JSS."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .errors import JSSCompilerError
from .frontend import analyze_source
from .llvm_generator import generate_llvm


def main() -> int:
    """Recebe o caminho do arquivo JSS como argumento e gera LLVM IR."""
    parser = argparse.ArgumentParser(description="Compilador JSS")
    parser.add_argument("arquivo", help="Arquivo fonte .jss a ser compilado")
    parser.add_argument(
        "-o", "--output",
        help="Arquivo de saída .ll (padrão: mesmo nome do fonte com extensão .ll)",
        default=None,
    )
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
        ast, analyzer = analyze_source(source)
    except JSSCompilerError as error:
        print(error)
        return 1

    ir = generate_llvm(ast, analyzer)

    output_path = args.output if args.output else Path(args.arquivo).with_suffix(".ll")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ir)
    except OSError as e:
        print(f"Erro ao escrever '{output_path}': {e}")
        return 1

    print(f"LLVM IR gerado: {output_path}")
    return 0
