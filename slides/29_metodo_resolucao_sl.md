
## Algoritmo

### Passo 7

<div class="grid-50-50">
<div class="grid-element small">

4. Na equação $V_{M_{1}} = -R \cdot i_{2} + \cdots = 0$, as reticências ($\cdots$) representam as tensões dos outros elementos que existem na malha mas que ainda não foram calculadas. Para continuar o procedimento, repita a análise dos sinais da tensão no próximo elemento a ser visitado e adicione a tensão deste elemento conforme o sinal que ele apresenta. Repita este processo quantas vezes forem necessárias até que todos os elementos da malha tenham sido visitados.

Aplicando o procedimento para os próximos elementos a serem visitados $-$ $R = 30 \Omega$ e a fonte de $125 V$ $-$ no resistor de $30 \Omega$ a tensão diminui, portanto:
$$ V_{M_{1}} = -R \cdot i_{2} - 30 \Omega \cdot i_{4} + \cdots = 0 $$

Na fonte de $125 V$, o sentido escolhido faz a tensão aumentar (vai do do $-$ para o $+$). Portanto:

$$ V_{M_{1}} = -R \cdot i_{2} - 30 \Omega \cdot i_{4} + 125 V = 0 $$

</div>
<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>
</div>

