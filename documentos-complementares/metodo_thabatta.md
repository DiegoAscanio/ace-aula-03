# Método Thabatta para determinação do sentido das correntes e das equações de malha para a obtenção de equações lineares que resolvem um circuito resistivo.

Consideramos que um circuito está resolvido quando sabemos todos os valores de seus componentes e das correntes que circulam por eles, pois aí, conseguimos derivar as demais grandezas de interesse.

## Algoritmo (passo-a-passo) 

1. Determine quais são os elementos (resistores e fontes) do circuito;
2. Determine quais são os nós do circuito (ponto onde dois ou mais elementos se juntam);
3. Determine quais são as malhas (Caminhos (laços) cujos nó inicial e final se coincidem sem englobar nenhum outro laço) do circuito;
4. Escreva as correntes que entram e saem dos elementos dos circuitos (resistores principalmente) levando em consideração as quedas de tensão provocadas pelos elementos resistivos. Este ponto é essencial, acima de cada resistor, desenhe um sinal de positivo (+) no ponto onde a corrente entra nele e um sinal de negativo (-) no ponto onde a corrente sai dele, para simbolizar uma queda de tensão.
5. Escreva as correntes que entram e saem dos nós levando em consideração a lei de kirchoff da corrente, que estabelece que a soma das correntes que entram em um nó é igual a soma das correntes que saem.
6. Escreva as diferenças de potencial existentes em uma malha levando em consideração a lei de kirchoff da tensão, que estabelece que a soma das diferenças de potencial dos elementos de uma malha é igual a zero. Aqui a sinalização dos pontos onde ocorrem quedas de pontecial nos resistores será essencial, pois, se em um ponto da malha, o caminho da malha se mover de um ponto de menor tensão (-) para um ponto de maior tensão (+) em um resistor, você deve considerar um aumento de tensão nesse caminho. Se o caminho se mover de um ponto de maior tensão para um ponto de menor tensão, você deve considerar um decréscimo de tensão no caminho da malha.
7. A partir das equações obtidas em 6 e 7, se você seguiu o método corretamente, você produziu um modelo matemático adequado para o comportamento de circuito e ele pode ser resolvido através de sistemas lineares.

Considerando o circuito da figura abaixo:


