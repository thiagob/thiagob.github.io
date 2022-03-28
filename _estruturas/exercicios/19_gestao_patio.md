---
layout: page
title: Gestão de Pátio (containers)
category: exercicio
subject: Listas Lineares
lesson: 6
---
Uma empresa que trabalha com logística costuma os empilhar vazios em seu pátio para que possam ser utilizados depois. 

Por recomendação dos frabricantes, a pilha só pode conter no máximo 5 containers

Desta forma, quando a pilha atinge 5 containers, uma nova pilha é formada em frente a pilha de 5 containers. Vários pilhas de containers podem ser feitas umas em frentes as outras, de forma a otimizar o espaço utilizado no pátio.

Quando a empresa precisa de um container, ela retira o primeiro container (topo) da última pilha formada, uma vez que a empilhadeira não consegue acessar as pilhas de trás.

![pilha de containers](http://sindicomis.sindicatosdigitais.com.br/uploads/c81cef6c4993ddf71bf5740441a9b871ad11e32a.jpg)

# Problema
* Implemente um gerenciador para este pátio de forma que 25 containers sejam empilhados, e depois todos sejam desempilhados até que não existem mais containers no pátio.
* Ao empilhar os containers, atribua uma sequencia ao mesmos (1, 2, 3, .., 25) de forma que consiga identificar a sequência de desempilhamento.


### Template
```python
from biblioteca.pilha import Pilha

from biblioteca.pilha import Pilha

patio = Pilha()
p_cont = Pilha()

# empilha 25 containers
for i in range(25):
    pass


while not patio.vazia():
    pass
```