<style scoped>
    p, li {
        text-align: justify;
        font-size: 14pt;
    }
</style>

## Método da Tensão nos Nós — Exemplo e Algortimo

O cerne do método das tensões dos nós está em encontrar as diferenças de potencial nos nós de um circuito em relação ao nó de referência e a partir destas tensões, especificar as correntes que transitam pelos nós do circuito em função de tal tensão. Portanto, o método pode ser sistematizado em 6 passos:

1. Identificar todos os nós do circuito atribuindo nomes (letras latinas, gregas, etc) a cada um deles;
2. Escolher um nó de referência;
    - Uma boa escolha de nó de referência é aquele que permite calcular de imediato a tensão nodal de outro nó — exemplo, um nó que esteja ligado ao terminal de uma fonte de tensão — ou na ausência de tal nó, um nó que esteja ligado ao maior número de elementos possíveis do circuito;
        - Escolher um nó de referência que permita encontrar de imediato a tensão nodal de outro(s) nó(s) reduz o número de equações a serem resolvidas;
3. Atribuir tensões a todos os outros nós em relação ao nó de referência;
    - Se forem nós cujos caminhos ao nó de referência possuam apenas fontes de tensão, a tensão é conhecida e deve ser atribuída como tensão do nó o valor da(s) fonte(s) de tensão conhecidas;
    - Senão, atribuir uma variável de tensão ao nó — exemplo: \\(V\_k\\) para o nó de nome \\(k\\);
