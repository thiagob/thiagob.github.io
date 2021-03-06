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

    # construtor
    def __init__(self):
        self.valor = None
        self.proximo = None
        # Ao invés de criar um método para identificar o último
        # também é possível de criar uma variável para controlar
        # self.utlimo = None

class ListaEncadeada:

    # construtor
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    # A implementação feita em sala de adiciona o nodo após o 
    # último, mas também é possível de fazer uma implementação
    # adicionando o elemento no início
    def adicionar(self, nodo):
        # lista vazia
        if self.vazia():
            # adicionar como primeiro
            ...
        else:
            # adiciona depois do último
            ...

        self.tamanho = self.tamanho + 1

    def vazia(self):
        # se não tem primeiro a lista está vazia
        return ...

    # retorna quem é o último
    def ultimo(self):
        if self.vazia():
           return False
        else:
            # percorre até o nodo que não tem próximo (vulgo último)
        
    def remover(self):
        # por enquanto só diminui a quantidade
        self.tamanho = self.tamanho - 1
```