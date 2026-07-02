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

### Pre-requisitos do sistema

- **Python 3.11+**
- **clang** (LLVM) instalado e disponivel no `PATH`. E usado para compilar o `.ll` gerado em `.exe`.
  Baixe em https://github.com/llvm/llvm-project/releases (instalador `LLVM-*-win64.exe`) e marque
  a opcao "Add LLVM to the system PATH". Confira com:
  ```powershell
  clang --version
  ```
  Sem o clang, o compilador ainda gera o `.ll`, mas falha ao gerar o `.exe`
  (`Erro: clang nao encontrado no PATH`).

O projeto **nao inclui a pasta `.venv/`** (ela e local e ignorada pelo git/`.gitignore`).
Cada pessoa que clonar ou receber o projeto precisa criar o proprio ambiente virtual
seguindo os passos abaixo.

### Criando o ambiente virtual

No Windows PowerShell, na raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pip install -e .
pip install -r requirements-dev.txt
```

Isso instala:
- `requirements.txt`: dependencias de execucao (`antlr4-python3-runtime`, `llvmlite`)
- `-e .`: o proprio pacote `jss_compiler` em modo editavel (permite `import jss_compiler` sem mexer no `PYTHONPATH`)
- `requirements-dev.txt`: dependencias de desenvolvimento (`pytest`, para rodar os testes em `tests/`)

Se nao instalar o pacote em modo editavel, defina o `PYTHONPATH` antes de executar:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

### Verificando a instalacao

```powershell
python .\main.py .\examples\teste1.jss
.\examples\teste1.exe
```

Se aparecer `Programa válido.` e o `.exe` rodar sem erro, o ambiente esta correto.

## Como executar o compilador
## ETAPA DE BUILD //Gerar .LL e .EXE SEM EXECUTAR
  python .\main.py arquivo.jss
  python .\main.py --build arquivo.jss
  python .\main.py .\examples\soma_run.jss
## ETAPA DE BILD + RUN DIRETO 
  python .\main.py --run .\examples\teste1.jss

## fluxo de execução simplificado (GERA A IR E O EXE ) *** a) e b)
  BUILD + RUN(DO EXE GERADO PELO BUILD) -- GERA A LL E O EXE E EXECUTA A EXE GERADA
  python .\main.py .\examples\teste1.jss 
  .\examples\teste1.exe                       


O compilador recebe o caminho do arquivo `.jss` como argumento:

```powershell
python .\main.py .\examples\teste1.jss
```

Para executar qualquer arquivo da pasta `examples`:

```powershell
python .\main.py .\examples\nome_do_arquivo.jss
```

Testes disponíveis (1 a 10):
```powershell BUILD DOS TESTES 

python .\main.py .\examples\1_basics.jss
.\examples\1_basics.exe  
python .\main.py .\examples\2_operators.jss
.\examples\2_operators.exe  
python .\main.py .\examples\3_control_flow.jss
.\examples\3_control_flow.exe  
python .\main.py .\examples\4_strings_casts.jss
.\examples\4_strings_casts.exe  
python .\main.py .\examples\5_classes.jss
.\examples\5_classes.exe  
python .\main.py .\examples\6_functions.jss
.\examples\6_functions.exe  
python .\main.py .\examples\teste7.jss
.\examples\teste7.exe  
python .\main.py .\examples\teste8.jss
.\examples\teste8.exe  
python .\main.py .\examples\teste9.jss
.\examples\teste9.exe 
python .\main.py .\examples\teste10.jss
.\examples\teste10.exe  
```

python .\main.py .\espc\espc1.jss
.\espc\espc1.exe

## NO POWERSHELL NA PASTA ONDE O EXECUTAVEL ESTA NO WINDOS VOCE PODE EXECUTAR SIMPLESMENTE
abrindo o powershell na pasta onde esta o exe 
e rodandoe sse comando
 .\teste1.exe

Para rodar todos os testes automaticamente:

```powershell
powershell -ExecutionPolicy Bypass -File .\testar_tudo.ps1
powershell -ExecutionPolicy Bypass -File .\teste_1_10.ps1
powershell -ExecutionPolicy Bypass -File .\executar_run.ps1
esse ultimo script roda todos os arquivos .jss que estao em run NAO E RUN E SO O BUILD O RUN E MANUAL AINDA 
O script roda todos os arquivos .jss que estiverem lá, em ordem alfabética, e imprime a saída de cada um.
```

Saida esperada para um programa lexica e sintaticamente valido:

```text
Programa válido.
```
