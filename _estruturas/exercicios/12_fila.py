---
layout: page
title: Implementação Fila
category: exercicio
subject: Listas Lineares
lesson: 4
---
Percorrer a matriz abaixo para identificar o maior número.

```
01, 20, 30, 01, 20, 02
05, 12, 17, 18, 65, 53
22, 10, 09, 45, 26, 12
34, 22, 10, 14, 18, 22
```

### Exemplo de solução

```python
matriz = [
    [1, 20, 30, 1, 20, 2],
    [5, 12, 17, 18, 65, 53],
    [22, 10, 9, 45, 26, 12],
    [34, 22, 10, 14, 18, 22]
]

max = 0
for linha in matriz:
    for val in linha:
        if val > max:
            max = val

print('Maior valor = ' + str(max))
```
