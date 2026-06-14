"""Analisador sintático da linguagem JSS.

A gramática será implementada de forma incremental, começando por
declarações, comandos, blocos e expressões.
"""

from __future__ import annotations

from .tokens import Token


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens

    def parse(self) -> None:
        """Valida se a sequência de tokens pertence à gramática JSS."""
        # TODO: implementar a gramática da linguagem.
        return None
