"""Nós da árvore sintática abstrata (AST).

Os nós serão adicionados conforme a gramática for implementada.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Program:
    declarations: list[object]
