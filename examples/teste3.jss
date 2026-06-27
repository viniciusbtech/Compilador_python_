// Int para Real
let int valor_int = 42;
let real valor_real = real(valor_int);
console.log("Int->Real:", valor_int, "->", valor_real);

// Real para Int
let real pi = 3.14;
let int pi_int = int(pi);
console.log("Real->Int:", pi, "->", pi_int);

// Para String
let str num_str = str(valor_int);
console.log("Int->String:", num_str);

// Para Bool
let int zero = 0;
let int nao_zero = 5;
let bool falso = bool(zero);
let bool verdadeiro = bool(nao_zero);
console.log("Int->Bool:", falso, verdadeiro);

// Cast em expressoes
let int result = int(5.5 + 4.5);
console.log("Cast expressao:", result);