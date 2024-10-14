<style scoped>
    p {
        font-size: 18px;
        text-align: justify;
    }
    h2 {
        font-size: 22px;
    }
    .flex-container {
        display: flex;
    }
    .flex-container > figure {
        flex: 1;
    }
    img {
        width: 100%;
    }
    .flex-container > p {
        flex: 3;
    }
    figcaption {
        text-align: center;
        font-size: 10px;
    }
</style>

## Método das tensões dos nós

<div class="flex-container">
<figure>
<img src="https://i.imgur.com/z21SbFS.png" class="transparent">
<figcaption>Figura 2 - Elemento de Exemplo</figcaption>
</figure>
<p>
O que torna o método dos nós possível? A lei de ohm, que diz que a corrente de um elemento é dada pela razão da diferença de potencial a qual está submetida sobre sua resistência. 
</p>
</div>

Essa diferença de potencial V é sempre dada pela tensão em um ponto A (\\(V\_A\\)) menos a tensão de um ponto B (\\(V\_B\\)) — \\(V = V\_A - V\_B\\). Logo, para o elemento de exemplo da Figura 2:

\\[ i = {{V\_A - V\_B}\over{R}} \\]

Generalizando isto para todos os elementos de um circuito que convergem em um nó qualquer, conseguimos escrever a lei de kirchhoff das correntes para um nó em função das tensões dos elementos que convergem nele!


Ao permitir analisar correntes em funções das tensões dos nós, as equações da lei de kirchoff da tensão ficam implicitas no método das tensões dos nós e portanto, são eliminadas das análises, diminuindo o número de equações e consequentemente, simplificando o sistema, demonstrando assim a sua desejabilidade!
