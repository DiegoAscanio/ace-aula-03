<style>
  section {
    background: #fff url(./img/background.png) no-repeat center center;
    background-size: cover;
  }

  .transparent {
    background-color: transparent!important;
  }

  section.transparent img {
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

  .grid-50-50 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    text-align: justify;
  }
  .grid-element {
    margin-left: 5%;
    margin-right: 5%;
  }
  img[alt=grid-img] {
    width: 100%;
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
    1. Método para modelagem de circuitos em Sistemas de Equações Lineares
    2. Representação dos Sistemas de Equações Lineares em Sua Forma Matricial
    3. Resolução dos Modelos de Circuitos em Equações Lineares por Sistemas Computacionais de Álgebra (CAS - sympy, numpy)


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


---

# Método para determinação do sentido das correntes e das equações de malha para a obtenção de equações lineares que resolvem um circuito resistivo.

Consideramos que um circuito está resolvido quando sabemos todos os valores de seus componentes e das correntes que circulam por eles, pois aí, conseguimos derivar as demais grandezas de interesse.



---



## Algoritmo (passo-a-passo) 

<div class="normal">

Dado um circuito qualquer:

1. Determine quais são os elementos (resistores e fontes) do circuito;
2. Determine quais são os nós do circuito (ponto onde dois ou mais elementos se juntam);
3. Determine quais são as malhas (Caminhos (laços) cujos nó inicial e final se coincidem sem englobar nenhum outro laço) do circuito;
4. Levando em conta a lei de Kirchhoff da corrente, que afirma que a soma das correntes entrando em um nó é igual àquelas que saem, identifique as correntes dos elementos do circuito e onde ocorrem quedas ou aumentos de tensão. 
    - **ESSENCIAL:** Nos resistores, assinale um sinal positivo no ponto onde a corrente entra (maior tensão) e um negativo onde ela sai (menor tensão). Por fim, assinale os sinais positivos e negativos aos respectivos polos da(s) fonte(s). 

</div>


---

## Algoritmo (passo-a-passo) 

<div class="normal">

5. Escreva as diferenças de potencial existentes em uma malha levando em consideração a lei de kirchoff da tensão, que estabelece que a soma das diferenças de potencial dos elementos de uma malha é igual a zero.
    - Aqui a sinalização dos pontos onde ocorrem quedas de pontecial nos resistores será essencial, pois:
        - Se em um ponto da malha, o caminho da malha se mover de um ponto de menor tensão (-) para um ponto de maior tensão (+) em um resistor, você deve considerar um aumento de tensão nesse caminho. 
        - Se o caminho se mover de um ponto de maior tensão para um ponto de menor tensão, você deve considerar um decréscimo de tensão no caminho da malha.
6. A partir das equações de corrente obtidas em 4 e 5, se você seguiu o método corretamente, você produziu um modelo matemático adequado para o comportamento de circuito e ele pode ser resolvido através de sistemas lineares. 

**Lembrando: Não adianta sua matemática estar correta se seu modelo estiver errado!**

</div>


---

## Algoritmo

### Passo 1

<div class="grid-50-50">

<div class="grid-element normal">

Considerando o circuito da figura, queremos resolvê-lo calculando o valor de todas as correntes de seus componentes em função do resistor de valor desconhecido $R$. Ao aplicar o passo 1 do algoritmo, os resistores identificados encontram-se contornados por linhas vermelhas e a fonte identificada por uma linha laranja:

</div>

<div class="grid-element">

<!-- _class: transparent -->
![Circuito Original](./img/circuito_original.png)

</div>

</div>


---

## Algoritmo

### Passo 2

<div class="grid-50-50">

<div class="grid-element">

Ao aplicar o passo 2, identificamos 4 nós $N_{1}, N_{2}, N_{3} \text{ e } N_{4}$ (em verde escuro) no circuito.

</div>

<div class="grid-element">

<!-- _class: transparent -->
![Identificação dos Nós](./img/circuito_nos_identificados.png)

</div>

</div>


---

 

## Algoritmo

### Passo 3

<div class="grid-50-50">

<div class="grid-element">

Ao aplicar o passo 3, identificamos 3 Malhas $M_{1}, M_{2} \text{ e } M_{3}$ (em azul) no circuito.

</div>

<div class="grid-element">

<!-- _class: transparent -->
![Identificação das Malhas](./img/circuito_malhas_identificadas.png)

</div>

</div>


---



## Algoritmo

### Passo 4

<div class="grid-50-50">

<div class="grid-element footnotesize">

Levando em conta a lei de Kirchhoff da corrente, que afirma que a soma das correntes entrando em um nó é igual àquelas que saem, identifique as correntes dos elementos do circuito e onde ocorrem quedas ou aumentos de tensão. 
- **ESSENCIAL:** Nos resistores, assinale um sinal positivo no ponto onde a corrente entra (maior tensão) e um negativo onde ela sai (menor tensão). Por fim, assinale os sinais positivos e negativos aos respectivos polos da(s) fonte(s). 

Cada elemento no circuito tem uma corrente que passa por ele. Começando pela fonte do circuito, temos uma corrente $i_{0}$ que flui do polo negativo da fonte em direção ao polo positivo. A corrente $i_{0}$ entra no nó $N_{1}$ e nesse nó ocorre uma ramificação do circuito para duas resistências: a resistência de valor indeterminado $R$ e a resistência de $30 \Omega$. 

Considerando a corrente que flui pelo resistor de $30 \Omega$ como $i_{1}$ e a corrente que flui por $R$ como $i_{2}$, como ambas $i_{1} \text{ e } i_{2}$ saem do nó $N_{1}$ e existe uma corrente $i_{0}$ que chega a este nó assim, pela LKC:

<div class="normal">

$$ i_{0} = i_{1} + i_{2} $$

</div>

</div>

<div class="grid-element">

<!-- _class: transparent -->
![](./img/circuito_n_1.png)

</div>

</div>


---



## Algoritmo

### Passo 4

<div class="grid-50-50">

<div class="grid-element footnotesize" >

Continuando a análise do circuito, verificamos que entre os nós $N_{1}$ e $N_{2}$ os resistores de $30 \Omega$ e de $20 \Omega$ estão em série, e portanto, possuem a mesma corrente $i_{1}$. Verificamos também que um resistor de $15 \Omega$ conecta os nós $N_{2}$ e $N_{3}$, existindo assim, uma corrente que circula neste elemento. O sentido de circulação da corrente deve ser definido arbitrariamente (a seu critério) e você pode definir tanto uma corrente $i_{3}$ que flui de $N_{2}$ para $N_{3}$ (direita para a esquerda) quanto de $N_{3}$ para $N_{2}$ (esquerda para a direita).

Nessa resolução, arbitraremos que a corrente $i_{3}$ flui de $N_{3}$ para $N_{2}$. Agora, escreveremos as equações da lei de Kirchhoff para a corrente para os nós $N_{3}$ e $N_{2}$ respectivamente. 
- No nó $N_{3}$ chega a corrente corrente $i_{2}$ que se divide para as correntes $i_{3}$ — que flui de $N_{3}$ para $N_{2}$ — e $i_{4}$ que passa no resistor de $15 \Omega$ entre $N_{3}$ e $N_{4}$.
    - Assim, a LKC no nó $N_{3}$ estabelece que $i_{2} = i_{3} + i_{4}$.
- No nó $N_{2}$ chegam as correntes $i_{1}$ e $i_{3}$ e sai uma corrente $i_{5}$ em direção aos dois resistores em série de $10 \Omega$ entre $N_{2}$ e $N_{4}$.
    - Assim, a LKC no nó $N_{2}$ estabelece que $i_{5} = i_{1} + i_{3}$

Por fim, em $N_{4}$ entram as correntes $i_{5}$ e $i_{4}$ que somadas produzem $i_{0}$ (que sai de $N_{4}$). Logo, $i_{4} + i_{5} = i_{0}$, porém essa equação não será utilizada, pois, é uma combinação das outras três equações de nós obtidas até o momento. Agora, devemos passar ao passo 5 - escrever as equações das tensões nas malhas $M_{1}, M_{2} \text{ e } M_{3}$ com base na lei de kirchoff da tensão.

</div>

<div class="grid-element">

<!-- _class: transparent -->
![](./img/circuito_final.png)

</div>

</div>


---

## Algoritmo

### Passo 5

<div class="grid-50-50">

<div class="grid-element small">

Agora, devemos fazer as equações das tensões nas malhas pelos princípios da LKT que preconizam que a soma das diferenças de potencial em uma malha é sempre nula. Existe um subalgoritmo deste passo para fazer a resolução que para cada malha do circuito determina que você:

1. Escolha um elemento da malha como elemento atual
    - Na malha $M_{1}$, vamos escolher o elemento $R$.
2. Escolha um sentido (horário ou anti-horário) para percorrer a malha a partir do elemento escolhido. Escolheremos o sentido horário.

</div>

<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>

</div>



---


## Algoritmo

### Passo 5

<div class="grid-50-50">

<div class="grid-element small">

3. **(ESSENCIAL)** Avalie os sinais da diferença de potencial do elemento no sentido escolhido para percorrer a malha. <!-- Em \( R \) no sentido horário a tensão vai do sentido positivo ao negativo, portanto, diminuindo. se fosse no sentido anti horário, a tensão no elemento iria do negativo para o positivo, portanto, aumentando -->
    1. Se no sentido escolhido a tensão diminuir — for do $+$ para o $-$ — então coloque a tensão deste elemento como negativa na equação da malha avaliada.
    2. Se no sentido escolhido a tensão aumentar — for do $-$ para o $+$ — então coloque a tensão deste elemento como positiva na equação da malha avaliada.
- No nosso elemento atual $R$ no sentido horário a tensão diminui. Portanto adicionamos a tensão negativa deste elemento na equação da malha $M_{1}$. Assim:

$$ V_{M_{1}} = -R \cdot i_{2} + \cdots = 0 $$

</div>

<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>

</div>



---


## Algoritmo

### Passo 5

<div class="grid-50-50">
<div class="grid-element small">

4. Na equação $V_{M_{1}} = -R \cdot i_{2} + \cdots = 0$, as reticências ($\cdots$) representam as tensões dos outros elementos que existem na malha mas que ainda não foram calculadas. Para continuar o algoritmo, escolha o próximo elemento não visitado no sentido escolhido para percorrer a malha como elemento atual.
5. repita os passos 3 e 4 do subalgoritmo do passo 5 até que todos os elementos da malha tenham sido visitados.

Aplicando o algoritmo para os próximos elementos a serem visitados $R = 15 \Omega$ e a fonte de $350 V$ no resistor de $15 \Omega$ a tensão diminui, portanto:
$$ V_{M_{1}} = -R \cdot i_{2} - 15 \Omega \cdot i_{4} + \cdots = 0 $$

Na fonte de $350 V$, o sentido escolhido faz a tensão aumentar (vai do do $-$ para o $+$). Portanto:

$$ V_{M_{1}} = -R \cdot i_{2} - 15 \Omega \cdot i_{4} + 350 V = 0 $$

</div>
<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>
</div>



---



<div class="grid-50-50">
<div class="grid-element normal">

## Algoritmo

### Passo 5

Aplicando o passo 5 para as próximas malhas no sentido horário temos que:

$$ 
\begin{align}
    V_{M_{2}} &= -30 i_{1} - 20 i_{1} + 15 i_{3} + R i_{2} = 0 \\
    V_{M_{3}} &= -10 i_{5} - 10 i_{5} + 15 i_{4} - 15 i_{3} = 0 \\
\end{align}
$$

</div>
<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>
</div>
