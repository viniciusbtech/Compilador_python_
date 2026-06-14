// Demonstração dos tokens da linguagem JSS
function void main() {
    let int numero = 10;
    let real media = 10.8E2;
    const str mensagem = "Olá\n";
    let bool ativo = true;

    numero++;
    numero += 2;

    if (numero >= 10 && ativo != false) {
        console.log(mensagem, numero, media);
    }
}
