## Circuito com Fonte de Tensão e Fonte de Corrente

<div class="grid-50-50">

<div class="grid-element small">

### Passo 9

A partir das equações de corrente obtidas em 6, 7 e 8, se você seguiu o método corretamente, você produziu um modelo matemático adequado para o comportamento de circuito e ele pode ser resolvido através de sistemas lineares. IMPORTANTE: o número de equações obtidas deve ser igual ao número de incógnitas (valores desconhecidos) que representam os elementos do circuito.

#### Equações

Como $i_{0} = 4A$

<div class="grid-50-50">

<div class="grid-element">

$$
\begin{align}
&V_{a} - 8 i_{1} &= &0 \\
&V_{b} - 12 i_{1} &= &0 \\
&V_{c} - 4 i_{1} &= &0 \\
&V_{d} - 6 i_{5} &= &0 \\
&V_{e} - 10 i_{5} &= &0 \\
&V_{f} &= &48 \\
&V_{h} - 4 i_{2} &= &0
\end{align}
$$

</div>
<div class="grid-element">

$$
\begin{align}
&V_{i} - 24 i_{3} &= 0 \\
&i_{1} + i_{2} &= 4 \\
&i_{2} - i_{3} - i_{4} &= 0 \\
&i_{5} - i_{1} - i_{3} &= 0 \\
&-4 i_{2} - V_{g} &= -32 \\
& -24 i_{3} - 16 i_{5} + V_{g} &= 0 \\
& -24 i_{1} + 24 i_{3} + 4 i_{2} &= 0
\end{align}
$$

</div>
</div>

</div>

<div class="grid-element small" style="margin: auto;">

<!-- _class: transparent -->
![](./img/circuito_2_5.png)

14 variáveis desconhecidas: $[V_{a}, V_{b}, V_{c}, V_{d}, V_{e}, V_{f}, V_{g}, V_{h}, V_{i}, i_{1}, i_{2}, i_{3}, i_{4}, i_{5}]$ e 14 equações para estas variáveis, logo, é possível resolver este circuito através de um sistema linear.

</div>

</div>
