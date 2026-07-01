# Avaliação: cobertura das letras a), b) e c)

Revisão feita sem alterar nenhum código ou arquivo existente — apenas leitura do repositório atual (README.md, 2_projetobackend.md, 3_regrasdetraduçãoAST_LLMVIR.md, 4_questoesdeprojetoexecutavel.md, src/jss_compiler/cli.py, examples/, espc/, erros/, tests/test_erros_execucao.py).

---

## a) Regras de tradução da parse tree / AST para linguagem intermediária (LLVM)

Existe em `3_regrasdetraduçãoAST_LLMVIR.md`. Cobre:

- tipos (int/real/bool/str/void/classe/array);
- classes → structs;
- variáveis globais e locais;
- funções;
- expressões aritméticas e lógicas (com promoção int→real);
- comparações;
- coerção de tipos;
- controle de fluxo (if/while/for/return);
- chamadas de função, `console.log`, `input`, casts;
- arrays e objetos (acesso, atributo, `new`, string literal).

**Status: parcialmente coberto.** O próprio arquivo termina com uma lista de lacunas que parece ter sido colada por engano (resíduo de edição/IA, com texto cortado/repetido nas linhas finais):

- Operadores unários (`-x`, `!b`, `x++`, `++x`, `x--`, `--x`) e a distinção pré vs pós — seção inteira ausente.
- Operadores compostos de atribuição (`+=`, `-=`, `*=`, `/=`, `%=`) com tabela int vs real — não documentados.
- Inicialização de array (`let int[3] arr = [1,2,3]`) — não documentada (gera `getelementptr` + `store` por elemento, segundo o próprio comentário).
- String literal como constante global (`[N x i8]` terminada em `\00`) — só mencionada de raspão no item 10.

**Recomendação:** completar essas 4 seções e remover o texto solto/duplicado do final do arquivo.

---

## b) Geração de executável a partir da linguagem intermediária

**Status: implementado e funcional.**

- `src/jss_compiler/cli.py` chama `clang arquivo.ll -o arquivo.exe` (`_build_executable`), com `-llegacy_stdio_definitions` no Windows.
- Verifica se `clang` está no PATH antes de tentar compilar, e reporta erro claro caso não esteja.
- Suporta `--build` (gera `.ll` + `.exe` sem rodar) e `--run` (gera e executa).
- Os `.exe` versionados em `examples/` e `espc/` existem e correspondem aos `.ll` gerados — evidência de que o pipeline `.jss → .ll → .exe` funciona de ponta a ponta no Windows.

Nenhuma lacuna funcional encontrada nesta etapa.

---

## c) Manual (README) — back-end e front-end

### I. Instalação de bibliotecas pré-requisitas

**Status: incompleto.** O README documenta apenas as dependências Python:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pip install -e .
pip install -r requirements-dev.txt
```

(`requirements.txt` cobre `antlr4-python3-runtime` e `llvmlite`.)

**Falta:** instruções para instalar o **Clang/LLVM toolchain**, que é uma dependência externa *obrigatória* para a etapa b) — sem ele, `_build_executable` falha com "clang nao encontrado no PATH" e nenhum `.exe` é gerado. O README não menciona isso em nenhum lugar (nem como pré-requisito, nem como troubleshooting).

### II. Execução com exemplos de código com erro e sucesso

**Status: incompleto — só há exemplos de sucesso.**

- O README mostra apenas fluxos de sucesso (`teste1.jss` ... `teste6.jss`, `espc1.jss`).
- **Não há nenhum exemplo de código com erro no README**, nem arquivos de exemplo demonstráveis via CLI:
  - a pasta `erros/` existe mas está **vazia**;
  - os arquivos `erro1.jss` ... `erro10.jss` citados em `2_projetobackend.md` **não existem** no repositório;
  - os únicos casos de erro presentes no projeto são strings inline em `tests/test_erros_execucao.py` (erros léxicos como caractere inválido, string não terminada, identificador iniciado por número, escape inválido, etc.) — úteis para teste automatizado, mas não utilizáveis como exemplo demonstrável no manual (não são arquivos `.jss` que alguém possa rodar com `python .\main.py arquivo.jss` para ver o erro).

**Recomendação:** criar 2–3 arquivos `.jss` reais com erro (léxico, sintático, semântico) dentro de `erros/`, e adicionar ao README um bloco mostrando o comando e a saída de erro esperada, ao lado dos exemplos de sucesso já existentes.

### Observação adicional sobre o README

O arquivo mistura instruções de uso com anotações de depuração/raciocínio (ex.: linhas próximas ao final sobre o comportamento de `console.log` como `void` dentro de chamadas aninhadas) que não são parte do manual e deveriam ser removidas ou movidas para um arquivo de notas técnicas separado.

---

## Resumo

| Item | Status |
|---|---|
| a) Regras de tradução AST → LLVM IR | Parcial — base sólida, faltam 4 seções (unários, compostos, init de array, string literal) + limpeza do final do arquivo |
| b) Geração de executável | Completo |
| c.I) Pré-requisitos de instalação | Faltando: instalação do Clang/LLVM não documentada |
| c.II) Exemplos com erro e sucesso | Faltando: só há exemplos de sucesso; pasta `erros/` vazia, sem arquivos `.jss` de erro demonstráveis |
