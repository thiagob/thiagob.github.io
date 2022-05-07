---
layout: page
title: Pilha Encadeada
category: exercicio
subject: Listas Lineares
lesson: 11
---

Utilizando a implementação de pilha encadeada do professor, refazer (ctrl + c e ctrl +v trocando a classe) algum dos exercícios anteriores que utilizou pilha na solução e comparar se os resultados obtidos são os mesmos.

```python
class Nodo:

    # construtor
    def __init__(self):
        self.valor = None
        self.proximo = None

class PilhaEncadeada:

    # construtor
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def empilhar(self, nodo):
        nodo.proximo = self.primeiro
        self.primeiro = nodo

        self.tamanho = self.tamanho + 1

    def vazia(self):
        # se não tem primeiro a lista está vazia
        if self.primeiro == None:
            return True
        else:
            return False

    def desempilhar(self):
        if self.vazia():
            return None
        else:
            # na pilha sempre retorna o primeiro
            nodo = self.primeiro
            # caso tenha mais de um elemento,
            # coloca o segundo como primeiro
            # (redundante)
            if self.primeiro.proximo != None:
                self.primeiro = self.primeiro.proximo
            else:
                self.primeiro = None

            # diminui a quantidade
            self.tamanho = self.tamanho - 1

            return nodo


if __name__ == "__main__":

    # Cria Pilha de camisetas (exerc. 17)
    pilha = PilhaEncadeada()

    # Passo 1 : Criar Nodo
    n1 = Nodo()
    n1.valor = 'Azul'
    pilha.empilhar(n1)

    # Empilha demais cores
    cores = ['Vermelha', 'Branca', 'Verde', 'Preta']
    for cor in cores:
        n = Nodo()
        n.valor = cor

        pilha.empilhar(n)

    print(pilha.tamanho)

    # Imprime a pilha
    while not pilha.vazia():
        camiseta = pilha.desempilhar()
        print(camiseta.valor)


    print(pilha.tamanho)
```