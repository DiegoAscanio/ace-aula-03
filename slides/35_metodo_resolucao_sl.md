## Resolução do Circuito

<div class="grid-50-50">

<div class="grid-element regular">

Todas as correntes do circuito em função do resistor $R$ dadas pelo sympy são:

$$

\left[\begin{matrix}1 & 0 & 0 & 0 & 0 & 0 & \frac{255 R + 4975}{53 R + 474}\\0 & 1 & 0 & 0 & 0 & 0 & \frac{255 R + 750}{53 R + 474}\\0 & 0 & 1 & 0 & 0 & 0 & \frac{4225}{53 R + 474}\\0 & 0 & 0 & 1 & 0 & 0 & \frac{2250 - 80 R}{53 R + 474}\\0 & 0 & 0 & 0 & 1 & 0 & \frac{80 R + 1975}{53 R + 474}\\0 & 0 & 0 & 0 & 0 & 1 & \frac{175 R + 3000}{53 R + 474}\end{matrix}\right]

$$

Sabemos que $i_{1} = {{255R + 750} \over {53R + 474}}$, sabemos também que $i_{1} = 3A$.

Resolvendo esta equação igual à $3A$ no sympy, obtemos $R = 7 \Omega$.

</div>

<div class="grid-element regular">

Substituindo $R$ por $7 \Omega$ em todas as outras equações de corrente obtemos:

$$
\begin{align}
    i_{0} = 8A \\
    i_{1} = 3A \\
    i_{2} = 5A \\
    i_{3} = 2A \\
    i_{4} = 3A \\
    i_{5} = 5A \\
\end{align}
$$

Portanto, agora o circuito está resolvido, pois, é possível calcular todas as grandezas elétricas associadas a seus elementos.

</div>

</div>
