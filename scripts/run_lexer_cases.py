"""Executa casos manuais do lexer e compara com as respostas esperadas."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
CASES_DIR = ROOT / "examples" / "bateria_lexer"

sys.path.insert(0, str(SRC))

from jss_compiler.errors import LexicalError  # noqa: E402
from jss_compiler.lexer import Lexer  # noqa: E402


def format_result(source: str) -> str:
    try:
        tokens = Lexer(source).tokenize()
    except LexicalError as error:
        return f"ERRO: {error}\n"

    lines = [
        f"{token.line}:{token.column} {token.type.name} {token.lexeme!r}"
        for token in tokens
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    source_files = sorted(CASES_DIR.glob("*.jss"))
    if not source_files:
        print(f"Nenhum caso encontrado em {CASES_DIR}")
        return 1

    failures = 0
    print("BATERIA MANUAL DO LEXER JSS")
    print("=" * 60)

    for source_file in source_files:
        expected_file = source_file.with_suffix(".expected.txt")
        if not expected_file.exists():
            print(f"[FALHOU] {source_file.name}: resposta esperada ausente")
            failures += 1
            continue

        actual = format_result(source_file.read_text(encoding="utf-8"))
        expected = expected_file.read_text(encoding="utf-8")

        if actual == expected:
            print(f"[OK]     {source_file.name}")
            continue

        failures += 1
        print(f"[FALHOU] {source_file.name}")
        print("  Esperado:")
        for line in expected.rstrip().splitlines():
            print(f"    {line}")
        print("  Obtido:")
        for line in actual.rstrip().splitlines():
            print(f"    {line}")

    print("-" * 60)
    passed = len(source_files) - failures
    print(f"Resultado: {passed}/{len(source_files)} casos passaram.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
