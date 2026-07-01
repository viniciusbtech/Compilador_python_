# Explicacao do back-end: questoes 3.2.a e 3.2.b

Este arquivo serve como material de estudo e tambem como base para explicar ao professor como foi feita a parte de back-end do compilador JSS.

O objetivo das questoes 3.2.a e 3.2.b e mostrar duas coisas principais:

1. Como a arvore sintatica/AST validada e traduzida para uma linguagem intermediaria.
2. Como essa linguagem intermediaria vira um executavel do sistema operacional.

No projeto, a linguagem intermediaria escolhida foi LLVM IR, e o executavel final e gerado com clang.

---

## 1. Estrutura geral do compilador

O compilador segue um fluxo classico:

```text
arquivo.jss
   -> lexer
   -> parser
   -> parse tree
   -> AST
   -> analise semantica
   -> LLVM IR (.ll)
   -> clang
   -> executavel (.exe)
```

A primeira parte e o front-end. Ela le o codigo fonte em JSS, verifica se os tokens, a sintaxe e a semantica estao corretos, e entrega uma AST pronta para o back-end.

A segunda parte e o back-end. Ela pega a AST ja validada e gera codigo LLVM IR. Depois, o clang pega esse arquivo `.ll` e gera o executavel nativo do Windows.

---

## 2. Ferramentas usadas em cada etapa

### Lexer

Arquivo principal:

```text
src/jss_compiler/lexer.py
```

O lexer faz a analise lexica. Ele le o codigo caractere por caractere e transforma em tokens, como identificadores, numeros, strings, palavras reservadas, operadores e simbolos.

Exemplo:

```jss
let int x = 10;
```

Vira uma sequencia de tokens parecida com:

```text
LET, INT, IDENTIFIER(x), ASSIGN, INT_LITERAL(10), SEMICOLON
```

### Parser ANTLR

Arquivos principais:

```text
src/jss_compiler/JSS.g4
src/jss_compiler/antlr_generated/JSSParser.py
```

O parser usa a gramatica da linguagem para verificar se a ordem dos tokens faz sentido. Nessa etapa e gerada a parse tree, que ainda e uma arvore muito ligada as regras da gramatica.

### AST Builder

Arquivo principal:

```text
src/jss_compiler/ast_builder.py
```

O AST Builder percorre a parse tree gerada pelo ANTLR e monta uma AST mais limpa, usando os nos definidos em:

```text
src/jss_compiler/ast_nodes.py
```

A AST e melhor para o back-end porque representa diretamente os conceitos da linguagem, como:

- declaracao de variavel;
- funcao;
- classe;
- bloco;
- if;
- while;
- for;
- atribuicao;
- chamada de funcao;
- expressao binaria;
- acesso a array;
- acesso a atributo.

### Analise semantica

Arquivo principal:

```text
src/jss_compiler/semantic.py
```

A analise semantica verifica regras que nao dependem so da sintaxe. Por exemplo:

- se uma variavel foi declarada antes de ser usada;
- se os tipos sao compativeis;
- se uma funcao existe;
- se os argumentos de uma chamada batem com os parametros;
- se um atributo existe dentro de uma classe;
- se `break` aparece dentro de laco;
- se retornos combinam com o tipo da funcao.

Essa etapa tambem monta tabelas de simbolos e escopos. O gerador LLVM usa essas informacoes para saber o tipo de cada nome e onde cada variavel deve ser encontrada.

### Gerador LLVM

Arquivo principal:

```text
src/jss_compiler/llvm_generator.py
```

Essa e a parte central do back-end. O gerador recebe:

```text
AST + SemanticAnalyzer
```

e produz:

```text
LLVM IR em texto
```

O projeto usa a biblioteca `llvmlite` para montar o LLVM IR por API, em vez de escrever todas as instrucoes manualmente por concatenacao de strings.

### Clang

Ferramenta externa:

```text
clang
```

O clang recebe o arquivo `.ll` gerado pelo compilador e transforma em executavel nativo:

```powershell
clang arquivo.ll -o arquivo.exe
```

No Windows, o projeto tambem adiciona a flag:

```text
-llegacy_stdio_definitions
```

Isso ajuda na ligacao com funcoes da runtime C usadas no LLVM IR, como `printf`, `scanf`, `malloc`, `sprintf`, `strlen`, `strcpy` e `strcat`.

---

## 3. Papel do back-end

O back-end nao deve mais decidir se o programa esta correto do ponto de vista da linguagem. Essa decisao ja foi feita pelo lexer, parser e analisador semantico.

O papel principal do back-end e traduzir a AST validada para uma forma executavel.

No nosso caso:

```text
AST validada -> LLVM IR -> executavel .exe
```

O LLVM IR funciona como uma linguagem intermediaria. Ele e mais baixo nivel que JSS, mas ainda nao e codigo de maquina final. Ele usa instrucoes parecidas com uma maquina de registradores, como `load`, `store`, `add`, `call`, `br` e `ret`.

---

## 4. Regras principais de traducao da AST para LLVM IR

### Tipos

Os tipos da linguagem JSS sao convertidos para tipos LLVM:

| Tipo JSS | Tipo LLVM IR | Uso |
|---|---|---|
| `int` | `i32` | inteiro de 32 bits |
| `real` | `double` | numero real de 64 bits |
| `bool` | `i1` | booleano, 0 ou 1 |
| `str` | `i8*` | ponteiro para caractere |
| `void` | `void` | retorno sem valor |
| classe | `%NomeClasse*` | ponteiro para struct |
| array | `[N x tipo]` | array estatico |

Exemplo:

```jss
let int x = 10;
```

Pode virar uma variavel LLVM do tipo `i32`.

### Variaveis globais e locais

Variaveis globais sao criadas como `GlobalVariable` no modulo LLVM.

Exemplo conceitual:

```jss
let int x = 0;
```

Vira algo parecido com:

```llvm
@x = internal global i32 0
```

Variaveis locais sao alocadas dentro da funcao com `alloca`. Depois, os valores sao gravados com `store` e lidos com `load`.

Fluxo geral:

```text
declarar variavel local -> alloca
atribuir valor -> store
usar valor -> load
```

### Expressoes aritmeticas

As expressoes da AST viram instrucoes LLVM.

| Operacao JSS | Inteiro LLVM | Real LLVM |
|---|---|---|
| `a + b` | `add` | `fadd` |
| `a - b` | `sub` | `fsub` |
| `a * b` | `mul` | `fmul` |
| `a / b` | `sdiv` | `fdiv` |
| `a % b` | `srem` | nao usado para real |

Se uma operacao mistura `int` e `real`, o `int` e convertido para `real` com `sitofp`.

Exemplo:

```jss
let real x = 2 + 3.5;
```

O `2` precisa ser convertido para `double` antes da soma.

### Comparacoes e booleanos

Comparacoes entre inteiros usam `icmp`.

Comparacoes entre reais usam `fcmp`.

Exemplos:

| JSS | LLVM |
|---|---|
| `a == b` | `icmp eq` ou `fcmp oeq` |
| `a != b` | `icmp ne` ou `fcmp one` |
| `a > b` | `icmp sgt` ou `fcmp ogt` |
| `a < b` | `icmp slt` ou `fcmp olt` |

O resultado de uma comparacao e sempre `bool`, ou seja, `i1` no LLVM.

### Atribuicoes

A atribuicao simples:

```jss
x = 10;
```

gera um valor e depois grava esse valor no endereco da variavel com `store`.

As atribuicoes compostas tambem sao tratadas:

```jss
x += 2;
x -= 2;
x *= 2;
x /= 2;
x %= 2;
```

O gerador primeiro carrega o valor atual de `x`, aplica a operacao e grava o novo valor de volta.

### If e else

Um `if` vira blocos basicos LLVM com saltos.

Estrutura conceitual:

```text
avaliar condicao
br i1 condicao, label if_then, label if_else

if_then:
   comandos do then
   br label if_merge

if_else:
   comandos do else
   br label if_merge

if_merge:
   continua o programa
```

Ou seja, o controle de fluxo da linguagem vira labels e instrucoes `br`.

### While

Um `while` vira tres regioes principais:

```text
while_cond
while_body
while_end
```

O compilador gera um salto para a condicao, testa o valor booleano e decide se entra no corpo ou se sai do laco.

O comando `break` dentro do while salta diretamente para o bloco final do laco.

### For

O `for` tambem e traduzido para blocos:

```text
inicializacao
for_cond
for_body
incremento
for_end
```

A inicializacao roda uma vez. A condicao e testada antes de cada repeticao. O incremento roda no fim de cada iteracao.

### Funcoes

Funcoes JSS viram funcoes LLVM.

Exemplo:

```jss
function int soma(int a, int b) {
    return a + b;
}
```

Vira uma funcao LLVM conceitualmente parecida com:

```llvm
define i32 @soma(i32 %a_arg, i32 %b_arg) {
entry:
  ...
  ret i32 %resultado
}
```

Os parametros sao armazenados em variaveis locais com `alloca + store`. Isso facilita reatribuicao de parametro dentro da funcao.

### Main do usuario e main real do executavel

O sistema operacional espera uma funcao de entrada chamada `main`.

No projeto, se o usuario cria:

```jss
function void main() {
    ...
}
```

essa funcao e renomeada internamente para:

```text
__jss_user_main
```

Depois o compilador gera uma `main` real em LLVM. Essa `main` real chama a inicializacao global e depois chama a main do usuario.

Fluxo:

```text
@main real
   -> SetConsoleOutputCP(65001)
   -> __jss_global_init, se existir
   -> __jss_user_main, se existir
   -> ret i32 0
```

Isso permite que o executavel tenha sempre uma entrada valida para o clang e para o sistema operacional.

### Comandos globais

Se existirem comandos soltos fora de funcao, eles sao colocados em uma funcao auxiliar:

```text
__jss_global_init
```

Essa funcao e chamada pela `main` real antes da main do usuario.

Isso resolve o problema de programas que tem comandos no escopo global.

### Classes

Classes JSS sao representadas como structs no LLVM.

Exemplo:

```jss
class Ponto {
    int x;
    int y;
}
```

Vira algo conceitual como:

```llvm
%Ponto = type { i32, i32 }
```

Cada atributo vira um campo da struct, na ordem em que foi declarado.

Metodos viram funcoes com nome qualificado, como:

```text
Ponto.metodo
```

O objeto atual e passado como primeiro parametro, parecido com um `self`.

### Construtores e new

O `new` chama uma funcao construtora.

Exemplo:

```jss
let Ponto p = new Ponto(1, 2);
```

O gerador cria uma chamada para:

```text
Ponto.constructor
```

O construtor aloca memoria usando `malloc`, converte o ponteiro bruto para ponteiro da struct e inicializa os atributos.

### Acesso a atributos

O acesso:

```jss
p.x
```

vira um calculo de endereco com `getelementptr`. O gerador descobre qual e o indice do atributo `x` dentro da struct e acessa o campo correto.

### Arrays

Arrays sao representados como arrays LLVM.

O acesso:

```jss
arr[i]
```

vira:

```text
calcular endereco do elemento com getelementptr
ler com load ou escrever com store
```

Para matrizes, o gerador junta os indices e tambem usa `getelementptr`.

### Strings

Strings em JSS sao representadas como `i8*`.

Literais de string viram constantes globais terminadas com byte zero, como em C.

Exemplo:

```jss
"Ola"
```

vira uma constante global com conteudo equivalente a:

```text
Ola\0
```

Concatenacao de strings pode ser resolvida de duas formas:

- se os dois lados sao literais, o compilador pode juntar em tempo de compilacao;
- se envolve variaveis, o compilador gera chamadas de runtime, como `malloc`, `strcpy` e `strcat`.

### console.log

O `console.log` e implementado usando `printf`.

O gerador avalia os argumentos, monta uma string de formato e chama `printf`.

Exemplo:

```jss
console.log("Soma:", x);
```

vira uma chamada conceitual:

```llvm
call i32 (i8*, ...) @printf(i8* formato, i8* texto, i32 valor)
```

Booleanos sao convertidos para as strings `"true"` ou `"false"` antes da impressao.

### input

O `input` e implementado usando `scanf`.

Para numeros e booleanos, o compilador passa o endereco da variavel.

Para strings, ele primeiro aloca um buffer com `malloc`, guarda esse ponteiro na variavel e depois passa o buffer para `scanf`.

Fluxo para string:

```text
malloc(256)
store ponteiro na variavel
scanf("%s", ponteiro)
```

### Casts

Casts nativos como `int`, `real`, `bool` e `str` sao traduzidos para instrucoes LLVM ou chamadas auxiliares.

Exemplos:

| Conversao | Implementacao |
|---|---|
| `int -> real` | `sitofp` |
| `real -> int` | `fptosi` |
| `bool -> int` | `zext` |
| `int -> bool` | comparacao com zero |
| `valor -> str` | `sprintf` em buffer alocado |

---

## 5. Geracao do arquivo LLVM IR

O arquivo `.ll` e gerado pela funcao:

```text
generate_llvm(program, analyzer)
```

Essa funcao cria um `LLVMGenerator`, percorre a AST e retorna o modulo LLVM em formato texto.

No CLI, esse texto e salvo no mesmo caminho do arquivo fonte, trocando a extensao para `.ll`.

Exemplo:

```powershell
python .\main.py .\examples\teste1.jss
```

gera:

```text
examples/teste1.ll
```

---

## 6. Geracao do executavel

Depois de gerar o LLVM IR, o compilador chama o clang.

No codigo, isso aparece na funcao:

```text
_build_executable(ir_path, exe_path)
```

Arquivo:

```text
src/jss_compiler/cli.py
```

O comando principal e:

```powershell
clang arquivo.ll -o arquivo.exe
```

No Windows, o projeto usa:

```powershell
clang arquivo.ll -o arquivo.exe -llegacy_stdio_definitions
```

O clang faz as etapas finais:

1. Le o LLVM IR.
2. Gera codigo de maquina para a arquitetura do sistema.
3. Faz a ligacao com a runtime C.
4. Produz o arquivo `.exe`.

Fluxo final:

```text
arquivo.jss
   -> arquivo.ll
   -> arquivo.exe
```

---

## 7. Modos de execucao do compilador

O compilador aceita dois modos principais.

### Build

Gera o `.ll` e o `.exe`, mas nao executa o programa:

```powershell
python .\main.py --build .\examples\teste1.jss
```

Tambem funciona sem escrever `--build`, porque esse e o comportamento padrao:

```powershell
python .\main.py .\examples\teste1.jss
```

Resultado esperado:

```text
examples/teste1.ll
examples/teste1.exe
```

Depois, o executavel pode ser chamado manualmente:

```powershell
.\examples\teste1.exe
```

### Run

Gera o `.ll`, gera um executavel temporario e ja executa:

```powershell
python .\main.py --run .\examples\teste1.jss
```

Esse modo e util para testar rapidamente o programa final.

---

## 8. Dependencias importantes

Para a parte Python:

```text
antlr4-python3-runtime
llvmlite
```

Para testes:

```text
pytest
```

Para gerar executavel:

```text
clang
```

O clang precisa estar instalado e disponivel no `PATH`. Se nao estiver, o compilador consegue chegar ate o `.ll`, mas falha ao criar o `.exe`.

Erro esperado nesse caso:

```text
Erro: clang nao encontrado no PATH. Nao foi possivel gerar o executavel.
```

---

## 9. Resposta resumida para apresentar ao professor

Na questao 3.2.a, o compilador traduz a AST validada para LLVM IR. A traducao e feita no arquivo `llvm_generator.py`, usando `llvmlite`. Cada no importante da AST possui uma regra de traducao: variaveis viram `alloca`, `store` e `load`; expressoes aritmeticas viram instrucoes como `add`, `sub`, `mul`, `sdiv`, `fadd` e `fdiv`; estruturas de controle viram blocos basicos e saltos com `br`; funcoes viram `define`; chamadas viram `call`; classes viram structs; objetos sao alocados com `malloc`; arrays e atributos usam `getelementptr`; e entrada/saida usam funcoes externas da runtime C, como `printf` e `scanf`.

Na questao 3.2.b, o compilador gera um arquivo `.ll` com LLVM IR e depois chama o clang para gerar o executavel do sistema operacional. No Windows, o resultado final e um arquivo `.exe`. O fluxo e: o arquivo `.jss` passa pelo front-end, gera uma AST valida, o back-end gera `arquivo.ll`, e o clang compila esse `.ll` para `arquivo.exe`. Assim, o projeto demonstra tanto a geracao da linguagem intermediaria quanto a geracao de um executavel real.

---

## 10. O que e mais importante lembrar

- O back-end comeca depois que a AST ja esta validada.
- A linguagem intermediaria escolhida foi LLVM IR.
- O gerador usa `llvmlite`, nao strings soltas.
- O arquivo principal do back-end e `src/jss_compiler/llvm_generator.py`.
- O arquivo principal do build e `src/jss_compiler/cli.py`.
- Variaveis locais usam `alloca`, `store` e `load`.
- Controle de fluxo usa labels e `br`.
- Funcoes usam `define`, `call` e `ret`.
- Classes sao structs.
- Objetos sao alocados com `malloc`.
- `console.log` usa `printf`.
- `input` usa `scanf`.
- O `.ll` vira `.exe` com `clang`.
