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
        flex: 3;
        margn-right: 10px;
        text-align: justify;
    }
    .flex-image {
        flex: 2;
    }
    li, p {
        font-size: 12pt;
    }
</style>

## Método das Tensões dos Nós - Passo 3 - Atribuição de Tensões a Todos os Nós em Relação ao nó de referência.

<div class="flex-container">
<div class="flex-paragraph">

3. Atribuir tensões a todos os outros nós em relação ao nó de referência;
    - Se forem nós cujos caminhos ao nó de referência possuam apenas fontes de tensão, a tensão é conhecida e deve ser atribuída como tensão do nó o valor da(s) fonte(s) de tensão conhecidas;
    - Senão, atribuir uma variável de tensão ao nó — exemplo: \\(V\_k\\) para o nó de nome \\(k\\).

O nó de referência está sempre conectado ao terra e portanto, sua tensão é sempre \\(V_\alpha = 0V\\).

No nosso exemplo, apenas um nó possui caminho com apenas fonte(s) de tensão, o nó δ que está conectado ao nó α por uma fonte de tensão de 5V. 

Saindo de α até δ temos que: \\(V_\alpha + 5 = V_\delta \implies 0 + 5 = V_\delta \therefore V_\delta = 5V \\)

Os outros dois nós, β e γ, têm tensões desconhecidas, portanto atribuo a eles as tensões \\(V_\beta\\) e \\(V_\gamma\\), respectivamente. Logo, todas as tensões de nó são:

- Nó α: \\(V_\alpha = 0V\\)
- Nó β: \\(V_\beta\\)
- Nó γ: \\(V_\gamma\\)
- Nó δ: \\(V_\delta = 5V\\)

</div>
<div class="flex-image">

<!-- _class: transparent -->
![](img/exemplo-tensao-dos-nos-passo-2.png)

</div>
</div>
