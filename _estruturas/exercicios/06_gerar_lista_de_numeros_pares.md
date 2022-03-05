---
layout: page
title: Gerar lista de números pares
category: exercicio
subject: Python
class_number: 2
---
Escrever um método ou rotina que gere uma lista contendo sem 100 números aleatórios, depois remover da lista todos os números ímpares.

### Exemplos de solução
```python
import random

lista = []

# adiciona 100 números
while len(lista) < 100:
    lista.append(random.randint(0,1000))
print(len(lista))

# percorre a lista e movendo somente os pares
pares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)        
print(len(pares))


# outra forma de filtrar
pares = [num for num in lista if num % 2 == 0]
print(len(pares))
```
