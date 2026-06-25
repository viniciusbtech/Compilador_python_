class Ponto {
int x;
int y;
Ponto constructor (int x, int y) {
this.x = x;
this.y = y;
}
int soma () {
return this.x + this.y;
}
}


let Ponto p1;
p1 = new Ponto (1 ,2);
p1 = null;
const Ponto p2 = new Ponto (10 ,100);