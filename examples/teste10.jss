class Aluno {
  str nome;
  real media;
  bool aprovado;

  Aluno constructor(str nome, real media, bool aprovado) {
    this.nome = nome;
    this.media = media;
    this.aprovado = aprovado;
  }

  str getNome() {
    return this.nome;
  }
}

let Aluno aluno = new Aluno("Ana", 8.5, true);

function void main() {
  console.log(aluno.getNome());
}