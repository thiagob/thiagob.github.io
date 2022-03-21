---
layout: page
title: Fila Prioritária
category: exercicio
subject: Listas Lineares
lesson: 5
---
Para melhorar seu atendimento aos clientes, um banco definiu que os clientes deveriam ser organizados em duas filas. Uma para clientes prioritários e outra de clientes não prioritários.
Também definiu-se que antes de atender um cliente não prioritário, 2 clientes prioritários deveriam ser chamados.

## Exemplo

**Fila priotária**

1. Maria
1. João

**Fila não prioritária**

1. José
1. Ana

Considerando as filas à cima, a ordem de atendimento seria: **Maria, João, José e Ana.**

## Problema

Implemente o controle destas filas utilizando sua classe de fila e responda: **quem foi atendido depois de Rosa?**

**Fila priotária**

1. Olavo
1. Afonso
1. Alcino
1. Aparecida
1. Rosa
1. Maria

**Fila não prioritária**

1. Antônio
1. Carlos
1. Francisco
1. Geraldo
1. João
1. José
1. Joaquim
1. Jorge'


## Ponto de Partida Opcional
```python
from biblioteca.fila import Fila

fila_prio = Fila()
fila_n_prio = Fila()

fila_prio.enfileirar('Maria')
fila_prio.enfileirar('João')
print(fila_prio.items)

fila_n_prio.enfileirar('José')
fila_n_prio.enfileirar('Ana')
print(fila_n_prio.items)

print('*** SEQUENCIA DE ATENDIMENTO ***')

# como posso fazer isto sem ter que copiar e colar o código?
# como identificar quem foi atendido depois de Rosa
# "if depois de Rosa?"
for i in range(2):
    print(fila_prio.desenfileirar())

print(fila_n_prio.desenfileirar())

for i in range(2):
    if not fila_prio.vazia():
        print(fila_prio.desenfileirar())

print(fila_n_prio.desenfileirar())
```
