## Resolução do Circuito

<div class="grid-50-50">

<div class="grid-element small">

Todas as correntes do circuito em função do resistor $R$ dadas pelo sympy são:

$$

\displaystyle \left[\begin{array}{cccccccccccccc}1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{4225 R}{53 R + 474}\\0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{2295 R + 6750}{53 R + 474}\\0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{1530 R + 4500}{53 R + 474}\\0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{11250 - 400 R}{53 R + 474}\\0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{1750 R + 30000}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{1050 R + 18000}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{2400 R + 59250}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \frac{255 R + 4975}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \frac{255 R + 750}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & \frac{4225}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & \frac{2250 - 80 R}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & \frac{80 R + 1975}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & \frac{175 R + 3000}{53 R + 474}\end{array}\right]

$$

Sabemos que $i_{1} = {{255R + 750} \over {53R + 474}}$ (linha 8 da matriz). Sabemos também que $i_{1} = 3A$.

Resolvendo esta equação igual à $3A$ no sympy, obtemos $R = 7 \Omega$.

</div>

<div class="grid-element regular">

Substituindo $R$ por $7 \Omega$ em todas as outras equações dos elementos obtemos:

<div class="grid-50-50 small">

<div class="grid-element">
$$
\begin{align}
    V_a = 35\\
    V_b = 27\\
    V_c = 18\\
    V_d = 10\\
    V_e = 50\\
    V_f = 30\\
    V_g = 90
\end{align}
$$
</div>

<div class="grid-element">
$$
\begin{align}
    i_0 = 8\\
    i_1 = 3\\
    i_2 = 5\\
    i_3 = 2\\
    i_4 = 3\\
    i_5 = 5\\
\end{align}
$$
</div>

</div>

Portanto, agora o circuito está resolvido, pois, é possível calcular todas as grandezas elétricas associadas a seus elementos.

</div>

</div>
