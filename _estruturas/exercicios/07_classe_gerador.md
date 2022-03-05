---
layout: page
title: Classe Gerador
category: exercicio
subject: Python
class_number: 2
---
Construa uma classe Gerador que possua 2 métodos. 

1. Um método que retorne uma lista (array) de inteiroes. O tamanho da lista deverá ser passado por parâmetro.
2. Um método que retorne uma uma string aleatório do tamanho (número de caracteres) passado por parâmetro.

Colocar essa classe em um arquivo .py e fazer uma chamada para esta classe de outro arquivo utilizando o import.

### Exemplos de solução

```python
import random
import string

class Gerador:

    def gerar_array_int(self, tamanho):
        arr = []
        while len(arr) < tamanho:
            arr.append(random.randint(0,100000000))
        
        return arr
    
    def gerar_string(self, tamanho):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(tamanho))
```
