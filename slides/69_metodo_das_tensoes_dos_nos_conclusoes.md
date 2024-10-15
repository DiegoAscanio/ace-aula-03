<style scoped>
    img {
      width: 100%;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
    .flex-container {
      display: flex;
      justify-content: space-between;
    }
    .flex-paragraph {
        flex: 2;
        margin-right: 10px;
        text-align: justify;
    }
    .flex-column {
        flex: 1;
        margin-right: 10px;
    }
    .flex-image {
        flex: 2;
    }
    li, p, table {
        font-size: 16pt;
    }
    table {
        margin-left: auto;
        margin-right: auto;
    }
    h3 {
        text-align: center;
    }
</style>

## Método das Tensões dos Nós - Conclusões

<div class="flex-container">
<div class="flex-column">

### Vantagens

- Reduz o número de equações a serem resolvidas;
- Facilita a visualização do comportamento da estrutura;
- Elimina a necessidade de se lidar com a LKT nas malhas.

</div>
<div class="flex-column">

### Desvantagens

- Sobrecarga cognitiva nas operações de montagem das equações, o que facilita a ocorrência de erros de desatenção por esquecimento de termos ou sinais;
    - Porque usando LKC nos nós, LKT nas malhas e Lei de Ohm, a montagem das equações é mais simples e direta;

</div>
</div>

### Exercício

Resolva o circuito anterior pelo método tradicional e aponte a quantidade de equações que o método das tensões dos nós eliminou.
