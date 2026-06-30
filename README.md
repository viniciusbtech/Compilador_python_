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
## ETAPA DE BUILD //Gerar .LL e .EXE SEM EXECUTAR
  python .\main.py arquivo.jss
  python .\main.py --build arquivo.jss
  python .\main.py .\examples\soma_run.jss
## ETAPDA DE RUN GERA EXECUTAVVEL E JA EXECUTA
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

python .\main.py .\examples\teste1.jss
.\examples\teste1.exe  
python .\main.py .\examples\teste2.jss
.\examples\teste2.exe  
python .\main.py .\examples\teste3.jss
.\examples\teste3.exe  
python .\main.py .\examples\teste4.jss
.\examples\teste4.exe  
python .\main.py .\examples\teste5.jss
.\examples\teste5.exe  
python .\main.py .\examples\teste6.jss
.\examples\teste6.exe  
python .\main.py .\examples\teste7.jss
.\examples\teste7.exe  
python .\main.py .\examples\teste8.jss
.\examples\teste8.exe  
python .\main.py .\examples\teste9.jss
.\examples\teste9.exe 
python .\main.py .\examples\teste10.jss
.\examples\teste10.exe  
```

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
