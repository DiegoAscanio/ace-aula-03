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

3. Para cada malha do circuito escreva LKT considerando em cada malha:
    - As quedas (ou elevações) de tensão causadas pelo trânsito das correntes nos resistores;
    - As quedas (ou elevações) de tensão causadas pelas fontes de tensão;
    - As quedas (ou elevações) de tensão causadas pelas fontes de corrente;

### Malha \\(M_1\\)

Percorrendo a malha 1 no sentido horário após o nó superior da fonte de \\(50 \text{V}\\), temos:

\\[
\begin{align\*}
&  & -5 i\_1 + 5 i\_2 - 20 i\_1 + 20 i\_3 + 50 &= 0 \therefore \\\\
&  & -25 i\_1 + 5 i\_2 + 20 i\_3 &= -50 \therefore \\\\
&  & 25 i\_1 - 5 i\_2 - 20 i\_3 &= 50 \quad (1)
\end{align\*}
\\]

</div>
<div class="flex-column">

<!-- _class: transparent -->

![](img/circuit-step-2.png)

</div>
</div>
