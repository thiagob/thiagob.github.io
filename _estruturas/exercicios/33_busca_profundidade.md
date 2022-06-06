---
layout: page
title: Busca em profundidade
category: exercicio
subject: Árvores
lesson: 15
---

Utlizando as classes disponibilizadas abaixo implemente os 3 algoritmos de busca em profunidade:

```python
#arvore_binaria.py
class NoArvoreBinaria:

    def __init__(self, pai):
        self.valor = None
        self.esquerda = None
        self.direita = None
        self.pai = pai
        self.nivel = 0

        # quando um nó pai é passado, incrementa o nível
        if pai is not None:
            self.nivel = self.pai.nivel + 1
        
class ArvoreBinaria:

    def __init___(self):
        self.raiz = None


    def carregar(self, json):
        valor = list(json.keys())[0]

        # cria o nós raiz
        self.raiz = NoArvoreBinaria(None)
        self.raiz.valor = valor

        # adiciona os demais nós recursivamente
        self.adicionar_filhos(self.raiz, json[valor])


    def adicionar_filhos(self, no, json):

        if json is not None:
            chaves = list(json.keys())
            esquerda = chaves[0]
            direita = chaves[1] if len(chaves) >= 2 else None

            # considera o primeiro item do array à esquerda
            # caso a descriação seja "" considera que não há informação
            if esquerda and esquerda != "":
                no.esquerda = NoArvoreBinaria(no)
                no.esquerda.valor = esquerda

                self.adicionar_filhos(no.esquerda, json[esquerda])

            # considera o primeiro item do array à esquerda
            # caso a descriação seja "" considera que não há informação
            if direita and direita != "":
                no.direita = NoArvoreBinaria(no)
                no.direita.valor = direita

                self.adicionar_filhos(no.direita, json[direita])

class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if self.raiz == None:
            self.raiz = NoArvoreBinaria(None)
            self.raiz.valor = valor
        else:
            self.adicionar_abaixo_de(self.raiz, valor)

    def adicionar_abaixo_de(self, no, valor):
        if valor == no.valor:
            return no
        elif valor > no.valor:
            if no.direita is None:
                no.direita = NoArvoreBinaria(no)
                no.direita.valor = valor
            else:
                self.adicionar_abaixo_de(no.direita, valor)
        elif valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoArvoreBinaria(no)
                no.esquerda.valor = valor
            else:
                self.adicionar_abaixo_de(no.esquerda, valor)
    
def imprimir_em_order(no):
    # implemente este método

def imprimir_pre_order(no):
    # implemente este método

def imprimir_pos_order(no):
    # implemente este método
```

Para deslocar os nós para direita de acordo com o nível você pode multiplicar espaços pelo nível da seguinte forma:
```python
print("   " * no.nivel + str(no.valor))
```

Aqui está um exemplo de chamada destas classes:
```python
from biblioteca.arvore_binaria import *

json = {
    "F": {
        "B": {
            "A": None,
            "D": {
                "C": None,
                "E": None
            }
        },
        "G": {
            "": None,
            "I": {
                "H": None,
                "": None
            }
        }
    }
}

arv_bn = ArvoreBinaria()
arv_bn.carregar(json)

print(arv_bn.raiz.valor)

print("----- Em Order ------")
imprimir_em_order(arv_bn.raiz)

print("----- Pré Order ------")
imprimir_pre_order(arv_bn.raiz)

print("----- Pós Order ------")
imprimir_pos_order(arv_bn.raiz)
```