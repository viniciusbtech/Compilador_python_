// Testes de erros semanticos (arquivo deve falhar na compilacao)

let int x = 10;

// ERRO: variavel nao declarada
y = 5;

// ERRO: redeclaracao de variavel
 x = 20;

// ERRO: tipo incompativel na atribuicao
let str s = "42";

// ERRO: atribuicao em constante
const int c = 100;
//c = 200;

// ERRO: break fora de loop
//break;

// ERRO: tipo incompativel em operacao
let real r = 5.5;
let bool b = false || true;

// ERRO: cast invalido de string para int  
let str texto = "hello";
let int numero = int(r);

// ERRO: cast invalido de string para bool  //CONFLITO DE CAST COM 4_string_cast.jss
let bool flag = bool(r);

// ERRO: concatenacao invalida (string + int)
let str msg = "Valor: " + "10";

// ERRO: operacao entre tipos incompativeis
let int resultado = int(r) * 2;

// Chamadas de funcoes com erro
//let int val1 = semReturn();
//voidComValor();
//let int val2 = intSemValor();
//let int val3 = tipoRetornoErrado();
//let str val4 = strSemReturn();

// Uso de 'this' fora de classe
//let int id = this.id;

//variavel não declarado em for
let int n = 10;

for(let int i = 0+0; i < n; i++){
    console.log(i);
}

//variavel não declarado em for
x = 0;
let int y = 0;
for( i = 0+0; i < n; i++){
    let int x;
    x++;
    y++;
}