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

## Método das Tensões dos Nós - Passo 4

<div class="flex-container">
<div class="flex-paragraph">

4. Atribuir correntes (sentidos arbitrários) para todos os elementos do circuito (fontes e resistores, por hora) e quando possível, escrever tais correntes em função das tensões que entram e que saem destes elementos (apenas nos resistores no caso) a partir da lei de Ohm que especifica que \\(i\_{ab} = \frac{v\_{ab}}{R\_{ab}} = \frac{V\_a - V\_b}{R\_{ab}} \\).

Correntes atribuídas, seus sentidos e sua forma em função das tensões de nós, quando possível:

<div class="flex-container">
<div class="flex-column">

|   Corrente   |              Sentido              |                        Forma em função<br/>das<br/>tensões de nós                        |
| :----------: | :-------------------------------: | :--------------------------------------------------------------------------------------: |
|   \\(I\\)    | \\( \alpha \rightarrow \delta \\) |                                      Não é possível                                      |
| \\(i\_{1}\\) | \\( \alpha \rightarrow \beta \\)  | \\(i\_{1} = \frac{V\_{\alpha} - V\_{\beta}}{4 \Omega} = \frac{- V\_{\beta}}{4 \Omega}\\) |
| \\(i\_{2}\\) | \\( \beta \rightarrow \gamma \\)  |                 \\(i\_{2} = \frac{V\_{\beta} - V\_{\gamma}}{3 \Omega}\\)                 |

</div>
<div class="flex-column">

|   Corrente   |              Sentido              |                              Forma em função<br/>das<br/>tensões de nós                               |
| :----------: | :-------------------------------: | :---------------------------------------------------------------------------------------------------: |
| \\(i\_{3}\\) | \\( \gamma \rightarrow \beta \\)  |                       \\(i\_{3} = \frac{V\_{\gamma} - V\_{\beta}}{6 \Omega}\\)                        |
| \\(i\_{4}\\) | \\( \delta \rightarrow \beta \\)  |      \\(i\_{4} = \frac{V\_{\delta} - V\_{\beta}}{7 \Omega} = \frac{5 - V\_{\beta}}{7 \Omega} \\)      |
| \\(i\_{5}\\) | \\( \gamma \rightarrow \delta \\) | \\(i\_{5} = \frac{V\_{\gamma} + 9 - V\_{\delta}}{8 \Omega} \therefore \\) <br> \\( i\_{5} = \frac{V\_{\gamma} + 9 - 5}{8 \Omega} = \frac{V\_{\gamma} + 4}{8 \Omega} \\) |

</div>
</div>
</div>
<div class="flex-image">

<!-- _class: transparent -->

![](img/exemplo-tensao-dos-nos-passo-4.png)

</div>
</div>
