"""Definições de tokens reconhecidos pelo analisador léxico."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    EOF = auto()

    IDENTIFIER = auto()
    INTEGER_LITERAL = auto()
    REAL_LITERAL = auto()
    STRING_LITERAL = auto()

    LET = auto()
    CONST = auto()
    FUNCTION = auto()
    VOID = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    BREAK = auto()
    RETURN = auto()
    CLASS = auto()
    CONSTRUCTOR = auto()
    NEW = auto()
    THIS = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()

    INPUT = auto()

    TYPE_INT = auto()
    TYPE_REAL = auto()
    TYPE_STR = auto()
    TYPE_BOOL = auto()

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()

    ASSIGN = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    POWER = auto()

    EQUAL_EQUAL = auto()
    BANG_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    BANG = auto()
    AND_AND = auto()
    OR_OR = auto()
    PLUS_PLUS = auto()
    MINUS_MINUS = auto()

    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    STAR_ASSIGN = auto()
    SLASH_ASSIGN = auto()
    PERCENT_ASSIGN = auto()
    POWER_ASSIGN = auto()


@dataclass(frozen=True, slots=True)
class Token:
    type: TokenType
    lexeme: str
    line: int
    column: int
