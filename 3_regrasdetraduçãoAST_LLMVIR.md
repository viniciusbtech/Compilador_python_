# Regras de Tradução: AST → LLVM IR

---

## 1. Tipos

| JSS        | LLVM IR        | Descrição                        |
|------------|----------------|----------------------------------|
| `int`      | `i32`          | Inteiro 32 bits com sinal        |
| `real`     | `double`       | Ponto flutuante 64 bits          |
| `bool`     | `i1`           | Inteiro de 1 bit (0 ou 1)        |
| `str`      | `i8*`          | Ponteiro para array de bytes     |
| `void`     | `void`         | Só em retorno de função          |
| `NomeClasse` | `%NomeClasse*` | Ponteiro para struct            |
| `int[]`    | `[0 x i32]*`   | Ponteiro para array de i32       |

---

## 2. Classes → Structs

```
class Ponto { int x; int y; }
  ↓
%Ponto = type { i32, i32 }
```
Cada atributo vira um campo da struct na ordem de declaração.

---

## 3. Variáveis

**Global:** `let int x = 0;` → `@x = internal global i32 0`

**Local:** toda variável local ganha `alloca` no início da função, depois `store` no ponto de atribuição.

**Parâmetros de função:** recebem `alloca + store` imediato para suportar reatribuição.

---

## 4. Funções

```
function int soma(int a, int b) { ... }
  ↓
define i32 @soma(i32 %a_arg, i32 %b_arg) {
entry:
  %a = alloca i32 ; store i32 %a_arg, i32* %a
  %b = alloca i32 ; store i32 %b_arg, i32* %b
  ...
}
```

---

## 5. Expressões Aritméticas e Lógicas

| JSS      | int       | real        |
|----------|-----------|-------------|
| `a + b`  | `add i32` | `fadd double` |
| `a - b`  | `sub i32` | `fsub double` |
| `a * b`  | `mul i32` | `fmul double` |
| `a / b`  | `sdiv i32`| `fdiv double` |
| `a % b`  | `srem i32`| —           |
| `a && b` | `and i1`  | —           |
| `a \|\| b` | `or i1` | —           |

> **Promoção:** se qualquer operando for `real`, o `int` é convertido com `sitofp` antes da operação.

---

## 6. Comparações

| JSS     | int        | real       |
|---------|------------|------------|
| `a == b`| `icmp eq`  | `fcmp oeq` |
| `a != b`| `icmp ne`  | `fcmp one` |
| `a > b` | `icmp sgt` | `fcmp ogt` |
| `a < b` | `icmp slt` | `fcmp olt` |

Resultado sempre `i1`.

---

## 7. Coerção de Tipos

| De   | Para | Instrução LLVM            |
|------|------|---------------------------|
| int  | real | `sitofp i32 %x to double` |
| real | int  | `fptosi double %x to i32` |
| int  | bool | `icmp ne i32 %x, 0`       |
| bool | int  | `zext i1 %x to i32`       |

Aplicada automaticamente em atribuições e chamadas quando os tipos diferem.

---

## 8. Controle de Fluxo

**if/else** → gera labels `if_then`, `if_else`, `if_merge` ligados por `br i1`.

**while** → labels `while_cond`, `while_body`, `while_end`; o `break` salta para `while_end`.

**for** → `init` emitido antes do label `for_cond`; `incr` emitido no fim de `for_body`.

**return** → `ret i32 %val` ou `ret void`.

---

## 9. Chamadas de Função

**Usuário:** `soma(a, b)` → `%t = call i32 @soma(i32 %a_val, i32 %b_val)`

**console.log:** gera chamada a `@printf` com string de formato por tipo (`%d\n`, `%f\n`).

**input:** gera chamada a `@scanf` passando o **ponteiro** da variável (não o valor).

**Casts:** `real(x)` → `sitofp`; `int(y)` → `fptosi`.

---

## 10. Arrays e Objetos

**Acesso a array:** `arr[i]` → `getelementptr` + `load`; atribuição usa `store`.

**Atributo de objeto:** `ponto.x` → `getelementptr` com índice do campo na struct + `load`.

**new:** `new Ponto(1,2)` → `call %Ponto* @Ponto.constructor(...)` que aloca via `malloc`.

**String literal:** `"hello"` → constante global `[6 x i8]`, acesso via `getelementptr`.



- Operadores unários (-x, !b, x++, ++x, x--, --x) e a distinção pré vs pós (pós retorna valor antigo, pré retorna novo) — seção inteira omitida.
- Operadores compostos de atribuição (+=, -=, *=, /=, %=) com a tabela int vs real — reduzi demais.
- Inicialização de array (let int[3] arr = [1,2,3]) que gera um getelementptr + store por elemento — não entrou.
- String literal ficou só mencionada no item 10, sem explicar que vira constante global com \00 no fim.
✻ Churned for 35s

Algumas coisas ficaram de fora ou muito resumidas p

- Operadores unários (-x, !b, x++, ++x, x--, --x) eretorna valor antigo, pré retorna novo) — seçãointeira omitida.
- Operadores compostos de atribuição (+=, -=, *=, /al — reduzi demais.
- Inicialização de array (let int[3] arr = [1,2,3]) que gera um getelementptr + store por elemento — não entrou.
- String literal ficou só mencionada no item 10, se global com \00 no fim.