## Resolução do Circuito

Agora, devemos reescrever o sistema em sua representação matricial e usar um sistema computacional de álgebra linear simbólica (sympy do python) para nos auxiliar a resolver esse circuito e encontrar as correntes em função do resistor $R$ desconhecido:

$$
\begin{bmatrix}
    1 & -1 & -1 & 0 & 0 & 0 \\
    0 & 0 & 1 & -1 & -1 & 0 \\
    0 & -1 & 0 & -1 & 0 & 1 \\
    0 & 0 & -R & 0 & -30 & 0 \\
    0 & -15 & R & 5 & 0 & 0 \\
    0 & 0 & 0 & -5 & 30 & -16 \\
\end{bmatrix}
\begin{bmatrix}
    i_{0} \\
    i_{1} \\
    i_{2} \\
    i_{3} \\
    i_{4} \\
    i_{5} \\
\end{bmatrix}
=
\begin{bmatrix}
    0 \\
    0 \\
    0 \\
    -125 \\
    0 \\
    0 \\
\end{bmatrix}
$$
