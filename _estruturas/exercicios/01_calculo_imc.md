---
layout: page
title: Cálculo IMC
category: exercicio
subject: Python
lesson: 1
---
Criar um método que receba massa e altura como parâmetros e calcule o índice de massa corporal.

## Definição

O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. Desenvolvido pelo polímata Lambert Quételet no fim do século XIX, trata-se de um método fácil e rápido para a avaliação do nível de gordura de cada pessoa, sendo, por isso, um preditor internacional de obesidade adotado pela Organização Mundial da Saúde (OMS).

Fonte: [Wikipedia](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal)

## Como calcular

![formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/4db320ff2cde68cebea226fb921247d7ebbfad33)


### Exemplo de solução

```python
def imc(massa, altura):
    return massa / (altura * altura)

print('IMC: %.1f' % imc(93, 2)) # IMC: 23.2
```
