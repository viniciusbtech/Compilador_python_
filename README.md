# Compilador JSS

Compilador academico para a linguagem **JavaScript Simplificado (JSS)**.

O front-end atual executa:

```text
arquivo .jss
   -> lexer manual (lexer.py)
   -> tokens com linha/coluna
   -> parser ANTLR4 (gerado de JSS.g4)
   -> AST + tabela de simbolos
   -> analisador semantico
   -> programa validado
```

## Estrutura do projeto

```text
jss-compiler/
|-- main.py
|-- examples/
|-- src/
|   `-- jss_compiler/
|       |-- lexer.py            # lexer manual
|       |-- tokens.py
|       |-- parser.py           # parser manual (usado apenas no debug_parser)
|       |-- ast_nodes.py
|       |-- ast_builder.py      # converte arvore ANTLR -> ast_nodes
|       |-- jss_token_source.py # ponte lexer JSS -> ANTLR
|       |-- antlr_error_listener.py
|       |-- JSS.g4              # gramatica formal ANTLR4
|       |-- antlr_generated/    # codigo gerado pelo ANTLR (nao editar)
|       |-- semantic.py         # analisador semantico
|       |-- frontend.py         # orquestra todas as etapas
|       |-- debug_lexer.py
|       |-- debug_parser.py
|       `-- errors.py
`-- tests/
```

## Ambiente

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
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
Get-Content .\examples\erro_sintatico.jss -Raw | python .\main.py
Get-Content .\examples\erro_lexico.jss -Raw | python .\main.py

#Testes
Get-Content .\examples\teste1.jss -Raw | python .\main.py
Get-Content .\examples\teste2.jss -Raw | python .\main.py
Get-Content .\examples\teste3.jss -Raw | python .\main.py
Get-Content .\examples\teste4.jss -Raw | python .\main.py
Get-Content .\examples\teste5.jss -Raw | python .\main.py

#Testes automatizado
powershell -ExecutionPolicy Bypass -File .\testar_tudo.ps1
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

Erro semantico (redeclaracao de variavel):

```powershell
Get-Content .\examples\erro_sintatico.jss -Raw | python .\main.py
```

Tabela de simbolos (AST em JSON):

```powershell
Get-Content .\examples\sucesso_minimo.jss -Raw | python -m jss_compiler.debug_parser
Get-Content .\examples\teste1.jss -Raw | python -m jss_compiler.debug_parser
```

## Atualizacao: analise semantica

O front-end agora tambem executa a etapa de analise semantica depois do parser:

```text
arquivo .jss
   -> lexer
   -> tokens com linha/coluna
   -> parser
   -> AST + tabela de simbolos inicial
   -> analisador semantico
   -> programa validado semanticamente
```

Novo arquivo principal:

```text
src/jss_compiler/semantic.py
```

O `frontend.py` passou a chamar `analyze_semantics(program)` depois de construir a AST. Assim, `python .\main.py` valida erros lexicos, sintaticos e semanticos no mesmo fluxo.

Regras semanticas implementadas:

- linguagem case-sensitive: nomes com grafias diferentes continuam sendo identificadores distintos;
- proibicao de redeclaracao de `let`, `const`, funcoes e classes no mesmo escopo;
- escopo global, escopo de funcao/metodo/construtor e escopos de bloco para `let` e `const`;
- validacao de tipos primitivos `int`, `real`, `str` e `bool`;
- sem conversoes implicitas: mudanca de tipo exige cast explicito com `int(...)`, `real(...)`, `bool(...)` ou `str(...)`;
- proibicao de mistura de tipos em atribuicoes, operacoes aritmeticas, concatenacao e comparacoes;
- concatenacao com `+` apenas entre operandos `str`;
- operadores logicos e relacionais retornando `bool`, com validacao de operandos;
- casts nativos `int(...)`, `real(...)`, `bool(...)` e `str(...)`;
- vetores homogeneos e inicializacao por lista apenas na declaracao;
- erro ao alterar constante ou elemento de vetor constante;
- comandos de expressao no escopo global, permitindo atribuicoes fora de funcoes;
- validacao de classes com atributos antes de construtores/metodos, ao menos uma variavel e ao menos um construtor;
- validacao de construtor, `this`, atributos, metodos e `new Classe(...)`;
- metodos em classes sao opcionais;
- proibicao de conflito entre nome de funcao e identificadores globais ja declarados;
- `main`, quando declarada, deve ter lista de parametros vazia;
- `break` apenas dentro de `while` ou `for`;
- `return` compativel com o tipo da funcao ou metodo.

As mensagens do CLI agora sao emitidas na saida padrao: confirmacao de sucesso, erro lexico, erro sintatico e erro semantico. Os erros indicam linha e coluna:

```text
Erro semantico na linha 3, coluna 5: constante 'x' nao pode ser alterada
```

Tambem foi adicionada uma bateria especifica:

```powershell
python -m pytest tests\test_semantic.py -v
```

Na estrutura do projeto, considere agora tambem:

```text
jss-compiler/
|-- src/
|   `-- jss_compiler/
|       |-- semantic.py
|       `-- frontend.py  # integra lexer, parser e semantico
`-- tests/
    `-- test_semantic.py
```


## Proximas etapas

1. Gerar codigo intermediario (LLVM IR ou JASMIN) percorrendo a AST.
