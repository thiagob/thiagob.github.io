---
layout: page
title: Adicionar espaços
category: exercicio
subject: Python
class_number: 1
---
Definir um método que receba uma string como parâmetro e retorne outra string, adicionando espaços entre cada caracter.

    entrada = "thiago bohn"
    saida = "t h i a g o   b o h n"

### Exemplo de solução

```python
def adiciona_espacos(texto):
    saida = ''

    for letra in texto:
        saida = saida + letra + ' '

    return saida

def adiciona_espacos_alt(texto):
    saida = ''
    tamanho = len(texto)

    for idx in range(tamanho):
        saida = saida + texto[idx] + ' '

    return saida    


print(adiciona_espacos('Thiago Bohn')) # T h i a g o   B o h n
print(adiciona_espacos_alt('Thiago Bohn')) # T h i a g o   B o h n
```
