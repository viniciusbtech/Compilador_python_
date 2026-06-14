"""Utilitario para visualizar a AST produzida pelo parser."""

from __future__ import annotations

import json
import sys
from dataclasses import fields, is_dataclass
from enum import Enum
from typing import Any

from .errors import JSSCompilerError
from .lexer import Lexer
from .parser import Parser
from .tokens import Token


def ast_to_dict(value: Any) -> Any:
    if isinstance(value, Token):
        return {
            "type": value.type.name,
            "lexeme": value.lexeme,
            "line": value.line,
            "column": value.column,
        }
    if isinstance(value, Enum):
        return value.name
    if is_dataclass(value):
        result = {"node": type(value).__name__}
        for field in fields(value):
            result[field.name] = ast_to_dict(getattr(value, field.name))
        return result
    if isinstance(value, list):
        return [ast_to_dict(item) for item in value]
    return value


def main() -> int:
    source = sys.stdin.read()
    if not source:
        print("Erro: nenhum codigo JSS foi recebido pela entrada padrao.", file=sys.stderr)
        return 1

    try:
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
    except JSSCompilerError as error:
        print(error, file=sys.stderr)
        return 1

    print(json.dumps(ast_to_dict(ast), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
