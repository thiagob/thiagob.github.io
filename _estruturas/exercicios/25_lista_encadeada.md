---
layout: page
title: Lista Encadeada (Parte I)
category: exercicio
subject: Listas Lineares
lesson: 9
---
Implementar uma classe de ```Nodo``` e outra classe de ```ListaEncadeada``` dentro de sua biblioteca em um arquivo ```encadeada.py```.

A Classe Nodo deve conter os seguintes atributos:
1. Valor: valor do Nodo
2. Proximo: referência para o próximo Nodo

A Classe ListaEncadeada deve conter:
1. Atributos
    1. Primeiro: referência para o primeiro Nodo
    1. Tamanho: que devem ser incrementado ou decremetnado de acordo com as adições e remoções
1. Métodos
    1. Adicionar: 
        * Caso a lista esteja vazia adiciona um novo nodo a lista como "Primeiro".
        * Caso a lista não esteja vazia adiciona o novo nodo após o último elemento

Adicionar os seguintes valores na lista encadeada, depois percorrer a lista imprimindo os valores com ```print()```:
```python
lista = ListaEncadeada()
lista.adicionar("Thiago")
lista.adicionar("João")
lista.adicionar("José")
```

### Template
```python
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:

    def __init__(self):
        self.primeiro = None
        self.atual = None
        self.tamanho = 0

    def adicionar(self, valor):
        return None
```