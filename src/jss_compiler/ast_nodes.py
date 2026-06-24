"""Nos da arvore sintatica abstrata (AST) da linguagem JSS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .tokens import Token


@dataclass(slots=True)
class Node:
    line: int
    column: int


@dataclass(slots=True)
class Symbol:
    name: str
    category: str
    type_name: str | None
    scope: str
    line: int
    column: int


@dataclass(slots=True)
class Program(Node):
    declarations: list[Node]
    symbols: list[Symbol] = field(default_factory=list)


@dataclass(slots=True)
class TypeNode(Node):
    name: str
    is_array: bool = False
    array_size: Node | None = None
    array_size2: Node | None = None


@dataclass(slots=True)
class Declarator(Node):
    name: str
    initializer: Node | None = None
    array_size: Node | None = None
    array_values: list[Node] = field(default_factory=list)


@dataclass(slots=True)
class VarDeclaration(Node):
    type_node: TypeNode
    declarators: list[Declarator]
    constant: bool = False


@dataclass(slots=True)
class Parameter(Node):
    type_node: TypeNode
    name: str


@dataclass(slots=True)
class FunctionDeclaration(Node):
    return_type: TypeNode
    name: str
    params: list[Parameter]
    body: "Block"


@dataclass(slots=True)
class ClassDeclaration(Node):
    name: str
    members: list[Node]


@dataclass(slots=True)
class ConstructorDeclaration(Node):
    class_name: str
    params: list[Parameter]
    body: "Block"


@dataclass(slots=True)
class MethodDeclaration(Node):
    return_type: TypeNode
    name: str
    params: list[Parameter]
    body: "Block"


@dataclass(slots=True)
class AttributeDeclaration(Node):
    type_node: TypeNode
    name: str


@dataclass(slots=True)
class Block(Node):
    statements: list[Node]


@dataclass(slots=True)
class IfStatement(Node):
    condition: Node
    then_branch: Block
    else_branch: Block | "IfStatement" | None = None


@dataclass(slots=True)
class WhileStatement(Node):
    condition: Node
    body: Block


@dataclass(slots=True)
class ForStatement(Node):
    initializer: Node | None
    condition: Node | None
    increment: Node | None
    body: Block


@dataclass(slots=True)
class ReturnStatement(Node):
    value: Node | None = None


@dataclass(slots=True)
class BreakStatement(Node):
    pass


@dataclass(slots=True)
class ExpressionStatement(Node):
    expression: Node


@dataclass(slots=True)
class Assignment(Node):
    target: Node
    operator: Token
    value: Node


@dataclass(slots=True)
class BinaryOperation(Node):
    left: Node
    operator: Token
    right: Node


@dataclass(slots=True)
class UnaryOperation(Node):
    operator: Token
    operand: Node


@dataclass(slots=True)
class Call(Node):
    callee: Node
    arguments: list[Node]
    native: bool = False


@dataclass(slots=True)
class IndexAccess(Node):
    collection: Node
    index: Node


@dataclass(slots=True)
class AttributeAccess(Node):
    object_expr: Node
    attribute: str


@dataclass(slots=True)
class NewObject(Node):
    class_name: str
    arguments: list[Node]


@dataclass(slots=True)
class Literal(Node):
    value: Any
    literal_type: str


@dataclass(slots=True)
class Identifier(Node):
    name: str


@dataclass(slots=True)
class This(Node):
    pass
