programa ::= declaracao_global*

declaracao_global ::= declaracao_variavel
                    | declaracao_constante
                    | declaracao_funcao
                    | declaracao_classe
                    | comando_expressao

declaracao_variavel ::= "let" tipo vetor_tipo? declarador ("," declarador)* ";"
declaracao_constante ::= "const" tipo vetor_tipo? declarador ("," declarador)* ";"

vetor_tipo ::= "[" expressao "]"

declarador ::= IDENTIFICADOR vetor_declarador? inicializador?
vetor_declarador ::= "[" expressao "]"

inicializador ::= "=" expressao
                | "=" "[" lista_expressoes? "]"

lista_expressoes ::= expressao ("," expressao)*

declaracao_funcao ::= "function" tipo_retorno IDENTIFICADOR parametros bloco

tipo_retorno ::= tipo | "void"

tipo ::= "int"
       | "real"
       | "str"
       | "bool"
       | IDENTIFICADOR

parametros ::= "(" lista_parametros? ")"

lista_parametros ::= parametro ("," parametro)*

parametro ::= tipo IDENTIFICADOR

declaracao_classe ::= "class" IDENTIFICADOR "{" membro_classe* "}"

membro_classe ::= declaracao_construtor
                | declaracao_metodo
                | declaracao_atributo

declaracao_construtor ::= IDENTIFICADOR "constructor" parametros bloco

declaracao_metodo ::= tipo_retorno IDENTIFICADOR parametros bloco

declaracao_atributo ::= tipo IDENTIFICADOR ";"


## condicionais

bloco ::= "{" comando* "}"

comando ::= declaracao_variavel
          | declaracao_constante
          | comando_if
          | comando_while
          | comando_for
          | comando_return
          | comando_break
          | bloco
          | comando_expressao

comando_if ::= "if" "(" expressao ")" bloco ("else" (bloco | comando_if))?

comando_while ::= "while" "(" expressao ")" bloco

comando_for ::= "for" "(" inicializador_for expressao? ";" expressao? ")" bloco

inicializador_for ::= declaracao_variavel
                    | declaracao_constante
                    | expressao? ";"

comando_return ::= "return" expressao? ";"

comando_break ::= "break" ";"

comando_expressao ::= expressao ";"

## Aritmeticos 

expressao ::= atribuicao

atribuicao ::= logico_or operador_atribuicao atribuicao
             | logico_or

operador_atribuicao ::= "="
                      | "+="
                      | "-="
                      | "*="
                      | "/="
                      | "%="
                      | "**="

logico_or ::= logico_and ("||" logico_and)*

logico_and ::= igualdade_relacional ("&&" igualdade_relacional)*

igualdade_relacional ::= adicao (("==" | "!=" | ">" | ">=" | "<" | "<=") adicao)*

adicao ::= multiplicacao (("+" | "-") multiplicacao)*

multiplicacao ::= exponenciacao (("*" | "/" | "%") exponenciacao)*

exponenciacao ::= unario ("**" exponenciacao)?

unario ::= ("!" | "+" | "-" | "++" | "--") unario
         | posfixo

posfixo ::= primario chamada_ou_acesso*

chamada_ou_acesso ::= "(" argumentos? ")"
                    | "[" expressao "]"
                    | "." IDENTIFICADOR

argumentos ::= expressao ("," expressao)*

primario ::= INTEIRO
           | REAL
           | STRING
           | "true"
           | "false"
           | "null"
           | IDENTIFICADOR
           | "input"
           | "console.log"
           | "this"
           | "new" IDENTIFICADOR "(" argumentos? ")"
           | "(" expressao ")"
           | tipo_primitivo "(" argumentos? ")"

tipo_primitivo ::= "int" | "real" | "bool" | "str"

## Precedencia 

=, +=, -=, *=, /=, %=, **=      direita
||                              esquerda
&&                              esquerda
==, !=, >, >=, <, <=            esquerda
+, -                            esquerda
*, /, %                         esquerda
**                              direita
!, +, -, ++, --                 direita
chamada (), índice [], acesso . maior precedência
