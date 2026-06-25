"""Coordena as etapas de análise do front-end."""

from __future__ import annotations

from antlr4 import CommonTokenStream  # type: ignore[import-untyped]

from .antlr_error_listener import JSSErrorListener
from .antlr_generated.JSSParser import JSSParser
from .ast_builder import ASTBuilder
from .jss_token_source import JSSTokenSource
from .lexer import Lexer
from .semantic import analyze_semantics


def analyze_source(source: str) -> None:
    """Executa análise léxica (Lexer JSS) + parsing (ANTLR4) + análise semântica."""
    # 1. Tokenização — usa o Lexer JSS existente (trata erros léxicos com mensagens precisas)
    tokens = Lexer(source).tokenize()

    # 2. Ponte: converte a lista de Token JSS em fluxo de tokens ANTLR
    token_source = JSSTokenSource(tokens)
    stream = CommonTokenStream(token_source)

    # 3. Parsing com o parser gerado pelo ANTLR a partir de JSS.g4
    parser = JSSParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(JSSErrorListener())
    tree = parser.program()

    # 4. Constrói a AST nos tipos de ast_nodes.py existentes
    ast = ASTBuilder().visit(tree)

    # 5. Análise semântica — sem mudanças
    analyze_semantics(ast)
