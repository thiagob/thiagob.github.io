---
layout: page
title: Produto e Pedido
category: exercicio
subject: Python
class_number: 2
---
Defina 2 classes: Produto e Pedido, conforme o diagrama abaixo.

A classe produto deverá ter um método para retornar o valor total do produto (quantidade * preço) e a classe Pedido deverá ter uma lista de produtos.

O Total do pedido deverá ser a soma dos totais dos produtos.



    ,--------------------.  
    |Produto             |  
    |--------------------|  
    |+int quantidade     |  
    |+decimal preco      |  
    |+string descricacao |      
    |total(): decimal    |  
    `--------------------'  
            |          
            |          
    ,-------------------.
    |Pedido             |
    |-------------------|
    |+Produto[] produtos|
    |total(): decimal   |
    `-------------------'

Diagrama gerado com: https://www.planttext.com/

### Exemplo de solução

```python
from turtle import pen


class Produto:

    quantidade = 0
    preco = 0
    descricao = ''

    def total(self):
        return self.preco * self.quantidade


class Pedido:

    produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def total(self):
        t = 0
        for p in self.produtos:
            t += p.total()
        return t


pedido = Pedido()

p1 = Produto()
p1.descricao = 'Café'
p1.quantidade = 1
p1.preco = 15.50

pedido.adicionar_produto(p1)

p2 = Produto()
p2.descricao = 'Açucar'
p2.quantidade = 3
p2.preco = 10.90

pedido.adicionar_produto(p2)


print(pedido.total()) # 48.2
```
