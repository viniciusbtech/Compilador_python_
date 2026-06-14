# Compilador JSS

Compilador acadêmico para a linguagem **Java Script Simplificado (JSS)**.

## Estrutura

```text
jss-compiler/
├── main.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── examples/
├── src/
│   └── jss_compiler/
└── tests/
```

## Ambiente

```bash
python -m venv .venv
python -m pip install -e .
```

### Linux/macOS

```bash
source .venv/bin/activate
```


Instale as dependências de desenvolvimento:

```bash
pip install -r requirements-dev.txt
```

## Execução

O compilador lê um arquivo `.jss` pela entrada padrão:

```bash
python main.py < examples/sucesso_minimo.jss
```

Enquanto o lexer e o parser ainda são estruturas iniciais, a execução retorna:

```text
Programa válido.
```

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
pip install -r requirements-dev.txt

Como executar 
$env:PYTHONPATH = "$PWD\src"
gc .\examples\sucesso_minimo.jss | python .\main.py
gc .\examples\codigo.jss | python .\main.py

Como exercutar um programa 
gc .\examples\teste.jss | python .\main.py

Ver os tokens do parser
Get-Content .\examples\teste.jss -Raw |
    python -m jss_compiler.debug_lexer
```

### Fim da execucação no powerShell


## Testes

```bash
pytest
```

## Próximas etapas

1. Implementar o analisador léxico.
2. Implementar a gramática e o analisador sintático.
3. Padronizar mensagens de erro com linha e coluna.
4. Implementar tabela de símbolos e análise semântica.





### ANALISADOR LEXICO 


## 1.COmo conferir a entrada 
Get-Content .\examples\teste_lexer.jss

!!importante
## TESTE VISUAL DOS TOKENS 
Get-Content .\examples\teste_lexer.jss -Raw |
    python -m jss_compiler.debug_lexer
Get-Content .\examples\<nomedocodigo>.jss -Raw |
    python -m jss_compiler.debug_lexer
Get-Content .\examples\teste.jss -Raw |
    python -m jss_compiler.debug_lexer
    

## Teste em teste_lexer
pytest -v .\tests\test_lexer.py

## Testar erro lexico 
Testando um erro léxico

Get-Content .\examples\erro_lexico.jss -Raw |
    python -m jss_compiler.debug_lexer

Get-Content .\examples\<example>.jss -Raw |
    python -m jss_compiler.debug_lexer
