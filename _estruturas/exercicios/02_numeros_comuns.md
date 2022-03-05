---
layout: page
title: Números comuns a 2 arrays
category: exercicio
subject: Python
class_number: 1
---
Criar um novo array com os números que são comuns a 2 arrays, por exemplo:

    a1 = [3, 7, 22, 43, 65, 32]
    a2 = [3, 4, 9, 22, 35, 43, 53, 65, 33]
    
    
### Exemplo de solução

```python
def numeros_em_comum(a1, a2):
    nums = []

    for n in a1:
        if n in a2:
            nums.append(n)

    return nums


def numeros_em_comum_alt(a1, a2):
    i = 0
    j = 0
    nums = []

    while(i < len(a1) and j < len(a2)):
        if a1[i] == a2[j]:
            nums.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1

    return nums
    



a1 = [3, 7, 22, 43, 65, 32]
a2 = [3, 4, 9, 22, 35, 43, 53, 65, 33]


print(numeros_em_comum(a1, a2)) # [3, 22, 43, 65]
print(numeros_em_comum(a1, [])) # []

print(numeros_em_comum_alt(a1, a2)) # [3, 22, 43, 65]
print(numeros_em_comum_alt(a1, [])) # []
```
