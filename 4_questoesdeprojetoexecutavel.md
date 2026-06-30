Letra b) - Geração de executável a partir do LLVM IR

  Objetivo: permitir que o compilador gere um executável do sistema operacional a partir do arquivo LLVM IR produzido pelo back-end.

  ———

  Sub-issue 1: Definir ferramenta de compilação do LLVM IR  OKKK!!!

  Descrição:
  Escolher e documentar qual ferramenta será usada para transformar .ll em executável.

  Opções prováveis:

  clang arquivo.ll -o programa.exe

  ou, em fluxo mais detalhado:

  llvm-as arquivo.ll -o arquivo.bc
  llc arquivo.bc -o arquivo.obj
  clang arquivo.obj -o programa.exe

  Critérios de aceite:

  - Definir se o projeto usará clang diretamente ou pipeline llvm-as + llc + clang.
  - Documentar dependências necessárias no Windows.
  - Registrar comando mínimo para compilar um .ll.

 O executável rodou corretamente:

  Soma: 8
  Mensagem: Ola Mundo
  Media: 8.000000
  10 eh par? true
  Nome: Joao Silva
  Total: 150
  Fatorial de 5: 120
  Processando...

  clang arquivo.ll -o programa.exe

  ———

  Sub-issue 2: Validar LLVM IR gerado OKK!!!

  Descrição:
  Antes de gerar executável, validar se o .ll produzido é aceito pelas ferramentas LLVM.

  Comando possível:

  llvm-as arquivo.ll -o arquivo.bc

  ou:

  clang arquivo.ll -o programa.exe

  Critérios de aceite:

  - Pegar exemplos já existentes em examples/.
  - Confirmar quais .ll compilam corretamente.
  - Listar erros encontrados, se houver.
  - Separar erros de geração LLVM de erros de ambiente.

  ———

  Sub-issue 3: Gerar executável manualmente a partir de um exemplo

  Descrição:
  Usar um programa .jss, gerar seu .ll e depois gerar o .exe.

  Fluxo esperado:

  python main.py examples/teste1.jss
  clang examples/teste1.ll -o examples/teste1.exe
  .\examples\teste1.exe

  Critérios de aceite:

  - Um exemplo simples gera .ll.
  - O .ll vira .exe.
  - O .exe executa no Windows.
  - A saída do programa bate com o esperado.

  ———

  Sub-issue 4: Testar suporte às funções externas usadas no LLVM IR

  Descrição:
  O LLVM IR gerado usa funções externas como:

  printf
  scanf
  malloc
  sprintf
  strlen
  strcpy
  strcat

  É preciso confirmar se o link com a runtime C funciona corretamente no Windows.

  Critérios de aceite:

  - console.log funciona no executável.
  - input funciona no executável.
  - Strings e concatenação funcionam, se já estiverem corretas no IR.
  - Programas com malloc linkam corretamente.

  ———

  Sub-issue 5: Documentar o processo de geração de executável

  Descrição:
  Criar documentação da etapa b), explicando como sair de:

  arquivo.jss

  para:

  arquivo.ll
  arquivo.exe

  Critérios de aceite:

  - Documentar pré-requisitos.
  - Documentar comandos.
  - Documentar exemplo completo.
  - Documentar possíveis erros comuns, como clang não encontrado.

  ———

  Sub-issue 6: Definir comportamento esperado do compilador para a etapa b)

  Descrição:
  Decidir se nesta fase o executável será gerado manualmente por comandos externos ou se futuramente o próprio compilador chamará
  clang.

  Opções:

  Opção 1: o compilador gera apenas .ll, e a documentação ensina a gerar .exe.
  Opção 2: o compilador passa a ter uma flag para gerar executável.

  Exemplo futuro:

  python main.py examples/teste1.jss --exe

  Critérios de aceite:

  - Decidir escopo da letra b).
  - Registrar se a automação fica para depois.
  - Deixar claro que a etapa atual é gerar executável a partir do .ll.

  ———

  Sub-issue 7: Criar casos de teste para executáveis gerados

  Descrição:
  Selecionar programas JSS representativos para validar executáveis.

  Casos mínimos:

  - programa com console.log;
  - programa com operações aritméticas;
  - programa com if;
  - programa com while ou for;
  - programa com função main;
  - programa com variável global;
  - programa com string;
  - programa com input, se for testável manualmente.

  Critérios de aceite:

  - Cada exemplo gera .ll.
  - Cada .ll gera .exe.
  - Cada .exe executa sem erro.
  - A saída é comparada com o esperado.

  ———

  Resumo: a letra b) pode ser quebrada assim:

  b.1 escolher ferramenta LLVM/clang
  b.2 validar o LLVM IR
  b.3 gerar executável manualmente
  b.4 validar runtime C
  b.5 documentar comandos
  b.6 decidir automação futura no compilador
  b.7 testar executáveis gerados



  ## STRING 42 DO TESTE 4

  %"valor_int.2" = load i32, i32* @"valor_int"
  %"str_buf" = call i8* @"malloc"(i64 64)
  %"strptr.38" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.41", i32 0, i32 0
  %".37" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %"str_buf", i8* %"strptr.38", i32 %"valor_int.2")
  store i8* %"str_buf", i8** @"num_str"
