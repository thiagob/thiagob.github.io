---
layout: page
title: Pilha de Camiseta
category: exercicio
subject: Listas Lineares
lesson: 6
---

João está em uma viagem de negócios de 6 dias de duração. Ao chegar no hotel, desfez sua mala. Sua pilha de camisetas ficou da seguinte forma (considere que a camiseta Preta é a camiseta que está no topo da pilha):

| Pilha |
|-------|
| Preta |
| Verde |
| Branca |
| Vermelha |
| Azul |

Ao longo dos dias, João sempre pegava a primeira camiseta (topo) quando precisava se trocar. Alguns dias utilizava 1 camiseta, outros dias mais conforme abaixo:

### Dia 1
João utilizou 1 Camiseta

### Dia 2
João utilizou 2 Camisetas

### Dia 3
João utilizou 2 Camisetas e após utilizá-las, percebendo que precisaria de mais camisetas do que trouxe, comprou mais 3 camisetas e as adicionou na pilha na seguinte sequência:

1. Branca
1. Verde
1. Azul

### Dia 4
João utilizou 1 Camiseta

### Dia 5
João utilizou 1 Camiseta

### Dia 6
João utilizou 1 Camiseta

## Perguntas
Ao final do dia 6, quantas camisetas limpas sobraram?
Qual foi a última cor de camiseta que João utilizou?


### Template

```python
from biblioteca.pilha import Pilha

pilha = Pilha()


# Dia 1

# Dia 2

# Dia 3

# Dia 4 

# Dia 5

# Dia 6
ultima = pilha.desempilhar()
print('Quantas camiseta sobraram: ' + str(pilha.tamanho()))
print('A última camiseta que João utilizou foi: ' + str(ultima))
```