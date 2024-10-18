<style scoped>
    table {
        font-size: 16px;
        margin-left: auto;
        margin-right: auto;
    }
    p, li {
        text-align: justify;
        font-size: 16px;
    }
    figcaption {
        font-size: 12px;
        text-align: center;
    }
    h2 {
        text-align: center;
        font-size: 28px;
    }
    h3 {
        text-align: center;
        font-size: 16px;
    }
    .flex-container {
        display: flex;
        align-items: center;
    }
    .flex-container > div {
        margin-right: 10px;
    }
    .left-element {
        flex: 3;
    }
    .right-element {
        flex: 1;
    }
    .flex-column {
        flex: 1;
    }
</style>

## Método das Correntes das Malhas - Passo 2

<div class="flex-container">
<div class="flex-column">

Através do método das correntes da malha, determine a potência dissipada pelo resistor de $4\Omega$.

2. Para cada resistor \\(R\\) dos \\(N\\) resistores do circuito, escreva sua corrente \\(i\_{R\_j} | j = 1 \ldots N \\) em função das correntes de malha que transitam sobre ele. Seus sentidos também são arbitrários, por isso, considere a tensão no ponto de entrada da corrente no resistor \\(i\_{R\_j}\\\) maior que a tensão no ponto de saída; Atribua um sinal de positivo no ponto da entrada da corrente e um sinal de negativo no ponto de saída;

### Resistor de $5\Omega$

Arbitramos para a corrente \\(i_{5\Omega}\\) o sentido da esquerda para a direia, como mostra o circuito ao lado.

No resistor de \\(5\Omega\\), vemos que a corrente \\(i_1\\) da malha 1 entra na esquerda e sai pela direita, já a da malha 2, \\(i_2\\), no sentido oposto, da direita para a esquerda. Assim, a corrente \\(i_{5\Omega}\\) que passa pelo resistor de \\(5\Omega\\) é a diferença entre as correntes \\(i_1\\) e \\(i_2\\), ou seja:

\\[i_{5\Omega} = i_1 - i_2\\]

</div>
<div class="flex-column">

<!-- _class: transparent -->

![](img/circuit-step-2.png)

</div>
</div>
