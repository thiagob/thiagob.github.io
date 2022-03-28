---
layout: page
title: Pilha de Quadros
category: exercicio
subject: Listas Lineares
lesson: 6
---

Em uma galeria de arte, os quadros disponíveis para venda ficam empilhados em duas pilhas: uma à direita e a outra à esquerda.

Quando os vendedores procuram um quadro, eles começam pela esquerda movendo o primeiro quadro da pilha da esquerda para a pilha da direita, até que encontrem o quadro que procuram.

Caso não o encontrem na pilha da esquerda, começam a procurá-lo na pilha da direita movendo 1 a 1 os quadros empilhados, sempre movendo o quadro no topo da pilha da direita para pilha da esquerda até que o encontrem.

Caso não encontrem o quadro na pilha da direita, os vendedoras avisam o cliente que não encontraram o quadro.

No início do dia as pilhas estão da seguinte forma:

| Pilha Esquerda            | Pilha Direita                  |
|---------------------------|--------------------------------|
| A Persistência da Memória | Noite Estrelada sobre o Ródano |
| Guernica                  | As Meninas                     |
| O beijo                   | O Nascimento de Vênus          |
| Noite Estrelada           | Meisje met de parel            |
| Mona Lisa                 |                                |

As tabelas representam as pilhas exatamente como estão fisicamente, ou seja, *A Persistência da Memória* e *Noite Estrelada sobre o Ródano* são os topos das pilhas.

Ao longo do dia os seguintes quadros foram procurados e vendidos:
1. Guernica
1. O Nascimento de Vênus
1. Noite Estrelada

Perto do final do dia os vendedores procuraram um quadro que não estava em nenhuma das pilhas.

## Perguntas
Ao final do dia, como ficaram as pilhas da direita e da esquerda?
Que quadro está no topo da pilha da esquerda?

### Template

```python
from biblioteca.pilha import Pilha

pilha_esq = Pilha()
pilha_dir = Pilha()


def procurar_esquerda(quadro):
    # Não encontrou
    return None

def procurar_direta(quadro):
    # Não encontrou
    return None

def vender(quadro):
    q = procurar_esquerda(quadro)
    # Não está na pilha da esquerda
    if q == None:
        q = procurar_direta(quadro)

    # Também não está na pilha da esquerda
    if q == None:
        print("Quadro não encontrado")
    
    return q

# Ao final do dia, como ficaram as pilhas da direita e da esquerda?
print(pilha_esq.itens)
print(pilha_dir.itens)

# Que quadro está no topo da pilha da esquerda?
print(pilha_esq.topo())
```