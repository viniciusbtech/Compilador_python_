# Compilador JSS

Compilador academico para a linguagem **JavaScript Simplificado (JSS)**.

O front-end atual executa:

```text
arquivo .jss
   -> lexer
   -> tokens com linha/coluna
   -> parser
   -> AST + tabela de simbolos inicial
```

## Estrutura do projeto

```text
jss-compiler/
|-- main.py
|-- examples/
|-- src/
|   `-- jss_compiler/
|       |-- lexer.py
|       |-- parser.py
|       |-- ast_nodes.py
|       |-- debug_lexer.py
|       |-- debug_parser.py
|       |-- frontend.py
|       |-- tokens.py
|       `-- errors.py
`-- tests/
```

## Ambiente

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
pip install -r requirements-dev.txt
```

Se nao instalar o pacote em modo editavel, defina o `PYTHONPATH` antes de executar:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

## Como executar o compilador

O compilador le o programa JSS pela entrada padrao:

```powershell
Get-Content .\examples\sucesso_minimo.jss -Raw | python .\main.py
```

Saida esperada para um programa lexica e sintaticamente valido:

```text
Programa válido.
```

Para testar outro arquivo:

```powershell
Get-Content .\examples\nome_do_arquivo.jss -Raw | python .\main.py
```

## Como ver os tokens do lexer

```powershell
Get-Content .\examples\sucesso_minimo.jss -Raw | python -m jss_compiler.debug_lexer
```

A saida mostra localizacao, tipo do token e lexema:

```text
LOCAL      TOKEN                  LEXEMA
------------------------------------------------------------
1:1        FUNCTION               'function'
1:10       VOID                   'void'
...
```

## Como ver a saida do parser

Use o utilitario `debug_parser` para imprimir a AST em JSON:

```powershell
Get-Content .\examples\sucesso_minimo.jss -Raw | python -m jss_compiler.debug_parser
```

Esse comando permite conferir se o parser respeitou precedencia, associatividade, blocos, chamadas nativas, vetores, classes e declaracoes.

Exemplo de trecho da AST:

```json
{
  "node": "FunctionDeclaration",
  "return_type": {
    "node": "TypeNode",
    "name": "void"
  },
  "name": "main",
  "params": [],
  "body": {
    "node": "Block"
  }
}
```

Se houver erro sintatico, a mensagem inclui linha e coluna:

```text
Erro sintático na linha 1, coluna 10: esperado ';' apos declaracao
```

## Parser implementado

O parser foi construido em `src/jss_compiler/parser.py` por **descida recursiva top-down**, com uma funcao para cada parte principal da gramatica:

- programa e declaracoes globais;
- declaracoes `let` e `const`;
- funcoes globais;
- classes, atributos, construtores e metodos;
- blocos e comandos;
- `if`, `else if`, `else`, `while`, `for`, `return` e `break`;
- expressoes com precedencia;
- chamadas nativas e casts.

O simbolo inicial e:

```text
Programa -> DeclaracaoGlobal*
```

Declaracoes globais aceitas:

```text
let Tipo ...
const Tipo ...
function TipoRetorno id(...)
class id { ... }
```

O parser rejeita funcao declarada dentro de bloco ou funcao, porque funcoes JSS devem ficar no escopo global.

## Precedencia de expressoes

A expressao e separada nos seguintes niveis, do menor para o maior:

```text
Atribuicao
OuLogico
ELogico
IgualdadeRelacional
Soma
Multiplicacao
Exponenciacao
Unario
Primario/Postfix
```

Regras importantes implementadas:

- atribuicao (`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`) e associativa a direita;
- exponenciacao (`**`) e associativa a direita;
- demais operadores binarios sao associativos a esquerda;
- `+` e apenas reconhecido pelo parser; soma numerica ou concatenacao deve ser decidido na analise semantica.

Exemplos:

```text
x = y = 10        -> x = (y = 10)
2 ** 3 ** 2      -> 2 ** (3 ** 2)
1 + 2 * 3        -> 1 + (2 * 3)
```

## AST e tabela de simbolos

Os nos da AST ficam em `src/jss_compiler/ast_nodes.py`.

Principais nos:

- `Program`
- `VarDeclaration`
- `FunctionDeclaration`
- `ClassDeclaration`
- `Block`
- `IfStatement`
- `WhileStatement`
- `ForStatement`
- `ReturnStatement`
- `BreakStatement`
- `Assignment`
- `BinaryOperation`
- `UnaryOperation`
- `Call`
- `IndexAccess`
- `AttributeAccess`
- `NewObject`
- `Literal`
- `Identifier`

O parser tambem monta uma tabela de simbolos inicial em `Program.symbols`, com:

- nome;
- categoria;
- tipo;
- escopo;
- linha e coluna da declaracao.

Essa tabela prepara a etapa de analise semantica. Validacoes como redeclaracao, tipos, `break` fora de laco, retorno incompativel e regras de `const` ainda pertencem a etapa semantica.

## Recursos reconhecidos pelo parser

- `let` e `const`;
- tipos `int`, `real`, `str`, `bool`, `void` como retorno e identificadores de classe;
- funcoes globais;
- classe, atributo, construtor e metodo;
- blocos `{ ... }`;
- `if`, `else if`, `else`;
- `while` e `for`;
- `return` e `break`;
- vetores em declaracao, acesso e inicializacao;
- chamadas de funcao;
- `input(...)`;
- `console.log(...)`;
- casts `int(...)`, `real(...)`, `bool(...)`, `str(...)`;
- `new Classe(...)`;
- `this.atributo`;
- acesso por ponto e por indice.

## Testes

Execute toda a bateria:

```powershell
python -m pytest
```

Executar apenas os testes do parser:

```powershell
python -m pytest tests\test_parser.py -v
```

Executar apenas os testes do lexer:

```powershell
python -m pytest tests\test_lexer.py tests\test_lexer_bateria.py -v
```

## Arquivos uteis para teste manual

Programa valido minimo:

```powershell
Get-Content .\examples\sucesso_minimo.jss -Raw | python .\main.py
Get-Content .\examples\sucesso_minimo.jss -Raw | python -m jss_compiler.debug_parser
```

Erro lexico:

```powershell
Get-Content .\examples\erro_lexico.jss -Raw | python .\main.py
```

Erro sintatico:

```powershell
Get-Content .\examples\erro_sintatico.jss -Raw | python .\main.py
```

## Proximas etapas

1. Implementar analise semantica usando `Program.symbols` e a AST.
2. Validar redeclaracao no mesmo escopo.
3. Validar `main` sem parametros quando existir.
4. Validar tipos de atribuicao, operadores, retorno e chamadas.
5. Validar `break` apenas dentro de `while` ou `for`.
6. Gerar codigo intermediario LLVM IR ou JASMIN percorrendo a AST.
