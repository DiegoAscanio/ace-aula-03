<style scoped>
    table {
        font-size: 16px;
        margin-left: auto;
        margin-right: auto;
    }
    p, li {
        text-align: justify;
        font-size: 16px;
    }
    figcaption {
        font-size: 12px;
        text-align: center;
    }
    h2 {
        text-align: center;
        font-size: 28px;
    }
    h3 {
        text-align: center;
        font-size: 16px;
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

## Método das Correntes das Malhas - Passo 3

<div class="flex-container">
<div class="flex-column">

### Malha \\(M_2\\)

Percorrendo a malha 2 no sentido horário após o nó inferior de \\(R = 1 \Omega\\), temos:

\\[
\begin{align\*}
&  & -i\_2 - 4 i\_2 + 4 i\_3 + 5 i\_1 - 5 i\_2 = 0 \therefore \\\\
&  & -10 i\_2 + 5 i\_1 + 4 i\_3 = 0 \therefore \\\\
&  & 10 i\_2 - 5 i\_1 - 4 i\_3 = 0 \therefore \\\\
&  & 5 i\_1 - 10 i\_2 + 4 i\_3 = 0 \quad (2)
\end{align\*}
\\]

### Malha \\(M_3\\)

Percorrendo a malha 3 no sentido horário após o nó anterior a \\(R = 4 \Omega\\), temos:

\\[
\begin{align\*}
4 i\_2 - 4 i\_3 - 15 i\_1 + 15 i\_3 + 20 i\_1 - 20 i\_3 = 0 \therefore \\\\
5 i\_1 + 4 i\_2 - 9 i\_3 = 0 \quad (3)
\end{align\*}
\\]


</div>
<div class="flex-column">

<!-- _class: transparent -->

![](img/circuit-step-2.png)

</div>
</div>
