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
        flex: 1;
        margn-right: 10px;
        font-size: 18pt;
        text-align: justify;
    }
    .flex-image {
        flex: 2;
    }
</style>

## Método das Tensões dos Nós - Passo 3 - Escolha do Nó de Referência

<div class="flex-container">
<div class="flex-paragraph">

Passo 2 - Escolha do nó de referência

Escolhemos como nó de referência o nó α por ele permitir deduzir de imediato a tensão nodal do nó δ — \\(V_\delta = 5V\\) — elminando desta forma duas equações de dois nós (o de referência, tensão \\(0V\\), e o nó δ com tensão \\(V_\delta = 5V\\)) do sistema de equações a resolver.

</div>
<div class="flex-image">

<!-- _class: transparent -->
![](img/exemplo-tensao-dos-nos-passo-2.png)

</div>
</div>
