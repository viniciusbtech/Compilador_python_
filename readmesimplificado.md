# Compilador JSS — Guia Rápido

## Instalação

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pip install -e .
```

**Linux / macOS (terminal):**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Como executar

**Windows:**
```powershell
python .\main.py .\examples\teste1.jss
```

**Linux / macOS:**
```bash
python3 main.py examples/teste1.jss
```

Substitua o caminho pelo arquivo `.jss` que deseja compilar.

## Como executar em lote

Coloque os arquivos `.jss` no diretório `run/` e execute:

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File .\executar_run.ps1
```

**Linux / macOS:**
```bash
for f in run/*.jss; do echo "--- $f ---"; python3 main.py "$f"; done
```


## Saídas possíveis

Programa válido:
```
Programa válido.
```

Erro (léxico, sintático ou semântico):
```
Erro léxico na linha X, coluna Y: ...
Erro sintático na linha X, coluna Y: ...
Erro semântico na linha X, coluna Y: ...
```
## COMO O PROGRAMA TRATA ARQUIVOS 
usuário passa o caminho como argumento
   -> argparse captura em args.arquivo
   -> open(args.arquivo, encoding="utf-8") lê o conteúdo inteiro
   -> source (string) é passado para analyze_source()
   -> frontend orquestra lexer -> parser -> semântico