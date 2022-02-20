---
layout: page
title: Calculadora (Soma)
category: exercicio
subject: Python
class_number: 2
---
Defina 2 classes: Produto e Pedido, conforme o diagrama abaixo.

A classe produto deverá ter um método para retornar o valor total do produto (quantidade * preço) e a classe Pedido deverá ter uma lista de produtos.

O Total do pedido deverá ser a soma dos totais dos produtos.



    ,----------------.  
    |Produto         |  
    |----------------|  
    |+int quantidade |  
    |+decimal preco  |  
    |total(): decimal|  
    `----------------'  
            |          
            |          
    ,-------------------.
    |Pedido             |
    |-------------------|
    |+Produto[] produtos|
    |total(): decimal   |
    `-------------------'

Diagrama gerado com: https://www.planttext.com/