---
layout: page
title: Implementação Pilha
category: exercicio
subject: Listas Lineares
lesson: 6
---
Fazer a implementação de uma classe para gerenciar uma pilha, fazendo uso dos recursos disponíveis no array Python.


A classe deverá se chamar Pilha e deverá conter os seguintes métodos:

1. *empilhar*: o elemento passado por parâmetro deverá ser adicionado no topo da pilha
1. *desempilhar()*: deverá retornar o elementoque está no topo da pilha e depois removê-lo da pilha
1. *topo():* deverá retornar o  elemento que está no topo da pilha (sem removê-lo da pilha)
1. *tamanho()*: deverá retornar a quantidade de elementos presentes na pilha
1. *vazia()*: deverá True quando não houverem elementos na pilha

*Importante:* implementar essa classe em um arquivo pilha.py para poder ser reutilizado como parte da biblioteca de estruturas de dados avançadas.

<a href="https://docs.python.org/pt-br/3/tutorial/datastructures.html">Documentação Python sobre Estruturas de Dados</a>

### Template

```python
class Pilha:

    def __init__(self):
        self.itens = []

    def empilhar(self, elemento):
        pass

    def desempilhar(self):
        pass

    def topo(self):
        pass

    def tamanho(self):
        pass

    def vazia(self):
        pass
```