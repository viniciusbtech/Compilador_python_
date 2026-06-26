## Arquitetura do BACKEND

PYTHON-->FRONTEND-->BACKEND--->X86(EXECUTAVEL)

Fluxo completo

codigo.jss
    │
    ▼
┌─────────────┐
│    Lexer    │  lexer.py
│  (léxico)   │  → lê char por char, gera lista de Tokens
└──────┬──────┘
       │ list[Token]
       ▼
┌─────────────────────┐
│  ANTLR4 Parser      │  antlr_generated/JSSParser.py
│  (sintático)        │  → valida a gramática, gera Parse Tree
└──────┬──────────────┘
       │ Parse Tree
       ▼
┌─────────────┐
│ ASTBuilder  │  ast_builder.py
│             │  → percorre Parse Tree, constrói AST limpa
└──────┬──────┘
       │ AST (ast_nodes.py)
       ▼
┌──────────────────┐
│ SemanticAnalyzer │  semantic.py
│  (semântico)     │  → verifica tipos, escopos, constâncias
│  + Scope chain   │  → anexa Scope a cada Block da AST
└──────┬───────────┘
       │ (AST, SemanticAnalyzer)
       ▼
┌────────────────┐
│ LLVMGenerator  │  llvm_generator.py
│  (llvmlite)    │  → constrói IR usando APIs reais do LLVM
└──────┬─────────┘
       │ texto LLVM IR
       ▼
  codigo.ll


## Arquiterua de registradores
LLVM
LLVM (LowLevelVirtual Machine)
•
IR mais próxima de máquina e fácil de traduzir para um assembly
•
Parecido com TAC


a = b + -c

LLVM IR

define void@main() {
entry:
%b = load i32, i32* 5
%c = load i32, i32* 3
%neg_c= sub i32 0, %c
%sum = addi32 %b, %neg_c
store i32 %sum, i32* %a
retvoid
}

Gerar Assembly x86 e binário


## a)Regras para tradução da parse tree ou arvore sintática no passo anterior para uma linguagem intermediária, podendo ser LLVM ou JASMIN.

-As regras todas foram movidas para um arquivo.md especifico

## FIM DAS REGRAS 

## FLUXO DA EXECUCão PENSANDO 

CÒDIGO SEM DECLARACAO DE FUNCAO MAIN 

Executa normalmente

CODIGO COM DECLACARA DE FUNCAO MAIN EXPLICITA 

1. Análise léxica/sintática.
2. Coleta de símbolos globais: variáveis, constantes, classes e funções.
3. Verificação semântica.
4. Inicialização das variáveis globais.
5. Execução dos comandos globais soltos, se existirem.
6. Se houver function void main(), executar main().

Caso 1: Não existe main
→ comandos globais viram uma main implícita e são executados.

Caso 2: Existe main
→ declarações globais são aceitas.
→ comandos globais também podem ser executados antes da main, mas isso deve ser documentado no README como regra do compilador.

O clang chama @main → executa globals → executa main do usuário. Especificação cumprida — globals rodam antes da main.