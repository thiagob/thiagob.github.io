---
layout: page
title: Roda de Chimarrão
category: exercicio
subject: Listas Lineares
lesson: 12
---

Implementar uma roda de chimarrão de 6 pessoas que seja controlada por uma lista circular encadeada.

### Template

```python
class Nodo:

    # construtor
    def __init__(self):
        self.valor = None
        self.proximo = None

class ListaCircularEncadeada:

    # construtor
    def __init__(self):
        self.primeiro = None
        self.ultimo_retornado = None

    def adicionar(self, nodo):
        # aponta o novo nodo para o primeiro
        nodo.proximo = self.primeiro
        # coloca o novo nodo como primeiro, movendo o primeiro para segundo
        self.primeiro = nodo

    def vazia(self):
        # se não tem primeiro a lista está vazia
        if self.primeiro == None:
            return True
        else:
            return False

    def proximo(self):
        # quando nunca retornou ninguém, retorna o primeiro
            # nas passadas subsequentes, retorna quem vem depois do ultimo retornado
            # se não existe próximo, retorna o primeiro
       
        # Substituir pelo código de verdade
        return None


            
if __name__ == "__main__":

    # Cria lista circular
    circ = ListaCircularEncadeada()

    
```