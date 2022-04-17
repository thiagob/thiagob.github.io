---
layout: page
title: Algoritmos de Ordenação
category: exercicio
subject: Listas Lineares
lesson: 8
---

Em sua biblioteca de funções/classes criar um novo arquivo ```ordenacao.py``` para que possas importá-lo nos próximos exercícios.


# Problema
* Neste arquivo faça a implementação dos algoritmos de ordenacao Bubble Sort e Quick Sort conforme tempalte abaixo:


### Template
```python
#############################################################
# para aumentar o limite de recursão
#############################################################
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(5000)
#############################################################

def bubble_sort(arr):
    return arr

# parametro= define o valor padrão e torna o parâmetro opcional
def quick_sort(arr, idx_ini=-1, idx_fim=-1):

    # se receber valor, usa o valor definido, são atribui
    idx_ini = idx_ini if idx_ini >= 0 else 0
    idx_fim = idx_fim if idx_fim >= 0 else len(arr)-1

    # implementar causa de saída da recursão
    # if ? return

    # define posição para o primeiro pivô
    arr, pivo_index = quick_sort_partition(arr, idx_ini, idx_fim)

    # faz quick sort na primeira metdade do arr

    # faz quick sort na segunda metdade do arr

    return arr

def quick_sort_partition(arr, idx_ini, idx_fim):

    pivo_index = 0

    return arr, pivo_index

print(bubble_sort([4, 3, 2, 7, 5, 1]))

arr = [7, 2, 1, 8, 6, 3, 5, 4]
arr = quick_sort(arr)
print(arr)

arr = [0, 7, 2, 1, 8, 6, 3, 5, 10, 4]
arr = quick_sort(arr)
print(arr)

a_str = ["azul", "amarelo", "verde", "roxo"]
a_str = quick_sort(a_str)
print(a_str)

a_str = bubble_sort(a_str)
print(a_str)
```