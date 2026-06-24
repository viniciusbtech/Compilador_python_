class Contador {
  int valor;

  Contador constructor(int valor) {
    this.valor = valor;
  }

  int soma(int x) {
    return this.valor + x;
  }
}

let Contador c = new Contador(10);

function void main() {
  console.log(c.soma(5));
}