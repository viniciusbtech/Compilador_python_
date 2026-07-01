function int fatorial (int fat) {
if (fat > 1) {
console.log(fat);
return fat * fatorial (fat - 1);
} else {
return 1;
}
}
function void printMedia (int v1 , int v2) {
const real x = media (v1 ,v2);
console.log (" Resultado : ", x);
}
function real media ( real n1 , real n2) {
return (n1 + n2)/2;
}
function void main( ) { // facultativo a declaração de uma função main
let int numero ;
let int n1 , n2;
console.log (" Programa Fatorial. Digite o valor: ");
input( numero );
console.log ( fatorial ( numero ));
console.log (" Programa Media . Digite os valores: ");
input(n1 , n2);
console.log (console.log(media (n1 , n2)));
}