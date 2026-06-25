# JSS Compiler — Estrutura do Projeto

Compilador da linguagem **JSS (Java Script Simplificado)** implementado em Python.

## Pipeline (`frontend.py`)

```
código-fonte → Lexer → JSSTokenSource → ANTLR Parser → ASTBuilder → SemanticAnalyzer
```

1. `Lexer.tokenize()` — gera lista de `Token`
2. `JSSTokenSource` — adapta tokens JSS para o stream ANTLR4
3. `JSSParser` (gerado de `JSS.g4`) — constrói árvore de parse
4. `ASTBuilder` — visita a árvore ANTLR e produz nós de `ast_nodes.py`
5. `analyze_semantics()` — valida semântica sobre a AST

---

## Léxico (`lexer.py`, `tokens.py`)

**Arquivo:** `src/jss_compiler/lexer.py`

- Classe `Lexer` — analisador léxico manual (sem gerador)
- Método principal: `tokenize() -> list[Token]`
- Ignora espaços, tabs, `\n`, e comentários `//`
- Reconhece tokens na ordem: 3 chars → 2 chars → 1 char

**Tokens especiais:**
- `console.log` tratado como único token (`CONSOLE_LOG`)
- Literais numéricos: inteiro, real com `.`, notação científica `e/E`
- Strings com escapes válidos: `\n \t \r \" \\`
- Identificadores: `[a-zA-Z_][a-zA-Z_0-9]*`

**Palavras-chave:** `let const function void if else while for break return class constructor new this true false null input`

**Tipos primitivos:** `int real str bool`

**Erros léxicos:** caractere inválido, string não terminada, expoente inválido, identificador iniciado por número.

---

## Gramática (`JSS.g4`) — usada pelo ANTLR

**Arquivo:** `src/jss_compiler/JSS.g4`

Gramática formal ANTLR4 que documenta a sintaxe e gera o parser.

**Estrutura:**
- `program` → `declaration*`
- `declaration` → `varDecl | constDecl | functionDecl | classDecl | exprStmt`
- `varDecl` → `let type arrayDim? declarator+;`
- `functionDecl` → `function returnType IDENTIFIER parameters block`
- `classDecl` → `class IDENTIFIER { classMember* }`
- `classMember` → construtor | método | atributo

**Hierarquia de expressões (maior→menor precedência):**
```
assignment → logicalOr → logicalAnd → equalityRel → addition
          → multiplication → exponentiation → unary → postfix → primary
```

**Postfix:** chamada `f()`, acesso por índice `a[i]`, acesso a atributo `obj.campo`

---

## Parser (`parser.py`)

**Arquivo:** `src/jss_compiler/parser.py`

- Descida recursiva manual sobre a lista de `Token`
- Coleta erros sem parar (recuperação por sincronização em `SYNCHRONIZATION_TOKENS`)
- Produz nós de `ast_nodes.py` e tabela de símbolos (`list[Symbol]`)

---

## AST (`ast_nodes.py`)

**Arquivo:** `src/jss_compiler/ast_nodes.py`

Nós como dataclasses: `Program`, `VarDeclaration`, `FunctionDeclaration`, `ClassDeclaration`, `IfStatement`, `WhileStatement`, `ForStatement`, `ReturnStatement`, `BreakStatement`, `BinaryOperation`, `UnaryOperation`, `Assignment`, `Call`, `IndexAccess`, `AttributeAccess`, `NewObject`, `Literal`, `Identifier`, `This`.

---

## Análise Semântica (`semantic.py`)

**Arquivo:** `src/jss_compiler/semantic.py`

- Classe `SemanticAnalyzer` com pilha de escopos (`Scope` com `parent`)
- **Fase 1** — pré-declara classes e funções globais antes de analisar corpos
- **Fase 2** — visita cada declaração verificando:
  - Variável/constante: redeclaração, atribuição a `const`, tipo compatível
  - Função: parâmetros únicos, tipo de retorno, `main` sem parâmetros
  - Classe: atributos, métodos, construtor
  - Expressões: tipos de operandos, chamadas (aridade e tipo), `break` fora de loop

**Tipos:** `TypeInfo(name, is_array, ndim)` — suporte a arrays 1D e 2D

---

## Erros (`errors.py`)

| Classe | Fase |
|---|---|
| `LexicalError` | Léxico |
| `SyntaxErrorJSS` | Sintático |
| `SemanticError` | Semântico |

Todas herdam de `JSSCompilerError(Exception)` e incluem linha e coluna.


---

## Erros Léxicos (`LexicalError`)

Gerados em `lexer.py` ao encontrar sequências inválidas no código-fonte.

| Situação | Exemplo |
|---|---|
| Caractere não pertence à linguagem | `10 @ 2` → `@` inválido |
| String sem fechar (EOF antes de `"`) | `"texto` |
| String com quebra de linha interna | `"abc\ndef"` com `\n` literal |
| Sequência de escape inválida | `"\q"` |
| Expoente sem dígito após `e/E` | `1e+` |
| Identificador iniciado por dígito | `3abc` |

---

## Erros Sintáticos (`SyntaxErrorJSS`)

Gerados pelo parser ANTLR (`JSS.g4`) quando a sequência de tokens não forma uma construção válida.

| Situação | Exemplo |
|---|---|
| `;` faltando ao final de statement | `return x + y` sem `;` |
| `}` inesperado (bloco mal formado) | fechar bloco sem abrir |
| Falta de `(` ou `)` em condição | `if x > 0 { }` |
| Token inesperado em declaração | `let int = 5;` (sem nome) |
| Falta de `{` ou `}` em bloco | `function void f() return;` |
| Operador sem operando | `let int x = * 2;` |

---

## Erros Semânticos (`SemanticError`)

Gerados em `semantic.py` após a AST ser construída com sucesso.

| Situação | Exemplo |
|---|---|
| Redeclaração no mesmo escopo | `let int x; let int x;` |
| Variável não declarada | `x = 10;` sem `let` antes |
| Atribuição a constante | `const int N = 5; N = 6;` |
| Tipos incompatíveis em atribuição | `let int x = "texto";` |
| Operação entre tipos distintos | `1 + "a"` |
| `break` fora de `while`/`for` | `break;` no corpo de função |
| `return` com tipo errado | função `int` retornando `str` |
| `main` declarada com parâmetros | `function void main(int x)` |
| `input` com variável `bool` ou vetor | `input(v)` onde `v` é `bool` |
| Cast com aridade errada | `int(1, 2)` |
| Chamada com número errado de args | `f(1)` onde `f` não tem parâmetros |
| `this` fora de classe | `this.x = 1;` em função global |
| `new` para classe não declarada | `new Foo()` sem `class Foo` |
| Classe sem atributos | `class A { A constructor() {} }` |
| Classe sem construtor | `class A { int x; }` |

## INput e Console.log()
sao palavras reservadas.'

#AINDA VAI SER IMPLEMENTADO
V. Curto-circuito (&&, ||) — NÃO implementado ❌
O analisador semântico apenas verifica o tipo dos dois operandos de && e ||, sem nenhuma lógica de avaliação em tempo de execução:

Curto-circuito é um comportamento de execução — o segundo operando não é avaliado em runtime. Como o compilador só tem front-end (sem interpretador ou gerador de código), essa regra não pode ser implementada ainda. Ela só existirá quando houver geração de código intermediário (ex: salto condicional no bytecode).


!!DIVERGENCIA 
1. || — a tabela diz "tipos aplicados: todos", mas o código exige bool nos dois lados. Provavelmente a tabela está errada aqui, já que || sendo lógico faz mais sentido exigir bool.
2. == != — a tabela diz "tipos aplicados: booleano", mas o código aceita int==int, str==str, etc. Provavelmente a tabela quis dizer que o retorno é bool, não que só aceita bool como entrada.
3. = — tabela diz "tipos aplicados: booleano", claramente um erro de formatação — atribuição funciona para todos os tipos.