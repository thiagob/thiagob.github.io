#############################################################
# para aumentar o limite de recursão
#############################################################
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(5000)
#############################################################

from gerador import Gerador

def bubble_sort(arr):
    troca = True

    while troca:
        troca = False

        for i in range(len(arr)-1):

            if arr[i] > arr[i+1]:
                maior = arr[i]
                menor = arr[i+1]

                arr[i] = menor
                arr[i+1] = maior

                troca = True

    return arr

# parametro= define o valor padrão e torna o parâmetro opcional
def quick_sort(arr, idx_ini=-1, idx_fim=-1):

    # valor padrão quando não foi passado por parâmetro
    if idx_ini < 0:
        idx_ini = 0

    # valor padrão quando não foi passado por parâmetro
    if idx_fim < 0:
        idx_fim = len(arr)-1

    # percorreu todo o array
    if idx_ini >= idx_fim:
        return arr

    # define posição para o primeiro pivô
    arr, pivo_index = quick_sort_partition(arr, idx_ini, idx_fim)

    # faz quick sort na primeira metdade do arr
    arr = quick_sort(arr, idx_ini, pivo_index - 1)

    # faz quick sort na segunda metdade do arr
    arr = quick_sort(arr, pivo_index + 1, idx_fim)

    return arr

# método do primeiro video (copinhos)
def quick_sort_partition(arr, idx_ini, idx_fim):
    if idx_ini >= idx_fim:
        return arr

    # ultimo elemento é definido como pivô
    pivo = arr[idx_fim]
    
    i = idx_ini - 1
    j = idx_ini

    while arr[j] != pivo:
        if arr[j] < pivo:
            i += 1
            # inverte as posições
            arr[j], arr[i] = arr[i], arr[j]
        j += 1

    pivo_index = i + 1

    # remove o pivô e adiciona depois da posição i
    arr.remove(pivo)
    arr.insert(i + 1, pivo)

    return arr, pivo_index

#print(bubble_sort([4, 3, 2, 7, 5, 1]))

arr = [7, 2, 1, 8, 6, 3, 5, 4]
arr = quick_sort(arr)
print(arr)

arr = [0, 7, 2, 1, 8, 6, 3, 5, 10, 4]
arr = quick_sort(arr)
print(arr)

unsorted_arr = Gerador.gerar_array_int(20, 1000)

print('Quick Sort')
arr = quick_sort(unsorted_arr)
print(arr)

print('Bubble Sort')
arr = bubble_sort(unsorted_arr)
print(arr)


a_str = ["azul", "amarelo", "verde", "roxo"]
a_str = quick_sort(a_str)
print(a_str)

a_str = bubble_sort(a_str)
print(a_str)