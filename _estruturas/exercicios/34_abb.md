---
layout: page
title: Árvore Binária de Busca
category: exercicio
subject: Árvores
lesson: 15
---

Utilizando a biblioteca de árvore disponibilizada no exercício anterior implementar o método a busca em uma árvore binária de busca no método abaixo:

```python
def buscar_abb(valor, no):
    # implementar este metodo
```
A seguinte árvore...

![Árvore](/estruturas/exercicios/34_abb.jpg)

Pode ser instanciada utilizando o seguinte código:

```python
print("----- Árvore Binária de Busca ------")
abb = ArvoreBinariaBusca()
abb.adicionar(8)
abb.adicionar(3)
abb.adicionar(10)
abb.adicionar(1)
abb.adicionar(6)
abb.adicionar(14)
abb.adicionar(4)
abb.adicionar(7)
abb.adicionar(13)
imprimir_em_order(abb.raiz)

no = buscar_abb(14, abb.raiz)
print(no.valor)
```

Lembre-se de implementar uma busca por um método que não existe na árovre.