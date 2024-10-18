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
    h3 {
        font-size: 22px;
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

## Método das Correntes das Malhas

É um método para análise (e solução) de circuitos elétricos que busca a descoberta de grandezas desconhecidas dos elementos (ex. correntes e tensões) à partir de correntes elétricas compostas existentes em malhas — caminhos fechados que não contém outros camnhos fechados dentro de si — de um circuito elétrico.

É desejável porque simplifica a solução de circuitos — em comparação às leis de kirchoff da corrente nos nós e da tensão nas malhas — ao permitir que a lei de kirchoff das tensões nas malhas nós seja escrita em função das correntes que transistam nas malhas.

### Fundamentos

Considerando a LKT nas malhas que estabelece que a soma algébrica das diferenças de potencial elétrico em uma malha é igual a zero e a lei de Ohm que estabelece que a tensão elétrica em um resistor é igual ao produto da resistência pelo valor da corrente que o atravessa \\((V = R \cdot I)\\), conseguimos, portanto, escrever a LKT nas malhas em função das correntes que transitam nas malhas — implicitando as equações da LKC nos nós — e, assim, diminuir a quantidade de equações a serem resolvidas para solucionar o circuito.

<div class="flex-container">
<div class="left-element">
</div>
<div class="right-element">
</div>
</div>
