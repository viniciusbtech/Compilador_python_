# Compilador JSS — Guia Rápido

## Instalação

No Windows PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pip install -e .
```

## Como executar

```powershell
python .\main.py .\examples\sucesso_minimo.jss
```

Substitua o caminho pelo arquivo `.jss` que deseja compilar.

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
