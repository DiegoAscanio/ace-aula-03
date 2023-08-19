
## Algoritmo

### Passo 5

<div class="grid-50-50">

<div class="grid-element small">

3. **(ESSENCIAL)** Avalie os sinais da diferença de potencial do elemento no sentido escolhido para percorrer a malha. <!-- Em \( R \) no sentido horário a tensão vai do sentido positivo ao negativo, portanto, diminuindo. se fosse no sentido anti horário, a tensão no elemento iria do negativo para o positivo, portanto, aumentando -->
    1. Se no sentido escolhido a tensão diminuir — for do \\(+\\) para o \\(-\\) — então coloque a tensão deste elemento como negativa na equação da malha avaliada.
    2. Se no sentido escolhido a tensão aumentar — for do \\(-\\) para o \\(+\\) — então coloque a tensão deste elemento como positiva na equação da malha avaliada.
- No nosso elemento atual \\( R \\) no sentido horário a tensão diminui. Portanto adicionamos a tensão negativa deste elemento na equação da malha \\( M_{1} \\). Assim:

\\[ V_{M_{1}} = -R \cdot i_{2} + \cdots = 0 \\]

</div>

<div class="grid-element">

<!-- _class: transparent -->
![grid-img](./img/circuito_final.png)

</div>

</div>

