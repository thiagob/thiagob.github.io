def busca_binaria_iterativa(arr, elemento):

    ini = 0
    fim = len(arr) - 1

    while ini <= fim:

        meio = (ini + fim) // 2

        if arr[meio] == elemento:
            return arr[meio]

        elif elemento > arr[meio]:
            ini = meio + 1

        elif elemento < arr[meio]:
            fim = meio - 1

    # não encontrou
    return None


a_int = [1, 2, 3, 4, 5, 9, 10]
a_str = ["amarelo", "azul", "roxo", "verde"]


print('Binary')
print(busca_binaria_iterativa(a_int, 2))
print(busca_binaria_iterativa(a_int, 6))
