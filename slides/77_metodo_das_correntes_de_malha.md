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

### Resistor de $4\Omega$

Arbitramos para a corrente \\(i_{4\Omega}\\) o sentido da direita para a esquerda, como mostra o circuito ao lado.

No resistor de \\(4\Omega\\), vemos que a corrente \\(i_2\\) da malha 2 entra na direita e sai pela esquerda, já a da malha 3, \\(i_3\\), no sentido oposto, da esquerda para a direita. Assim, a corrente \\(i_{4\Omega}\\) que passa pelo resistor de \\(5\Omega\\) é a diferença entre as correntes \\(i_2\\) e \\(i_3\\), ou seja:

\\[i_{4\Omega} = i_2 - i_3\\]

### Resistor de $20\Omega$

Arbitramos para a corrente \\(i_{20\Omega}\\) o sentido da esquerda para a direia, como mostra o circuito ao lado.

No resistor de \\(20\Omega\\), vemos que a corrente \\(i_1\\) da malha 1 entra por cima e sai por baixo, já a da malha 3, \\(i_3\\), no sentido oposto, de baixo para cima. Assim, a corrente \\(i_{20\Omega}\\) que passa pelo resistor de \\(20\Omega\\) (que também é \\(i_{\phi}\\) é a diferença entre as correntes \\(i_1\\) e \\(i_3\\), ou seja:

\\[i_{20\Omega} = i_{\phi} = i_1 - i_3\\]


</div>
<div class="flex-column">

<!-- _class: transparent -->

![](img/circuit-step-2.png)

</div>
</div>
