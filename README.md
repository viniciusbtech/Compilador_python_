<div align="center">

# ⚙️ Compilador JSS

### Um compilador acadêmico para a linguagem JavaScript Simplificado, desenvolvido em Python com geração de código LLVM.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![ANTLR](https://img.shields.io/badge/ANTLR-4-ED2224?style=for-the-badge)
![LLVM](https://img.shields.io/badge/LLVM-IR-262D3A?style=for-the-badge\&logo=llvm\&logoColor=white)
![Pytest](https://img.shields.io/badge/Testes-Pytest-0A9EDC?style=for-the-badge\&logo=pytest\&logoColor=white)

</div>

---

## 🔗 Links do Projeto

| Recurso        | Link                                                                                               |
| -------------- | -------------------------------------------------------------------------------------------------- |
| 📦 Repositório | [github.com/viniciusbtech/Compilador_python_](https://github.com/viniciusbtech/Compilador_python_) |
| 🌐 Aplicação   | Não possui aplicação web hospedada                                                                 |
| 🎥 Vídeo       | [Adicionar link do vídeo](#-vídeo-do-projeto)                                                      |

---

## 📖 Introdução

O **Compilador JSS** é um projeto acadêmico que implementa um compilador para uma versão simplificada da linguagem JavaScript, chamada **JavaScript Simplificado — JSS**.

O compilador recebe um arquivo com a extensão `.jss`, realiza as etapas de análise léxica, sintática e semântica, constrói uma Árvore Sintática Abstrata — AST, gera código intermediário LLVM e utiliza o Clang para produzir um arquivo executável.

O fluxo principal de compilação é:

```text
Arquivo .jss
    ↓
Análise léxica
    ↓
Lista de tokens
    ↓
Análise sintática com ANTLR4
    ↓
Construção da AST
    ↓
Análise semântica e tabela de símbolos
    ↓
Geração de código LLVM IR
    ↓
Compilação com Clang
    ↓
Arquivo executável
```

O projeto foi desenvolvido com foco no estudo prático das principais etapas envolvidas na construção de compiladores.

---

## 🛠️ Tecnologias

### 🧠 Núcleo do compilador

| Tecnologia                | Utilização                                                                |
| ------------------------- | ------------------------------------------------------------------------- |
| **Python 3.11+**          | Implementação das etapas do compilador e da interface de linha de comando |
| **ANTLR4**                | Geração do parser a partir da gramática formal da linguagem JSS           |
| **ANTLR4 Python Runtime** | Execução do parser gerado dentro da aplicação Python                      |
| **llvmlite**              | Construção e geração do código intermediário LLVM IR                      |
| **LLVM IR**               | Representação intermediária utilizada antes da geração do executável      |
| **Clang**                 | Conversão do arquivo `.ll` em um programa executável                      |
| **argparse**              | Processamento dos argumentos informados na linha de comando               |

### 🧪 Testes

| Tecnologia             | Utilização                                                  |
| ---------------------- | ----------------------------------------------------------- |
| **Pytest**             | Execução dos testes automatizados                           |
| **Testes de lexer**    | Validação da identificação de tokens e erros léxicos        |
| **Testes de parser**   | Validação da estrutura sintática dos programas              |
| **Testes semânticos**  | Verificação de tipos, escopos e regras da linguagem         |
| **Testes de execução** | Validação dos programas compilados                          |
| **Smoke tests**        | Verificação básica do funcionamento integrado do compilador |

### 💻 Desenvolvimento e versionamento

| Tecnologia                  | Utilização                                                 |
| --------------------------- | ---------------------------------------------------------- |
| **Git**                     | Controle de versão do código                               |
| **GitHub**                  | Hospedagem e organização do repositório                    |
| **PowerShell**              | Automação da compilação e execução dos exemplos no Windows |
| **Ambiente virtual Python** | Isolamento das dependências do projeto                     |

### 🖥️ Frontend

Não se aplica. O projeto não possui interface gráfica ou aplicação web. A interação acontece por meio do terminal.

### ⚙️ Backend

Não existe um backend web ou uma API. O núcleo do compilador é executado localmente por meio dos módulos Python.

### 🗄️ Banco de dados

O projeto não utiliza banco de dados.

### 🚀 Deploy

O projeto não possui deploy em servidor. O processo de build acontece localmente, gerando arquivos LLVM IR e executáveis por meio do Clang.

---

## ✨ Features

* [x] Leitura de arquivos-fonte com extensão `.jss`.
* [x] Lexer manual desenvolvido em Python.
* [x] Identificação de tokens com linha e coluna.
* [x] Tratamento de erros léxicos com mensagens específicas.
* [x] Parser gerado pelo ANTLR4.
* [x] Gramática formal definida no arquivo `JSS.g4`.
* [x] Construção de uma Árvore Sintática Abstrata — AST.
* [x] Criação e gerenciamento de tabela de símbolos.
* [x] Análise semântica de variáveis, funções, classes e expressões.
* [x] Validação de tipos e escopos.
* [x] Detecção do uso incorreto de identificadores.
* [x] Suporte a variáveis com `let`.
* [x] Suporte a constantes com `const`.
* [x] Suporte aos tipos `int`, `real`, `str` e `bool`.
* [x] Suporte ao valor `null`.
* [x] Suporte a vetores e matrizes.
* [x] Suporte a estruturas condicionais `if` e `else`.
* [x] Suporte aos laços `while` e `for`.
* [x] Suporte aos comandos `break` e `return`.
* [x] Suporte à declaração e chamada de funções.
* [x] Suporte a classes, atributos, métodos e construtores.
* [x] Suporte às palavras-chave `new` e `this`.
* [x] Suporte a entrada de dados com `input`.
* [x] Suporte à saída de dados com `console.log`.
* [x] Suporte a conversões explícitas entre tipos.
* [x] Suporte a operadores aritméticos, relacionais e lógicos.
* [x] Suporte a operadores de atribuição composta.
* [x] Suporte aos operadores de incremento e decremento.
* [x] Suporte ao operador de exponenciação `**`.
* [x] Geração de código intermediário LLVM IR.
* [x] Geração de executáveis utilizando o Clang.
* [x] Modo de build sem execução.
* [x] Modo de build seguido de execução automática.
* [x] Definição personalizada do caminho do executável.
* [x] Testes automatizados com Pytest.
* [x] Exemplos práticos organizados por funcionalidade.

---

## ⌨️ Keyboard Shortcuts

O projeto não possui uma interface gráfica e, portanto, não utiliza atalhos de teclado próprios.

A interação acontece por meio de argumentos da linha de comando:

| Comando            | Função                                                        |
| ------------------ | ------------------------------------------------------------- |
| `--build`          | Gera o arquivo LLVM IR e o executável sem executar o programa |
| `--run`            | Gera o LLVM IR, cria o executável e executa o programa        |
| `-o` ou `--output` | Define o caminho e o nome do executável de saída              |
| `-h` ou `--help`   | Exibe a ajuda da interface de linha de comando                |

Exemplo:

```bash
python main.py --help
```

### Sugestões de atalhos futuros

Caso seja criada uma interface gráfica ou extensão para editor, poderão ser adicionados os seguintes atalhos:

| Atalho sugerido    | Ação                     |
| ------------------ | ------------------------ |
| `Ctrl + B`         | Compilar o arquivo atual |
| `Ctrl + R`         | Compilar e executar      |
| `Ctrl + Shift + T` | Executar os testes       |
| `Ctrl + L`         | Limpar o terminal        |
| `F5`               | Executar o programa JSS  |
| `F6`               | Exibir o LLVM IR gerado  |

---

## 🔄 O Processo

### 1. Planejamento

A primeira etapa foi definir o escopo da linguagem JavaScript Simplificado, incluindo seus tipos primitivos, operadores, declarações, estruturas de controle, funções, vetores e orientação a objetos.

Também foi planejado o pipeline completo do compilador:

```text
Lexer → Parser → AST → Analisador semântico → LLVM IR → Executável
```

### 2. Desenvolvimento

O desenvolvimento foi dividido em módulos com responsabilidades específicas:

* O lexer identifica os elementos presentes no código-fonte.
* A ponte de tokens converte os tokens internos para o formato utilizado pelo ANTLR.
* O parser verifica se o código segue a gramática da linguagem.
* O AST Builder transforma a árvore gerada pelo ANTLR em uma AST própria.
* O analisador semântico valida tipos, escopos e declarações.
* O gerador LLVM converte a AST validada em código intermediário.
* A CLI organiza o processo de compilação e execução.

### 3. Testes

Os testes automatizados foram desenvolvidos com Pytest e organizados por responsabilidade:

```text
tests/
├── test_erros_execucao.py
├── test_lexer.py
├── test_lexer_bateria.py
├── test_parser.py
├── test_parser_semicolon_locations.py
├── test_semantic.py
└── test_smoke.py
```

Além dos testes automatizados, o diretório `examples` contém programas destinados à validação de:

* Declarações básicas.
* Operadores.
* Estruturas de controle.
* Strings e conversões.
* Classes.
* Funções.

### 4. Versionamento

O código foi versionado com Git e armazenado no GitHub. A organização modular permite acompanhar as alterações de cada etapa do compilador e facilita a identificação de regressões.

### 5. Revisão

A revisão foi realizada por meio da execução dos testes automatizados, da compilação dos arquivos de exemplo e da análise das mensagens de erro produzidas pelo compilador.

Os arquivos `.ll` gerados também podem ser inspecionados para verificar a tradução do código JSS para LLVM IR.

### 6. Build e execução

Após a validação do código, o compilador gera um arquivo `.ll`. Em seguida, o Clang recebe esse arquivo e cria o programa executável.

O projeto não possui deploy em servidor, pois seu resultado final é uma aplicação de linha de comando executada localmente.

---

## 🎓 O Que Eu Aprendi

Durante o desenvolvimento deste projeto, aprofundei meus conhecimentos sobre:

* Funcionamento das principais etapas de um compilador.
* Construção de analisadores léxicos.
* Definição de tokens, palavras-chave e operadores.
* Criação de gramáticas formais.
* Precedência e associatividade de operadores.
* Uso do ANTLR4 para análise sintática.
* Construção e navegação em Árvores Sintáticas Abstratas.
* Implementação do padrão Visitor.
* Criação e gerenciamento de tabelas de símbolos.
* Controle de escopos globais e locais.
* Verificação de tipos durante a análise semântica.
* Validação de funções, variáveis, constantes e classes.
* Geração de código intermediário com LLVM.
* Integração entre Python, LLVM IR e Clang.
* Construção de interfaces de linha de comando.
* Organização de projetos Python em módulos.
* Gerenciamento de dependências com ambiente virtual.
* Desenvolvimento de testes automatizados com Pytest.
* Identificação e tratamento de erros com linha e coluna.
* Uso de Git e GitHub para versionamento.
* Importância da documentação e da separação de responsabilidades para facilitar revisões e colaboração em equipe.

O projeto também permitiu compreender, na prática, como um código escrito em uma linguagem de alto nível passa por diversas transformações até se tornar um programa executável.

---

## 🚀 Como Ele Pode Ser Melhorado

Algumas melhorias futuras que podem ser implementadas são:

* [ ] Criar uma integração contínua com GitHub Actions.
* [ ] Executar os testes automaticamente em Windows, Linux e macOS.
* [ ] Gerar executáveis com nomes adequados para cada sistema operacional.
* [ ] Melhorar as mensagens de erro com trechos do código e indicadores visuais.
* [ ] Implementar recuperação de erros sintáticos para apresentar múltiplos problemas em uma única execução.
* [ ] Aumentar a cobertura dos testes automatizados.
* [ ] Adicionar testes específicos para o código LLVM gerado.
* [ ] Implementar otimizações no LLVM IR.
* [ ] Criar uma opção para gerar somente o arquivo `.ll`.
* [ ] Adicionar um modo detalhado para visualizar tokens, AST e tabela de símbolos.
* [ ] Criar um REPL para executar comandos JSS de forma interativa.
* [ ] Disponibilizar o compilador como um comando instalável pelo Python.
* [ ] Criar releases com executáveis prontos para uso.
* [ ] Separar os arquivos gerados dos arquivos-fonte de exemplo.
* [ ] Expandir a documentação da gramática.
* [ ] Adicionar mais exemplos de códigos válidos e inválidos.
* [ ] Desenvolver uma interface gráfica para edição, compilação e execução.
* [ ] Criar uma extensão para o Visual Studio Code com destaque de sintaxe para arquivos `.jss`.

---

## ▶️ Como Iniciar o Projeto

### Pré-requisitos

Antes de iniciar, verifique se as seguintes ferramentas estão instaladas:

* Git.
* Python 3.11 ou superior.
* Pip.
* Clang/LLVM disponível no `PATH`.

Verifique as versões instaladas:

#### Windows

```powershell
git --version
python --version
pip --version
clang --version
```

#### Linux e macOS

```bash
git --version
python3 --version
python3 -m pip --version
clang --version
```

> Sem o Clang, o compilador poderá gerar o arquivo LLVM IR, mas não conseguirá produzir o executável.

### 1. Clonar o repositório

```bash
git clone https://github.com/viniciusbtech/Compilador_python_.git
```

Entre na pasta do projeto:

```bash
cd Compilador_python_
```

### 2. Criar o ambiente virtual

#### Windows — PowerShell

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois, execute novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows — Prompt de Comando

```cmd
python -m venv .venv
```

```cmd
.venv\Scripts\activate.bat
```

#### Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

#### macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

#### Windows

```powershell
python -m pip install --upgrade pip
```

```powershell
pip install -r requirements.txt
```

```powershell
python -m pip install -e .
```

```powershell
pip install -r requirements-dev.txt
```

#### Linux e macOS

```bash
python3 -m pip install --upgrade pip
```

```bash
python3 -m pip install -r requirements.txt
```

```bash
python3 -m pip install -e .
```

```bash
python3 -m pip install -r requirements-dev.txt
```

As dependências principais são:

```text
antlr4-python3-runtime
llvmlite
pytest
```

### 4. Variáveis de ambiente

O projeto não utiliza arquivo `.env` nem exige variáveis de ambiente obrigatórias.

Caso o pacote não tenha sido instalado no modo editável, configure temporariamente o `PYTHONPATH`.

#### Windows — PowerShell

```powershell
$env:PYTHONPATH = "$PWD\src"
```

#### Linux e macOS

```bash
export PYTHONPATH="$PWD/src"
```

### 5. Banco de dados

O projeto não utiliza banco de dados. Nenhuma migration ou configuração de conexão é necessária.

### 6. Compilar um programa JSS

#### Windows

```powershell
python .\main.py --build .\examples\1_basics.jss
```

Também é possível omitir `--build`, pois esse é o comportamento padrão:

```powershell
python .\main.py .\examples\1_basics.jss
```

A compilação gera:

```text
examples/1_basics.ll
examples/1_basics.exe
```

Execute o programa gerado:

```powershell
.\examples\1_basics.exe
```

#### Linux e macOS

```bash
python3 main.py --build examples/1_basics.jss
```

Execute o programa gerado:

```bash
./examples/1_basics.exe
```

> O fluxo principal do repositório está documentado para Windows. Em Linux e macOS, é necessário ter uma instalação compatível do Clang e permissão para executar o arquivo gerado.

### 7. Compilar e executar automaticamente

#### Windows

```powershell
python .\main.py --run .\examples\1_basics.jss
```

#### Linux e macOS

```bash
python3 main.py --run examples/1_basics.jss
```

### 8. Definir um arquivo de saída

#### Windows

```powershell
python .\main.py --build .\examples\1_basics.jss -o .\examples\programa.exe
```

#### Linux e macOS

```bash
python3 main.py --build examples/1_basics.jss -o examples/programa.exe
```

### 9. Executar outros exemplos

#### Windows

```powershell
python .\main.py --run .\examples\2_operators.jss
```

```powershell
python .\main.py --run .\examples\3_control_flow.jss
```

```powershell
python .\main.py --run .\examples\4_strings_casts.jss
```

```powershell
python .\main.py --run .\examples\5_classes.jss
```

```powershell
python .\main.py --run .\examples\6_functions.jss
```

#### Linux e macOS

```bash
python3 main.py --run examples/2_operators.jss
```

```bash
python3 main.py --run examples/3_control_flow.jss
```

```bash
python3 main.py --run examples/4_strings_casts.jss
```

```bash
python3 main.py --run examples/5_classes.jss
```

```bash
python3 main.py --run examples/6_functions.jss
```

### 10. Executar os testes automatizados

Com o ambiente virtual ativado:

```bash
pytest
```

Executar os testes com informações detalhadas:

```bash
pytest -v
```

Executar um arquivo específico:

```bash
pytest tests/test_semantic.py -v
```

Executar os testes interrompendo na primeira falha:

```bash
pytest -x
```

### 11. Executar os scripts do PowerShell

No Windows, o projeto disponibiliza scripts para automatizar testes e compilações.

```powershell
powershell -ExecutionPolicy Bypass -File .\testar_tudo.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\teste_1_10.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\executar_run.ps1
```

### 12. Consultar a ajuda da CLI

#### Windows

```powershell
python .\main.py --help
```

#### Linux e macOS

```bash
python3 main.py --help
```

### Endereços locais


---


<div align="center">

Desenvolvido para o estudo prático de compiladores, análise de linguagens e geração de código. ⚙️

</div>
