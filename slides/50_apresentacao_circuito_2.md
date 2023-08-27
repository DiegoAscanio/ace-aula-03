## Resolução do Circuito

<div class = "small">

Agora, devemos reescrever o sistema em sua representação matricial e usar um sistema computacional de álgebra linear numérica(numpy do python) para nos auxiliar a resolver esse circuito:

<!-- 
a & b & c & d & e & f & g & h  & i   & 1  & 2   & 3   & 4   & 5  \\
-->

$$
\begin{equation*}
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0  & 0   & -8 & 0   & 0   & 0   & 0  \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0  & 0   & -12& 0   & 0   & 0   & 0  \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0  & 0   & -4 & 0   & 0   & 0   & 0  \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0  & 0   & 0  & 0   & 0   & 0   & -6 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0  & 0   & 0  & 0   & 0   & 0   & -10\\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0  & 0   & 0  & 0   & 0   & 0   & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1  & 0   & 0  & -4  & 0   & 0   & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  & 1   & 0  & 0   & -24 & 0   & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  & 0   & 1  & 1   & 0   & 0   & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  & 0   & 0  & 1   & -1  & -1  & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  & 0   & -1 & 0   & -1  & 0   & 1  \\
0 & 0 & 0 & 0 & 0 & 0 & -1& 0  & 0   & 0  & -4  & 0   & 0   & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0  & 0   & 0  & 0   & -24 & 0   & -16\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  & 0   & -24& 4   & 24  & 0   & 0  \\
\end{bmatrix}
\begin{bmatrix}
V_a \\ V_b \\ V_c \\ V_d \\ V_e \\ V_f \\ V_g \\ V_h \\ V_i \\ i_1 \\ i_2 \\ i_3 \\ i_4 \\ i_5
\end{bmatrix}
=
\begin{bmatrix}
0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 48\\ 0 \\ 0 \\ -4 \\ 0 \\ 0 \\ -128 \\ 0 \\ 0
\end{bmatrix}
\end{equation*}
$$

</div>
