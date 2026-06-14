"""Utilitário para visualizar os tokens produzidos pelo lexer."""

from __future__ import annotations

import sys

from .errors import LexicalError
from .lexer import Lexer


def main() -> int:
    source = sys.stdin.read()

    if not source:
        print("Erro: nenhum código JSS foi recebido pela entrada padrão.", file=sys.stderr)
        return 1

    try:
        tokens = Lexer(source).tokenize()
    except LexicalError as error:
        print(error, file=sys.stderr)
        return 1

    print(f"{'LOCAL':<10} {'TOKEN':<22} LEXEMA")
    print("-" * 60)

    for token in tokens:
        location = f"{token.line}:{token.column}"
        print(f"{location:<10} {token.type.name:<22} {token.lexeme!r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
