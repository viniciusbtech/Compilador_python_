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


## TESTES DE IR PARA 

1.basics IR
2.Operatores IR
3.Control_flows testados IR
4.STRING CASTS IR 
5.
6.
7.
8.

## ESPECIFICAÇÂO SEPARADORES , CONSOLE.LOG 
4. Nenhuma característica de outra linguagem deve ser reconhecida pelo compilador
No JavaScript, quando você passa múltiplos argumentos para a função console.log separados por vírgulas, ela os imprime na ordem, inserindo automaticamente um espaço entre cada argumento.

Opção 4 ESCOLHIDA!!!!
Opção 4: Comportamento real do JS (manter espaço mas aceitar o comportamento)
O console.log do JavaScript de fato separa todos os argumentos com espaço. Então console.log("Ola", " ", "Mundo", "!") em JS real produz Ola   Mundo ! (três espaços). O comportamento atual é tecnicamente "correto" do ponto de vista do JS.

Nesse caso, a solução seria documentar que o JSS tem console.log sem separador automático (Opção 1).


Opção 1: Sem separa os argumentos com espaço  
DESCARTADA POIS A ESPECIFICAÇÂO  
Nenhuma característica de outra linguagem deve ser reconhecida pelo compilador.
CARACTERÌSTICA DE LINGUAGENS COMO C JAVA e C++ 
Muda " ".join(specs) para "".join(specs).
┌──────────────────────────────────┬────────────────┬─────────────────────┐
│             Chamada              │ Formato gerado │        Saída        │
├──────────────────────────────────┼────────────────┼─────────────────────┤
│ ("Ola", " ", "Mundo", "!")       │ %s%s%s%s       │ Ola Mundo! ✓        │
├──────────────────────────────────┼────────────────┼─────────────────────┤


## CONCATENAÇÂO DE STRINGS UNE EXATAMENTE O CONTEÙDO DAS STRINGS

Opção C: Híbrida (A para literais, B para variáveis)

No _gen_binary com str + str:
- Se ambos os lados forem nós Literal → fold em tempo de compilação (Opção A)
- Caso contrário → gera runtime com malloc/strcat (Opção B)

┌────────┬──────────────────────────────────────────────────────────┐
│        │                                                          │
├────────┼──────────────────────────────────────────────────────────┤
│ Pro    │ IR otimizada quando possível, correta sempre             │
├────────┼──────────────────────────────────────────────────────────┤
│ Contra │ Mais código no gerador para implementar os dois caminhos │
└────────┴──────────────────────────────────────────────────────────┘


O operador + simplesmente "cola" as strings exatamente como elas são, sem adicionar nenhum espaço extra.

Você controlou o espaçamento manualmente incluindo " " (uma string contendo apenas um espaço) entre as palavras "Ola" e "Mundo".
JavaScript

## TRATAMENTO DO INPUT 

 malloc antes de cada scanf de string

No handler do input, antes de chamar scanf para uma string, aloca o buffer em runtime:

%buf  = call i8* @"malloc"(i64 256)
store i8* %buf, i8** @"nome1"           ; grava o ponteiro do buffer na variável
%ptr  = load i8*, i8** @"nome1"         ; agora carrega o i8* válido
call i32 @"scanf"(i8* %fmt, i8* %ptr)  ; passa i8*

┌────────┬───────────────────────────────────────────────────────────────────────────────────────┐
│        │                                                                                       │
├────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ Pro    │ Só aloca quando há leitura de fato; nome1 fica apontando para o buffer após a leitura │
├────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ Contra │ Mais instruções IR; tamanho ainda fixo (256); sem free (vazamento de memória)         │
└────────┴──────────────────────────────────────────────────────────┘


## Problemas 01 ; TargetData (como o GCC, Clang ou o próprio LLVM)


1. O que é o TargetData na prática?
Imagine que o LLVM é um tradutor. Ele traduz o seu código (que é genérico) para a linguagem de máquina (que é muito específica).

O TargetData é o manual de regras da CPU. Ele diz ao LLVM:

Olhando para as regras desta máquina específica onde este executável vai rodar, 
qual é o tamanho exato ocupado por esta estrutura de dados?"

Ao usar struct.get_abi_size(target_data), você está pedindo ao compilador para seguir a ABI (Application Binary Interface) do sistema operacional e do hardware.

struct.get_abi_size(target_data), você está pedindo ao compilador para seguir a ABI (Application Binary Interface) do sistema operacional e do hardware.

Inicialização: Você carrega o backend do LLVM para a arquitetura alvo (ex: x86-64 ou ARM64). Isso permite que o programa acesse tabelas internas que descrevem como o hardware funciona.

Definição do Layout: Você cria um objeto que contém uma "string de layout" (ex: e-m:w-p270:34:64...). Essa string é um código compacto que descreve todas as regras de memória daquela arquitetura.

Consulta: O LLVM pega a definição da sua struct (que você construiu antes), cruza com o TargetData (as regras da CPU) e calcula o tamanho final.

## COMO ELA 

















## QUESTOES PARA SEREM TRATADAS NA EXECUÇÃO DEPOIS" AINDa NÂO TRATADA" 

A verificação de índices fora do limite não é responsabilidade do parser; 
ela pode ser feita pela análise semântica quando os índices são constantes, ou em tempo de execução quando os índices dependem de variáveis.


A. ACESSO EM ARRAYS FORA DOS LIMITES
Ela também diz que o compilador precisa tratar erros léxicos, sintáticos e semânticos, mas não define explicitamente o que deve acontecer em tempo de execução se o índice sair do limite.

1. Parser: não trata limite de índice.
2. Semântica: verifica se o acesso ao array é válido em tipo e dimensão.
3. Semântica opcional: acusa erro se índice constante estiver fora do limite.
4. LLVM IR: gera getelementptr assumindo índice válido.
5. Não implementar comportamento estilo JavaScript.



i passa do limite, por exemplo i = 3 numa matriz [3][3], o parser não tem como acusar, porque o parser só vê que a sintaxe está correta.

Parser:
aceita matriz[i][j], porque a sintaxe está correta.

Análise semântica:
verifica se matriz é array, se tem duas dimensões e se i/j são int.

Análise semântica com índice constante:
pode rejeitar matriz[3][0], porque sabe que 3 está fora de [0..2].

Geração de IR atual:
gera getelementptr assumindo que i/j são válidos.

Runtime check opcional: PODE OU NAO SER IMPLEMENTANDO 
verifica i e j antes de acessar.

## AINDA NAO AVALIADA 