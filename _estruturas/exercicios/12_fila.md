---
layout: page
title: Implementação Fila
category: exercicio
subject: Listas Lineares
lesson: 4
---
Fazer a implementação de uma classe para gerenciar uma fila, fazendo uso dos recursos disponíveis no array Python.


A classe deverá se chamar Fila e deverá conter os seguintes métodos:

1. *enfileirar(elemento)*: o elemento passado por parâmetro deverá ser adicionado na final da fila
1. *desenfileirar()*: deverá retorno o primeiro elemento da fila, removendo-o da fila
1. *primeiro():* deverá retornar o primeiro elemento da fila sem removê-lo da fila
1. *tamanho()*: deverá retornar a quantidade de elementos presentes na fila
1. *vazia()*: deverá True quando não houverem elementos na fila

*Importante:* implementar essa classe em um arquivo fila.py para poder ser reutilizado como parte da biblioteca de estruturas de dados avançadas.

<a href="https://docs.python.org/pt-br/3/tutorial/datastructures.html">Documentação Python sobre Estruturas de Dados</a>


### Template

```python
class Fila:

    def __init__(self):
        self.itens = []

    def enfileirar(self, elemento):
        pass

    def desenfileirar(self):
        return None

    def primeiro(self):
        return None

    def tamanho(self):
        return None

    def vazia(self):
        pass

```
