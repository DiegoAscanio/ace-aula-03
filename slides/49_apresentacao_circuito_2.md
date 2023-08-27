## Circuito com Fonte de Tensão e Fonte de Corrente

### Passo 9

<div class="regular">

Reorganizando as equações do circuito para construir um sistema linear terminamos o algoritmo de modelagem nos seguintes termos:


$$
\begin{cases}
    &1 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} - 8 i_{1} + 0 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\
    &0 V_{a} + 1 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} -12 i_{1} + 0 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 1 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} - 4 i_{1} + 0 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 1 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} + 0 i_{1} + 0 i_{2} + 0 i_{3} + 0 i_{4} - 6 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 1 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} + 0 i_{1} + 0 i_{2} + 0 i_{3} + 0 i_{4} - 10 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 1 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} + 0 i_{1} + 0 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= 48\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 1 V_{h} + 0 V_{i} + 0 i_{1} - 4 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 1 V_{i} + 0 i_{1} + 0 i_{2} -24 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} + 1 i_{1} + 1 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= -4\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} + 0 i_{1} + 1 i_{2} - 1 i_{3} - 1 i_{4} + 0 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} - 1 i_{1} + 0 i_{2} - 1 i_{3} + 0 i_{4} + 1 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} - 1 V_{g} + 0 V_{h} + 0 V_{i} + 0 i_{1} - 4 i_{2} + 0 i_{3} + 0 i_{4} + 0 i_{5} &= -128\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 1 V_{g} + 0 V_{h} + 0 V_{i} + 0 i_{1} + 0 i_{2} - 24 i_{3} + 0 i_{4} - 16 i_{5} &= 0\\
    &0 V_{a} + 0 V_{b} + 0 V_{c} + 0 V_{d} + 0 V_{e} + 0 V_{f} + 0 V_{g} + 0 V_{h} + 0 V_{i} - 24 i_{1} + 4 i_{2} + 24 i_{3} + 0 i_{4} + 0 i_{5} &= 0\\
\end{cases}
$$

</div>
