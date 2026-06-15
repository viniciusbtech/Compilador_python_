"""Coordena as etapas de análise do front-end."""

from __future__ import annotations

from .lexer import Lexer
from .parser import Parser
from .semantic import analyze_semantics


def analyze_source(source: str) -> None:
    """Executa análise léxica e sintática sobre o código-fonte."""
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    program = parser.parse()
    analyze_semantics(program)
