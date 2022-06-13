---
layout: page
title: Representação do Menu
category: exercicio
subject: Árvores
lesson: 16
---
Implemente uma busca em largura para a seguinte árvore:
![BFS](/estruturas/exercicios/37_bfs.png)

Observe que não se trata de uma árvore binário porque existem nós com mais de 2 filhos, então utilize as classes abaixo como base para realizar a implementação.


### Arvore.py
```python
class NoArvore:

    def __init__(self, pai):
        self.valor = None
        self.filhos = []
        self.pai = pai
        self.nivel = 0

        # quando um nó pai é passado, incrementa o nível
        if pai is not None:
            self.nivel = self.pai.nivel + 1
        
class Arvore:

    def __init___(self):
        self.raiz = None


    def carregar(self, json):
        valor = list(json.keys())[0]

        # cria o nós raiz
        self.raiz = NoArvore(None)
        self.raiz.valor = valor

        # adiciona os demais nós recursivamente
        self.adicionar_filhos(self.raiz, json[valor])


    def adicionar_filhos(self, no, json):

        if json is not None:
            chaves = list(json.keys())
            for chave in chaves:
                filho = NoArvore(no)
                filho.valor = chave
                no.filhos.append(filho)

                self.adicionar_filhos(filho, json[chave])
```

### Exercício 36 Template
```python
from biblioteca.fila import *
from biblioteca.arvore import Arvore

json = {
    "A": {
        "B": {
            "E": None,
            "F": None,
        },
        "C": {
            "G": {
                "J": None,
                "K": None,
            },
        },
        "D": {
            "H": None,
            "I": None
        },
    }
}

def bfs(raiz):
    print('implementar busca em largura')


arvore = Arvore()
arvore.carregar(json)

bfs(arvore.raiz)
```