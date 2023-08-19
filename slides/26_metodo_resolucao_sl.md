
## Algoritmo

### Passo 5

<div class="grid-50-50">
<div class="grid-element small">

4. Na equação $ V_{M_{1}} = -R \cdot i_{2} + \cdots = 0 $, as reticências ($ \cdots $) representam as tensões dos outros elementos que existem na malha mas que ainda não foram calculadas. Para continuar o algoritmo, escolha o próximo elemento não visitado no sentido escolhido para percorrer a malha como elemento atual.
5. repita os passos 3 e 4 do subalgoritmo do passo 5 até que todos os elementos da malha tenham sido visitados.

Aplicando o algoritmo para os próximos elementos a serem visitados $ R = 15 \Omega $ e a fonte de $ 350 V $ no resistor de $15 \Omega $ a tensão diminui, portanto:
$$ V_{M_{1}} = -R \cdot i_{2} - 15 \Omega \cdot i_{4} + \cdots = 0 $$

Na fonte de $ 350 V $, o sentido escolhido faz a tensão aumentar (vai do do $-$ para o $+$). Portanto:

$$ V_{M_{1}} = -R \cdot i_{2} - 15 \Omega \cdot i_{4} + 350 V = 0 $$

</div>
<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>
</div>

