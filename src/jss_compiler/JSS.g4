/**
 * Gramática ANTLR4 da linguagem JSS (Java Script Simplificado).
 *
 * No pipeline do compilador, o lexer existente (lexer.py) é utilizado para
 * tokenização e detecção de erros léxicos; as regras léxicas aqui presentes
 * servem como documentação formal e para geração das constantes de tipo de
 * token usadas pelo parser ANTLR.
 */
grammar JSS;

// ═══════════════════════════════════════════════════════════════════════════
// REGRAS DO PARSER
// ═══════════════════════════════════════════════════════════════════════════

program
    : declaration* EOF
    ;

declaration
    : functionDecl
    | classDecl
    | statement
    ;

// ── Declarações de variáveis ─────────────────────────────────────────────

varDecl
    : LET type_ arrayTypeDim? declarator (',' declarator)* SEMICOLON
    ;

constDecl
    : CONST type_ arrayTypeDim? declarator (',' declarator)* SEMICOLON
    ;

// Suporta 1D [N] ou 2D [N][M]
arrayTypeDim
    : LEFT_BRACKET expr RIGHT_BRACKET (LEFT_BRACKET expr RIGHT_BRACKET)?
    ;

declarator
    : IDENTIFIER (LEFT_BRACKET expr RIGHT_BRACKET)?
      ('=' (LEFT_BRACKET (expr (',' expr)*)? RIGHT_BRACKET | expr))?
    ;

// ── Funções ──────────────────────────────────────────────────────────────

functionDecl
    : FUNCTION returnType IDENTIFIER parameters block
    ;

parameters
    : LEFT_PAREN (parameter (',' parameter)*)? RIGHT_PAREN
    ;

parameter
    : type_ arrayTypeDim? IDENTIFIER
    ;

returnType
    : type_ arrayTypeDim?
    | VOID
    ;

type_
    : TYPE_INT
    | TYPE_REAL
    | TYPE_STR
    | TYPE_BOOL
    | IDENTIFIER
    ;

// ── Classes ──────────────────────────────────────────────────────────────

classDecl
    : CLASS IDENTIFIER LEFT_BRACE classMember* RIGHT_BRACE
    ;

classMember
    : constructorDecl
    | returnType IDENTIFIER parameters block   // método
    | type_ arrayTypeDim? IDENTIFIER SEMICOLON // atributo (scalar ou array/matriz)
    ;

constructorDecl
    : IDENTIFIER CONSTRUCTOR parameters block
    ;

// ── Bloco e comandos ─────────────────────────────────────────────────────

block
    : LEFT_BRACE statement* RIGHT_BRACE
    ;

statement
    : varDecl
    | constDecl
    | ifStmt
    | whileStmt
    | forStmt
    | returnStmt
    | breakStmt
    | block
    | exprStmt
    ;

ifStmt
    : IF LEFT_PAREN expr RIGHT_PAREN block (ELSE (block | ifStmt))?
    ;

whileStmt
    : WHILE LEFT_PAREN expr RIGHT_PAREN block
    ;

forStmt
    : FOR LEFT_PAREN forInit expr? SEMICOLON expr? RIGHT_PAREN block
    ;

forInit
    : varDecl
    | constDecl
    | expr SEMICOLON
    | SEMICOLON
    ;

returnStmt
    : RETURN expr? SEMICOLON
    ;

breakStmt
    : BREAK SEMICOLON
    ;

exprStmt
    : expr SEMICOLON
    ;

// ── Expressões (precedência crescente de cima para baixo) ────────────────

expr
    : assignment
    ;

assignment
    : logicalOr (assignOp assignment)?
    ;

assignOp
    : ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | STAR_ASSIGN
    | SLASH_ASSIGN
    | PERCENT_ASSIGN
    | POWER_ASSIGN
    | AND_AND_ASSIGN
    | OR_OR_ASSIGN
    ;

logicalOr
    : logicalAnd (OR_OR logicalAnd)*
    ;

logicalAnd
    : equalityRel (AND_AND equalityRel)*
    ;

equalityRel
    : addition ((EQUAL_EQUAL | BANG_EQUAL | GREATER | GREATER_EQUAL | LESS | LESS_EQUAL) addition)*
    ;

addition
    : multiplication ((PLUS | MINUS) multiplication)*
    ;

multiplication
    : exponentiation ((STAR | SLASH | PERCENT) exponentiation)*
    ;

exponentiation
    : unary (POWER exponentiation)?
    ;

unary
    : (BANG | PLUS | MINUS | PLUS_PLUS | MINUS_MINUS) unary
    | postfix
    ;

postfix
    : primary postfixOp*
    ;

postfixOp
    : LEFT_PAREN argumentList? RIGHT_PAREN   // chamada de função/método
    | LEFT_BRACKET expr RIGHT_BRACKET        // acesso por índice
    | DOT IDENTIFIER                         // acesso a atributo
    | PLUS_PLUS                              // pós-incremento
    | MINUS_MINUS                            // pós-decremento
    ;

argumentList
    : expr (',' expr)*
    ;

primary
    : INTEGER_LITERAL                                                     # litInt
    | REAL_LITERAL                                                        # litReal
    | STRING_LITERAL                                                      # litStr
    | TRUE                                                                # litTrue
    | FALSE                                                               # litFalse
    | NULL                                                                # litNull
    | THIS                                                                # primaryThis
    | IDENTIFIER                                                          # primaryId
    | INPUT                                                               # primaryInput
    | CONSOLE_LOG                                                         # primaryConsoleLog
    | NEW IDENTIFIER LEFT_PAREN argumentList? RIGHT_PAREN                # primaryNew
    | LEFT_PAREN expr RIGHT_PAREN                                         # primaryParen
    | (TYPE_INT | TYPE_REAL | TYPE_BOOL | TYPE_STR)
      LEFT_PAREN argumentList? RIGHT_PAREN                               # primaryCast
    ;

// ═══════════════════════════════════════════════════════════════════════════
// REGRAS DO LEXER
// Os nomes dos tokens correspondem exatamente ao enum TokenType de tokens.py
// ═══════════════════════════════════════════════════════════════════════════

// Palavras-chave (devem preceder IDENTIFIER para terem prioridade)
LET         : 'let' ;
CONST       : 'const' ;
FUNCTION    : 'function' ;
VOID        : 'void' ;
IF          : 'if' ;
ELSE        : 'else' ;
WHILE       : 'while' ;
FOR         : 'for' ;
BREAK       : 'break' ;
RETURN      : 'return' ;
CLASS       : 'class' ;
CONSTRUCTOR : 'constructor' ;
NEW         : 'new' ;
THIS        : 'this' ;
TRUE        : 'true' ;
FALSE       : 'false' ;
NULL        : 'null' ;
INPUT       : 'input' ;

// Token composto: console.log é tratado como uma única unidade léxica.
// O predicate garante que 'console.log2' não case (letra/dígito após 'log').
CONSOLE_LOG : 'console.log' ;

// Tipos primitivos
TYPE_INT    : 'int' ;
TYPE_REAL   : 'real' ;
TYPE_STR    : 'str' ;
TYPE_BOOL   : 'bool' ;

// Literais numéricos — o mais específico (real/científico) precede o inteiro
REAL_LITERAL
    : [0-9]+ '.' [0-9]+ ([eE] [+\-]? [0-9]+)?
    | [0-9]+             [eE] [+\-]? [0-9]+
    ;

INTEGER_LITERAL
    : [0-9]+
    ;

// Literal de string (escapes válidos: \n \t \r \" \\)
STRING_LITERAL
    : '"' ( ~["\\\n\r] | '\\' [ntr"\\] )* '"'
    ;

// Identificador — vem depois de todas as palavras-chave
IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// Operadores — da combinação mais longa para a mais curta
POWER_ASSIGN    : '**=' ;
AND_AND_ASSIGN  : '&&=' ;
OR_OR_ASSIGN    : '||=' ;
POWER           : '**' ;
EQUAL_EQUAL     : '==' ;
BANG_EQUAL      : '!=' ;
GREATER_EQUAL   : '>=' ;
LESS_EQUAL      : '<=' ;
AND_AND         : '&&' ;
OR_OR           : '||' ;
PLUS_PLUS       : '++' ;
MINUS_MINUS     : '--' ;
PLUS_ASSIGN     : '+=' ;
MINUS_ASSIGN    : '-=' ;
STAR_ASSIGN     : '*=' ;
SLASH_ASSIGN    : '/=' ;
PERCENT_ASSIGN  : '%=' ;
ASSIGN          : '=' ;
PLUS            : '+' ;
MINUS           : '-' ;
STAR            : '*' ;
SLASH           : '/' ;
PERCENT         : '%' ;
BANG            : '!' ;
GREATER         : '>' ;
LESS            : '<' ;

// Pontuação
LEFT_PAREN      : '(' ;
RIGHT_PAREN     : ')' ;
LEFT_BRACE      : '{' ;
RIGHT_BRACE     : '}' ;
LEFT_BRACKET    : '[' ;
RIGHT_BRACKET   : ']' ;
SEMICOLON       : ';' ;
COMMA           : ',' ;
DOT             : '.' ;

// Descartados
WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '//' ~[\r\n]* -> skip ;
