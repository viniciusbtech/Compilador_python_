"""Error listener ANTLR que converte erros de sintaxe no formato JSS."""

from __future__ import annotations

from antlr4.error.ErrorListener import ErrorListener  # type: ignore[import-untyped]

from .errors import RawSyntaxErrorJSS


class JSSErrorListener(ErrorListener):
    """Substitui o listener padrão do ANTLR para produzir erros no padrão JSS."""

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        col = column + 1  # ANTLR usa coluna 0-based; JSS usa 1-based
        text = offending_symbol.text if offending_symbol is not None else "?"
        raise RawSyntaxErrorJSS(
            f"Erro sintático na linha {line}, coluna {col}: token inesperado '{text}'",
            line,
            col,
        )
