<style>
  section {
    background: #fff url(./img/background.png) no-repeat center center;
    background-size: cover;
  }

  .transparent {
    background-color: transparent!important;
  }

  .transparent-table-tr-td-th {
    background-color: rgba(0, 0, 0, 0.0) !important;
  }

  .cabecalho {
    position: absolute;
    top: 10%;
    margin-left: 5%;
    margin-right: 10%;
    font-size: 48px;
    font-weight: bold;
  }

  .conteudo {
    top: 30%;
    margin-left: 5%;
    margin-right: 10%;
    font-size: 28px;
    text-align: justify;
  }

  .conteudo-absoluto {
    position: absolute;
    top: 30%;
    margin-left: 5%;
    margin-right: 10%;
    font-size: 28px;
    text-align: justify;
  }
  
  .large {
    font-size: 36px;
  }

  .normal {
    font-size: 22px;
  }
  .regular {
    font-size: 18px;
  }
  .small {
    font-size: 16px;
  }
  .footnotesize {
    font-size: 14px;
  }
  .scriptsize {
    font-size: 12px;
  }
  .tiny {
    font-size: 10px;
  }
  .bold {
    font-weight: bold;
  }
  .center {
    text-align: center;
  }
  section.lead p {
    text-align: justify;
  }
  section.lead h1 {
    text-align: center;
  }
  section.lead h2 {
    text-align: center;
  }
  .two-columns-33-66 {
    position: absolute;
    top: 30%;
    margin-left: 5%;
    margin-right: 10%;
    display: grid;
    grid-template-columns: 1fr 2fr;
    font-size: 28px;
    text-align: justify;
  }
  .two-columns-66-33 {
    position: absolute;
    top: 30%;
    margin-left: 5%;
    margin-right: 10%;
    display: grid;
    grid-template-columns: 2fr 1fr;
    font-size: 28px;
    text-align: justify;
  }

  .two-columns-50-50 {
    position: absolute;
    top: 30%;
    margin-left: 5%;
    margin-right: 10%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    font-size: 28px;
    text-align: justify;
  }
</style>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


# Análise de Circuitos Elétricos
## Aula 03 - Leis de Kirchoff e Instrumentos Para Medição de Grandezas
 
Prof. M.Sc. Diego Ascânio Santos (ascanio@cefetmg.br)

Aula baseada sobre o material do professor Dr. Emerson Gonçalves de Melo (emerdemelo@usp.br - DEMAR EEL USP), da professora Dra. Thabatta Moreira Alves de Araújo (thabatta@cefetmg.br - DIGDDV) e da Khan Academy.

CEFET-MG DIGGDDV - Divinópolis, 2023.


---

# Roteiro

1. Definições, Terminações e Nomenclaturas
    1. Elementos
    2. Nós
    3. Malhas
    4. Tabela de Terminações e Nomenclaturas
2. Lei de Kirchoff da Corrente
3. Lei de Kirchoff da Tensão


---

# Roteiro

4. Análise de circuitos pelas Leis de Kirchoff da Corrente e da Tensão
    1. Construção de Sistemas de Equações Lineares à Partir do Método Thabatta / Khan Academy
    2. Representação dos Sistemas de Equações Lineares em Sua Forma Matricial
    3. Resolução dos Sistemas Lineares por Sistemas Computacionais de Álgebra (CAS - sympy, numpy)


---

# Roteiro

5. Instrumentos de medida de grandezas elétricas
    1. Voltímetro (Tensão)
    2. Amperímetro (Corrente)
    3. Ohmímetro (Resistência)
    4. Multímetro (Múltiplas Grandezas)
6. Lista 3 de Exercícios


---

<!-- _class: lead -->
# Definições, Terminações e Nomenclaturas


---

<div class="cabecalho">
    Definições - Elementos
</div>

<div class="two-columns-50-50">

<div class="normal" style="margin: auto;">

Elementos de circuitos são os componentes presentes em um circuito elétrico como resistores, capacitores, indutores, baterias, fontes (tensão / corrente), chaves, dentre outros.

</div>
<div class="small">
    <center>
        <figure>
            <img class="transparent" src="./img/elementos-circuitos.png" width=75% >
            <figcaption>Exemplos de Elementos de Circuitos.</figcaption>
        </figure>
        <figure>
            <img class="transparent" src="https://cdn.kastatic.org/ka-perseus-images/c603cd86d591948dd4fba50318ba2f1cefebe594.svg" width=75% >
            <figcaption>Circuito composto por resistor, capacitor e indutor.</figcaption>
        </figure>
    </center>
</div>

</div>


---

<div class="cabecalho">
    Definições - Nós
</div>

<div class="two-columns-50-50">

<div style="margin: auto;">

Um nó é um ponto em circuito elétrico que conecta dois ou mais de seus elementos.

</div>
<div class="normal">
    <center>
        <figure>
            <img class="transparent" src="./img/nos.png" width=75% >
            <figcaption>Nós em Um Circuito Elétrico </figcaption>
        </figure>
    </center>
</div>

</div>


---

<div class="cabecalho">
    Definições - Malhas
</div>

<div class="two-columns-50-50">

<div style="margin: auto;">

Um laço é qualquer caminho contínuo e fechado em um circuito que começa e termina no mesmo nó.

<center>
    <figure>
        <img class="transparent" src="https://cdn.kastatic.org/ka-perseus-images/678eee017eff9f24e6e0064a6c6f49c679e7a941.svg" width=75% >
        <figcaption class="regular">Laços (destacados em laranja) presentes em um circuito </figcaption>
    </figure>
</center>

</div>
<div style="margin-left:10%;">

Uma malha é um laço (caminho contínuo e fechado em um circuito) que não apresenta outros laços dentro dele.

<center>
    <figure>
        <img class="transparent" src="./img/malhas.png" width=75% >
        <figcaption class="regular">Exemplo de Circuito Com Três Malhas Dentro Dele </figcaption>
    </figure>
</center>

</div>

</div>


---

<div class="cabecalho large">

Referência de Terminações e Nomenclaturas em Um Circuito

</div>

<div class="two-columns-66-33">
<div>
    <img class="transparent" src="./img/tabela41.png" width>
</div>
<div>
    <img class="transparent" src="./img/figura43.png" width>
</div>
</div>


---

<!-- _class: lead -->
# Lembrete nº 1

<!-- _class: lead -->
## Não Adianta a Sua Matemática Estar Correta se Seu Modelo Estiver Errado!

<!-- _class: lead -->
Um circuito só está resolvido quando os valores das correntes e tensões de seus elementos são conhecidos!


---

<!-- _class: lead -->
# Lei de Kirchoff das Correntes em Um Nó


---

<div class="cabecalho large">
Lei de Kirchoff das Correntes
</div>
<div class="conteudo regular">

A Lei de Kirchhoff das Correntes diz que a soma das correntes que entram em um nó de um circuito tem de ser igual a soma das correntes que saem dele:

$$
    \sum{i_{\text{entrada}}} = \sum{i_{\text{saida}}}
$$

Considerando o nó abaixo, temos as correntes $i_{1}, i_{3} \text{ e } i_{4}$ entrando no nó, enquanto as correntes $i_{2} \text{ e } i_{5}$ saem dele.

<img class="transparent" src="https://diegoascanio.github.io/ace-aula-02/img/entrada_saida_correntes.png">

Assim, $i_{1} + i_{3} + i_{4} = i_{2} + i_{5}$

</div>


---

<!-- _class: lead -->
# Lei de Kirchoff das Tensões em Uma Malha


---

<div class="cabecalho large">
Lei de Kirchoff das Tensões 
</div>
<div class="two-columns-50-50">

<div class="regular">

A Lei de Kirchhoff das Tensões diz que a soma das $n$ tensões presentes em (em torno de) uma malha fechada é zero:

$$
    \sum_{n}{V_{n}} = 0 
$$

A Lei de Kirchhoff das Tensões também pode ser descrita de outra forma: A soma dos aumentos de tensão é igual à soma das quedas de tensão em torno de uma malha fechada:
<!-- Guardem isso, pois, isso é de suma importância! -->

$$
    \sum_{V_{\text{aumento}}} = \sum_{V_{\text{queda}}} 
$$


</div>

<div class="small">

<center>
<img class="transparent" src="https://cdn.kastatic.org/ka-perseus-images/ffdd00057828a3dd41a6ed563b2da30a22add4bd.svg">
</center>

Observe as setas laranjas, as que transitam de negativo pra positivo, representam um aumento de tensão. As que transitam de positivo para negativo, uma diminuição (subtração) da tensão.

Escrevendo a LKT desta malha pela primeira equação: $+20V - 2V - 4V - 6V - 8V = 0V$.

Considerando que a soma das tensões de queda é de $20V$, pela segunda equação, temos que $20V = 2V + 4V + 6V + 8V$

</div>

</div>


---

<!-- _class: lead -->
# Lembrete nº 2

<!-- _class: lead -->
## Não Adianta a Sua Matemática Estar Correta se Seu Modelo Estiver Errado!

<!-- _class: lead -->
Um circuito só está resolvido quando os valores das correntes e tensões de seus elementos são conhecidos!
