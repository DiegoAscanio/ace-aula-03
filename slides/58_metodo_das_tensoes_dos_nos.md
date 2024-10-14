<style scoped>
    p {
        text-align: justify;
        font-size: 20px;
    }
    figcaption {
        font-size: 12px;
        text-align: center;
    }
    h2 {
        font-size: 24px;
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
</style>

## Método das Tensões dos Nós

É um método para análise (e solução) de circuitos elétricos que busca a descoberta de grandezas desconhecidas dos elementos (ex. correntes e tensões) à partir das tensões existentes entre nós (pontos de encontro de dois ou mais elementos) de um circuito elétrico.

É desejável porque simplifica a solução de circuitos — em comparação às leis de kirchoff da corrente nos nós e da tensão nas malhas — ao permitir que a lei de kirchoff das correntes nos nós seja escrita em função das tensões que estes nós apresentam em relação a um nó de referência.

<div class="flex-container">
<div class="left-element">
<p>Um nó de referência é um ponto de partida — normalmente o nó com a maior quantidade de elementos — conectado ao referencial nulo (terra) através do qual pode-se calcular as diferenças de potencial em relação aos demais nós do circuito a partir das quedas (ou subidas) de tensão ocasionadas pelos elementos existentes entre o nó de referência e nó que se deseja descobrir a tensão.</p>
</div>
<div class="right-element">
<figure>
<img src="https://i.imgur.com/qHiTLLH.png" class="transparent" alt="grid-img">
<figcaption>Figura 1 - Exemplo de Nó de Referência.
</figcaption>
</figure>
</div>
</div>
