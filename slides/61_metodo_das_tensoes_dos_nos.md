<style scoped>
    p, li {
        text-align: justify;
        font-size: 14pt;
    }
</style>

## Método da Tensão nos Nós — Exemplo e Algoritmo

O cerne do método das tensões dos nós está em encontrar as diferenças de potencial nos nós de um circuito em relação ao nó de referência e a partir destas tensões, especificar as correntes que transitam pelos nós do circuito em função de tal tensão. Portanto, o método pode ser sistematizado em 6 passos:

4. Atribuir correntes (sentidos arbitrários) para todos os elementos do circuito (fontes e resistores, por hora) e quando possível, escrever tais correntes em função das tensões que entram e que saem destes elementos (apenas nos resistores no caso) a partir da lei de Ohm que especifica que:

\\[
    i_\text{ab} = \frac{v_\text{ab}}{R} = \frac{v_\text{a} - v_\text{b}}{R}
\\]

5. Para cada um dos nós cujas tensões sejam desconhecidas:
    - Escrever a LKC para o nó em questão, considerando as correntes que entram e que saem do nó em função das tensões nodais desconhecidas, quando aplicável, e em função das correntes oriundas de fontes de corrente e das correntes oriundas de fontes de tensão, também quando aplicável.
6. Construir um sistema de equações lineares a partir das equações de LKC escritas para cada nó desconhecido e resolver tal sistema para encontrar as tensões nodais desconhecidas, resolvendo desta forma o circuito.
