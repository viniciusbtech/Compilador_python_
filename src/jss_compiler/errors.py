"""Exceções padronizadas do compilador JSS."""

from __future__ import annotations


class JSSCompilerError(Exception):
    """Classe-base para erros detectados pelo compilador."""


class LexicalError(JSSCompilerError):
    def __init__(self, message: str, line: int, column: int) -> None:
        super().__init__(f"Erro léxico na linha {line}, coluna {column}: {message}")


class SyntaxErrorJSS(JSSCompilerError):
    def __init__(self, message: str, line: int, column: int) -> None:
        super().__init__(f"Erro sintático na linha {line}, coluna {column}: {message}")


class SemanticError(JSSCompilerError):
    def __init__(self, message: str, line: int, column: int) -> None:
        super().__init__(f"Erro semântico na linha {line}, coluna {column}: {message}")
