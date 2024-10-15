<style scoped>
    img {
      width: 100%;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
    .flex-container {
      display: flex;
      justify-content: space-between;
    }
    .flex-paragraph {
        flex: 2;
        margin-right: 10px;
        text-align: justify;
    }
    .flex-column {
        flex: 1;
        margin-right: 10px;
    }
    .flex-image {
        flex: 2;
    }
    li, p, table {
        font-size: 12pt;
    }
    table {
        margin-left: auto;
        margin-right: auto;
    }
</style>

## Método das Tensões dos Nós - Passo 5

<div class="flex-container">
<div class="flex-paragraph">

Para cada um dos nós cujas tensões sejam desconhecidas:

-   Escrever a LKC para o nó em questão, considerando as correntes que entram e que saem do nó em função das tensões nodais desconhecidas, quando aplicável, e em função das correntes oriundas de fontes de corrente e das correntes oriundas de fontes de tensão, também quando aplicável. No caso, temos os nós β e γ com tensões desconhecidas.

| Nó  |           Correntes que entram         | Correntes que saem | LKC com correntes<br/>em função das tensões nodais<br/>(Quando Aplicável) |
| :-: | :------------------------------------: | :----------------: | :-----------------------------------------------------------------------: |
|  β  | \\( 2A, i\_1, i\_3 \text{ e } i\_4 \\) |   \\( i\_2 \\)     | \\( 2 - \frac{V\_{\beta}}{4} + \frac{V\_{\gamma} - V\_{\beta}}{6} + \frac{5 - V\_{\beta}}{7} = \frac{V\_{\beta} -  V\_{\gamma}}{3} \\) |
|  γ  | \\( i\_2 \\) |   \\( i\_3 \text{ e } i\_5 \\)  | \\( \frac{V\_{\beta} -  V\_{\gamma}}{3} = \frac{V\_{\gamma} - V\_{\beta}}{6} + \frac{V\_{\gamma} + 4}{8} \\) |

Vemos que apenas duas variáveis são desconhecidas, \\( V\_{\beta} \\) e \\( V\_{\gamma} \\), e que temos duas equações. Assim, podemos resolver o sistema de equações para encontrar as tensões nodais desconhecidas.

</div>
<div class="flex-image">

<!-- _class: transparent -->

![](img/exemplo-tensao-dos-nos-passo-4.png)

</div>
</div>
