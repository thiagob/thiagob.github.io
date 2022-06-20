---
layout: page
title: Custo de Produção
category: exercicio
subject: Árvores
lesson: 17
---
Com base na árvore de custo apresentada em aula e também no template apresentado abaixo, implementar o método ```calcular_porcentagem``` para determinar a porcentagem que custo do nó corresponde em comparação com o nó ascendente/pai.

Por exemplo: se o custo do nó pai é 3 e este nó possui 3 filhos cada um com 1 de custo, cada filho corresponderá a 33% do custo do nó pai.

**Importante:** considerar o percentual sempre com relação ao custo do pai e não do custo total.

Ao final, implementar o método ```imprimir_custos``` para fazer a impressão dos valores.

Árvore de custo:
![BFS](/estruturas/exercicios/38_custo_hamburguer.jpg)

Observe que não se trata de uma árvore binário porque existem nós com mais de 2 filhos, então utilize as classes abaixo como base para realizar a implementação.


### arvore_custo.py
```python
class NoArvoreCusto:

    def __init__(self, pai):
        self.nome = None
        self.custo = None
        self.porcentagem = 0
        self.filhos = []
        self.pai = pai
        self.nivel = 0

        # quando um nó pai é passado, incrementa o nível
        if pai is not None:
            self.nivel = self.pai.nivel + 1
        
class ArvoreCusto:

    def __init___(self):
        self.raiz = None


    def carregar(self, json):
        nome = list(json.keys())[0]

        # cria o nós raiz
        self.raiz = NoArvoreCusto(None)
        self.raiz.nome = nome
        self.raiz.valor = None

        # adiciona os demais nós recursivamente
        self.adicionar_filhos(self.raiz, json[nome])


    def adicionar_filhos(self, no, json):

        if json is not None:
            chaves = list(json.keys())
            for chave in chaves:
                filho = NoArvoreCusto(no)
                no.filhos.append(filho)
                
                filho.nome = chave
                filho.valor = None

                filhos = json[chave]

                # nó não folha (contém filhos)
                if type(filhos) is dict:
                    self.adicionar_filhos(filho, json[chave])
                else:
                    filho.valor = json[chave]
```

### Template Exercício
```python
from biblioteca.arvore_custo import *

json = {
    "Hambúrguer": {
        "Ingredientes": {
            "Carne": 4.50,
            "Queijo": 2.50,
            "Saladas": 1.50,
            "Molho BBQ": {
                "Catchup": 1,
                "Açucar": 0.25,
                "Molho shoyu": 0.75,
                "Azeite": 0.25
            }
        },
        "Mão de Obra": {
            "Grelhar": 1.0,
            "Montagem": 2,
            "Servir": 1
        },
        "Entrega": {
            "Embalagem": 1.25,
            "Motorista": 7
        }
    }
}

def calcular_custos(no):
    if len(no.filhos) == 0:
        return no.valor

    custo = 0
    for filho in no.filhos:
        custo += calcular_custos(filho)
    
    no.valor = custo
    return custo

def calcular_porcentagem(no):
    print('IMPLEMENTAR ESTE MÉTODO')


def imprimir_custos(no):
    print('IMPLEMENTAR ESTE MÉTODO')

arv_custos = ArvoreCusto()
arv_custos.carregar(json)

calcular_custos(arv_custos.raiz)
calcular_porcentagem(arv_custos.raiz)

imprimir_custos(arv_custos.raiz)
```

### Exemplo impressão
```python
Hambúrguer 23.0 | ?%
..Ingredientes 10.75 | ?%
....Carne 4.5 | ?%
....Queijo 2.5 | ?%
....Saladas 1.5 | ?%
....Molho BBQ 2.25 | ?%
......Catchup 1 | ?%
......Açucar 0.25 | ?%
......Molho shoyu 0.75 | ?%
......Azeite 0.25 | ?%
..Mão de Obra 4.0 | ?%
....Grelhar 1.0 | ?%
....Montagem 2 | ?%
....Servir 1 | ?%
..Entrega 8.25 | ?%
....Embalagem 1.25 | ?%
....Motorista 7 | ?%
```