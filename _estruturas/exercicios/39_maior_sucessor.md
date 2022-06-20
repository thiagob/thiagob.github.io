---
layout: page
title: Operação em ABB (Maior e Sucessor)
category: exercicio
subject: Árvores
lesson: 17
---
Implementar os métodos 
sucessor e maior

Implemente uma busca em largura para a seguinte árvore:
![BFS](/estruturas/exercicios/39_maior_sucessor.JPG)

Observe que não se trata de uma árvore binário porque existem nós com mais de 2 filhos, então utilize as classes abaixo como base para realizar a implementação.



### Template
```python
from biblioteca.arvore_binaria import *

json = {
    "8": {
        "3": {
            "1": {
                "0": None,
                "2": None,
            },
            "6": {
                "4": None,
                "7": None,
            },
        },
        "14": {
            "10": {
                "9": None,
                "13": None,
            },
            "19": {
                "17": None,
                "20": None,
            },
        }
    }
}

def menor_no(no):
    while no and no.esquerda:
        no = no.esquerda
    return no

def maior_no(no):
    print('IMPLEMENTAR ESTE MÉTODO')

def antecessor(valor, abb):
    no = buscar_abb(valor, abb.raiz)

    if no:
        if no.esquerda:
            return maior_no(no.esquerda)
        elif no.pai:
            if no.pai.direita == no:
                return no.pai
            else:
                no = no.pai
                while no.pai:
                    if no.pai.direita == no:
                        return no.pai
                    no = no.pai

    return None

def sucessor(valor, abb):
    print('IMPLEMENTAR ESTE MÉTODO')

abb = ArvoreBinariaBusca()
abb.adicionar(8)

abb.adicionar(3)
abb.adicionar(14)

abb.adicionar(1)
abb.adicionar(6)
abb.adicionar(10)
abb.adicionar(19)


abb.adicionar(0)
abb.adicionar(2)
abb.adicionar(4)
abb.adicionar(7)

abb.adicionar(9)
abb.adicionar(13)
abb.adicionar(17)
abb.adicionar(20)



#abb.carregar(json)
print(menor_no(abb.raiz).valor)
print(maior_no(abb.raiz).valor)

print(antecessor(8, abb).valor)
print(antecessor(7, abb).valor)
print(antecessor(9, abb).valor)
print(antecessor(0, abb))

print(sucessor(8, abb).valor)
print(sucessor(9, abb).valor)
print(sucessor(7, abb).valor)
print(sucessor(20, abb))
```