---
layout: page
title: Fila Encadeada
category: exercicio
subject: Listas Lineares
lesson: 11
---

Utilizando a implementação de fila encadeada do professor, refazer (ctrl + c e ctrl +v trocando a classe) algum dos exercícios anteriores que utilizou fila na solução e comparar se os resultados obtidos são os mesmos.

```python
class Nodo:

    # construtor
    def __init__(self):
        self.valor = None
        self.proximo = None

class FilaEncadeada:

    # construtor
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def enfileirar(self, nodo):
        # fila ainda está vazia
        if self.primeiro == None:
            self.primeiro = nodo
        else:
            # adiciona depois do último
            self.ultimo.proximo = nodo

        # "memoriza" último
        self.ultimo = nodo
        self.tamanho = self.tamanho + 1

    def vazia(self):
        # se não tem primeiro a lista está vazia
        if self.primeiro == None:
            return True
        else:
            return False

    def desenfileirar(self):
        if self.vazia():
            return None
        else:
            # FIFO (remove o primeiro)
            nodo = self.primeiro
            self.primeiro = nodo.proximo

            # diminui a quantidade
            self.tamanho = self.tamanho - 1

            return nodo


if __name__ == "__main__":

    # Cria fila de camisetas (exerc. 17)
    fila = FilaEncadeada()

    # Passo 1 : Criar Nodo
    n1 = Nodo()
    n1.valor = 'Azul'
    fila.enfileirar(n1)

    # Emfila demais cores
    cores = ['Vermelha', 'Branca', 'Verde', 'Preta']
    for cor in cores:
        n = Nodo()
        n.valor = cor

        fila.enfileirar(n)

    print(fila.tamanho)

    # Imprime a fila
    while not fila.vazia():
        camiseta = fila.desenfileirar()
        print(camiseta.valor)

    print(fila.tamanho)
```