
<style>
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
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

---

# Método para determinação do sentido das correntes e das equações de malha para a obtenção de equações lineares que resolvem um circuito resistivo.

Consideramos que um circuito está resolvido quando sabemos todos os valores de seus componentes e das correntes que circulam por eles, pois aí, conseguimos derivar as demais grandezas de interesse.

---

## Algoritmo (passo-a-passo) 

Dado um circuito qualquer:

1. Determine quais são os elementos (resistores e fontes) do circuito;
2. Determine quais são os nós do circuito (ponto onde dois ou mais elementos se juntam);
3. Determine quais são as malhas (Caminhos (laços) cujos nó inicial e final se coincidem sem englobar nenhum outro laço) do circuito;
4. Levando em conta a lei de Kirchhoff da corrente, que afirma que a soma das correntes entrando em um nó é igual àquelas que saem, identifique as correntes dos elementos do circuito e onde ocorrem quedas ou aumentos de tensão. 
    - **ESSENCIAL:** Nos resistores, assinale um sinal positivo no ponto onde a corrente entra (maior tensão) e um negativo onde ela sai (menor tensão). Por fim, assinale os sinais positivos e negativos aos respectivos polos da(s) fonte(s). 
---

## Algoritmo (passo-a-passo) 

5. Escreva as diferenças de potencial existentes em uma malha levando em consideração a lei de kirchoff da tensão, que estabelece que a soma das diferenças de potencial dos elementos de uma malha é igual a zero.
    - Aqui a sinalização dos pontos onde ocorrem quedas de pontecial nos resistores será essencial, pois:
        - Se em um ponto da malha, o caminho da malha se mover de um ponto de menor tensão (-) para um ponto de maior tensão (+) em um resistor, você deve considerar um aumento de tensão nesse caminho. 
        - Se o caminho se mover de um ponto de maior tensão para um ponto de menor tensão, você deve considerar um decréscimo de tensão no caminho da malha.
6. A partir das equações de corrente obtidas em 4 e 5, se você seguiu o método corretamente, você produziu um modelo matemático adequado para o comportamento de circuito e ele pode ser resolvido através de sistemas lineares. 

**Lembrando: Não adianta sua matemática estar correta se seu modelo estiver errado!**

---

## Algoritmo

### Passo 1

Considerando o circuito da figura abaixo, queremos resolvê-lo calculando o valor de todas as correntes de seus componentes em função do resistor de valor desconhecido \\(R\\). **Para resolver o circuito ao final do algoritmo, bem como encontrar o valor de \\(R\\), sabemos que no resistor de \\(30 \Omega\\) passa uma corrente de \\(1A\\).**

Ao aplicar o passo 1 do algoritmo, os resistores identificados encontram-se contornados por linhas vermelhas e a fonte identificada por uma linha laranja:

![Circuito Original](./img/circuito_original.png)

---

## Algoritmo

### Passo 2

Ao aplicar o passo 2, identificamos 4 nós \\( N_{1}, N_{2}, N_{3} \text{ e } N_{4} \\) (em verde escuro) no circuito.

![Identificação dos Nós](./img/circuito_nos_identificados.png)

--- 

## Algoritmo

### Passo 3

Ao aplicar o passo 3, identificamos 3 Malhas \\(M_{1}, M_{2} \text{ e } M_{3}\\) (em azul) no circuito.

![Identificação das Malhas](./img/circuito_malhas_identificadas.png)

---

## Algoritmo

### Passo 4

Levando em conta a lei de Kirchhoff da corrente, que afirma que a soma das correntes entrando em um nó é igual àquelas que saem, identifique as correntes dos elementos do circuito e onde ocorrem quedas ou aumentos de tensão. 
- **ESSENCIAL:** Nos resistores, assinale um sinal positivo no ponto onde a corrente entra (maior tensão) e um negativo onde ela sai (menor tensão). Por fim, assinale os sinais positivos e negativos aos respectivos polos da(s) fonte(s). 

Cada elemento no circuito tem uma corrente que passa por ele. Começando pela fonte do circuito, temos uma corrente \\( i_{0} \\) que flui do polo negativo da fonte em direção ao polo positivo. A corrente \\(i_{0}\\) entra no nó \\(N_{1}\\) e nesse nó ocorre uma ramificação do circuito para duas resistências: a resistência de valor indeterminado \\( R \\) e a resistência de \\( 30 \Omega \\). 

![](./img/circuito_n_1.png)

Considerando a corrente que flui pelo resistor de \\( 30 \Omega \\) como \\( i_{1} \\) e a corrente que flui por \\(R\\) como \\(i_{2}\\), como ambas \\( i_{1} \text{ e } i_{2} \\) saem do nó \\( N_{1} \\) e existe uma corrente \\( i_{0} \\) que chega a este nó assim, pela LKC, \\( i_{0} = i_{1} + i_{2} \\). 

---

## Algoritmo

### Passo 4

Continuando a análise do circuito, verificamos que entre os nós \\( N_{1} \\) e \\( N_{2} \\) os resistores de \\( 30 \Omega \\) e de \\( 20 \Omega \\) estão em série, e portanto, possuem a mesma corrente \\( i_{1} \\). Verificamos também que um resistor de \\( 15 \Omega \\) conecta os nós \\( N_{2} \\) e \\( N_{3} \\), existindo assim, uma corrente que circula neste elemento. O sentido de circulação da corrente deve ser definido arbitrariamente (a seu critério) e você pode definir tanto uma corrente \\( i_{3} \\) que flui de \\( N_{2} \\) para \\( N_{3} \\) (direita para a esquerda) quanto de \\( N_{3} \\) para \\( N_{2} \\) (esquerda para a direita).

Nessa resolução, arbitraremos que a corrente \\( i_{3} \\) flui de \\( N_{3} \\) para \\( N_{2} \\). Agora, escreveremos as equações da lei de Kirchhoff para a corrente para os nós \\( N_{3} \\) e \\( N_{2} \\) respectivamente. 
- No nó \\( N_{3} \\) chega a corrente corrente \\( i_{2} \\) que se divide para as correntes \\( i_{3} \\) — que flui de \\( N_{3} \\) para \\( N_{2} \\) — e \\( i_{4} \\) que passa no resistor de \\( 15 \Omega \\) entre \\( N_{3} \\) e \\( N_{4} \\).
    - Assim, a LKC no nó \\(N_{3}\\) estabelece que \\( i_{2} = i_{3} + i_{4} \\).
- No nó \\( N_{2} \\) chegam as correntes \\( i_{1} \\) e \\( i_{3} \\) e sai uma corrente \\( i_{5} \\) em direção aos dois resistores em série de \\(10 \Omega\\) entre \\(N_{2}\\) e \\(N_{4}\\).
    - Assim, a LKC no nó \\(N_{2}\\) estabelece que \\( i_{5} = i_{1} + i_{3} \\)

![](./img/circuito_final.png)

Por fim, em \\( N_{4} \\) entram as correntes \\( i_{5} \\) e \\( i_{4} \\) que somadas produzem \\( i_{0} \\) (que sai de \\(N_{4}\\)). Logo, \\( i_{4} + i_{5} = i_{0} \\), porém essa equação não será utilizada, pois, é uma combinação das outras três equações de nós obtidas até o momento. Agora, devemos passar ao passo 5 - escrever as equações das tensões nas malhas \\(M_{1}, M_{2} \text{ e } M_{3}\\) com base na lei de kirchoff da tensão.

---

<div class="grid-50-50">

<div class="grid-element">

## Algoritmo

### Passo 5

Agora, devemos fazer as equações das tensões nas malhas pelos princípios da LKT que preconizam que a soma das diferenças de potencial em uma malha é sempre nula. Existe um subalgoritmo deste passo para fazer a resolução que para cada malha do circuito determina que você:

1. Escolha um elemento da malha como elemento atual
    - Na malha \\(M_{1}\\), vamos escolher o elemento \\(R\\).
2. Escolha um sentido (horário ou anti-horário) para percorrer a malha a partir do elemento escolhido. Escolheremos o sentido horário.

</div>

<div class="grid-element">

![grid-img](./img/circuito_final.png)

</div>

</div>

---

<div class="grid-50-50">

<div class="grid-element">

## Algoritmo

### Passo 5

3. **(ESSENCIAL)** Avalie os sinais da diferença de potencial do elemento no sentido escolhido para percorrer a malha. <!-- Em \( R \) no sentido horário a tensão vai do sentido positivo ao negativo, portanto, diminuindo. se fosse no sentido anti horário, a tensão no elemento iria do negativo para o positivo, portanto, aumentando -->
    1. Se no sentido escolhido a tensão diminuir — for do \\(+\\) para o \\(-\\) — então coloque a tensão deste elemento como negativa na equação da malha avaliada.
    2. Se no sentido escolhido a tensão aumentar — for do \\(-\\) para o \\(+\\) — então coloque a tensão deste elemento como positiva na equação da malha avaliada.
- No nosso elemento atual \\( R \\) no sentido horário a tensão diminui. Portanto adicionamos a tensão negativa deste elemento na equação da malha \\( M_{1} \\)

</div>

<div class="grid-element">

![grid-img](./img/circuito_final.png)

</div>

</div>

---

<div class="grid-50-50">
<div class="grid-element">

## Algoritmo

### Passo 5

4. Na equação \\( V_{M_{1}} = -R \cdot i_{2} + \cdots = 0 \\), as reticências (\\( \cdots \\)) representam as tensões dos outros elementos que existem na malha mas que ainda não foram calculadas. Para continuar o algoritmo, escolha o próximo elemento não visitado no sentido escolhido para percorrer a malha como elemento atual.
5. repita os passos 3 e 4 do subalgoritmo do passo 5 até que todos os elementos da malha tenham sido visitados.

Aplicando o algoritmo para os próximos elementos a serem visitados \\( R = 15 \Omega \\) e a fonte de \\( 350 V \\) no resistor de \\(15 \Omega \\) a tensão diminui, portanto:
\\[ V_{M_{1}} = -R \cdot i_{2} - 15 \Omega \cdot i_{4} + \cdots = 0 \\]

Na fonte de \\( 350 V \\), o sentido escolhido faz a tensão aumentar (vai do do \\(-\\) para o \\(+\\)). Portanto:

\\[ V_{M_{1}} = -R \cdot i_{2} - 15 \Omega \cdot i_{4} + 350 V = 0 \\]

</div>
<div class="grid-element">

![grid-img](./img/circuito_final.png)

</div>
</div>

---

<div class="grid-50-50">
<div class="grid-element">

## Algoritmo

### Passo 5

Aplicando o passo 5 para as próximas malhas no sentido horário temos que:

\\[ 
\begin{align}
    V_{M_{2}} &= -30 i_{1} - 20 i_{1} + 15 i_{3} + R i_{2} = 0 \\\\
    V_{M_{3}} &= -10 i_{5} - 10 i_{5} + 15 i_{4} - 15 i_{3} = 0 \\\\
\end{align}
\\]

</div>
<div class="grid-element">

![grid-img](./img/circuito_final.png)

</div>
</div>

---

## Algoritmo

## Passo 6

Tendo obtido equações dos elementos dos circuitos através da LKC e da LKC, obtemos:

\\[
\begin{align}
    &i_{0} = i_{1} + i_{2} \\\\
    &i_{2} = i_{3} + i_{4} \\\\
    &i_{5} = i_{1} + i_{3} \\\\
    &-R \cdot i_{2} - 15 \Omega \cdot i_{4} + 350V = 0 \\\\
    &-30 i_{1} - 20 i_{1} + 15 i_{3} + R i_{2} = 0 \\\\
    &-10 i_{5} - 10 i_{5} + 15 i_{4} - 15 i_{3} = 0
\end{align}
\\]

---

## Algoritmo

## Passo 6

Reorganizando as equações do circuito para construir um sistema linear terminamos o algoritmo de modelagem.

\\[
\begin{cases}
    &1 i_{0} - 1 i_{1} - 1 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\\\
    &0 i_{0} + 0 i_{1} + 1 i_{2} - 1 i_{3} - 1 i_{4} + 0 i_{5} &= 0\\\\
    &0 i_{0} - 1 i_{1} + 0 i_{2} - 1 i_{3} + 0 i_{4} + 1 i_{5} &= 0\\\\
    &0 i_{0} + 0 i_{1} - R i_{2} + 0 i_{3} - 15 i_{4} + 0 i_{5} &= -350\\\\
    &0 i_{0} - 50 i_{1} + R i_{2} + 15 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\\\
    &0 i_{0} + 0 i_{1} + 0 i_{2} - 15 i_{3} + 15 i_{4} - 20 i_{5} &= 0\\\\
\end{cases}
\\]

---

## Resolução do Circuito

Agora, devemos reescrever o sistema em sua representação matricial e usar um sistema computacional de álgebra linear simbólica (sympy do python) para nos auxiliar a resolver esse circuito e encontrar as correntes em função do resistor \\(R\\) desconhecido:

\\[
\begin{bmatrix}
    1 & -1 & -1 & 0 & 0 & 0 & 0 \\\\
    0 & 0 & 1 & -1 & -1 & 0 & 0\\\\
    0 & -1 & 0 & -1 & 0 & 1 & 0\\\\
    0 & 0 & -R & 0 & -15 & 0 & -350\\\\
    0 & -50 & R & 15 & 0 & 0 & 0\\\\
    0 & 0 & 0 & -15 & 15 & -20 & 0
\end{bmatrix}
\\]

---

