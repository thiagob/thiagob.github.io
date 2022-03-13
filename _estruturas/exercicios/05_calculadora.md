---
layout: page
title: Calculadora (Soma)
category: exercicio
subject: Python
lesson: 1
---
Criar um programa que solicite¹ dois números e imprima a soma dos dois números.
Além de somar, o programa também deverá consistir se o valor informado pelo usuário é um número válido.

    
¹ n = input()

### Exemplos de solução

```python
import string


while True:
    num1 = ''
    num2 = ''

    while not num1.isnumeric():
        num1 = input('Digite o primeiro número: ')

    while not num2.isnumeric():
        num2 = input('Digite o segundo número: ')

    soma = int(num1) + int(num2)

    print('>>> ' + num1 + ' + ' + num2 + ' = ' + str(soma))
```
