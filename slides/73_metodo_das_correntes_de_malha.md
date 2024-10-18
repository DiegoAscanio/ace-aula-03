<style scoped>
    p, li {
        text-align: justify;
        font-size: 18px;
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
    .flex-column {
        flex: 1;
    }
</style>

## Método das Correntes das Malhas

### Algoritmo

<div class="flex-container">
<div class="flex-column">

1. Identifique as \\(M\\) malhas do circuito, enumere-as e atribua uma corrente de malha \\(i\_k | k = 1 \ldots M \\) — com sentido arbitrário — a cada uma delas;
2. Para cada resistor \\(R\\) dos \\(N\\) resistores do circuito, escreva sua corrente \\(i\_{R\_j} | j = 1 \ldots N \\) em função das correntes de malha que transitam sobre ele. Seus sentidos também são arbitrários, por isso, considere a tensão no ponto de entrada da corrente no resistor \\(i\_{R\_j}\\\) maior que a tensão no ponto de saída; Atribua um sinal de positivo no ponto da entrada da corrente e um sinal de negativo no ponto de saída;

</div>
<div class="flex-column">

3. Para cada malha do circuito escreva LKT considerando em cada malha:
    - As quedas (ou elevações) de tensão causadas pelo trânsito das correntes nos resistores;
    - As quedas (ou elevações) de tensão causadas pelas fontes de tensão;
    - As quedas (ou elevações) de tensão causadas pelas fontes de corrente;
4. Simplifique até quando possível as equações obtidas, construa um sistema de equações lineares e resolva-o para encontrar as grandezas incógnitas do circuito.

</div>
</div>
