def busca_linear(arr, elemento):
    for idx, val in enumerate(arr):
        if val == elemento:
            return val

    return None

def busca_binaria(arr, elemento, idx_ini = -1, idx_fim = -1):
    
    # = -1 é o valor padrão do parâmetro
    # quando o parâmetro tem um valor padrã ele é opcional
    idx_ini = idx_ini if idx_ini >= 0 else 0
    idx_fim = idx_fim if idx_fim >= 0 else len(arr)

    if idx_ini > idx_fim:
        return None

    # // divide e arredonda para baixo
    meio = (idx_ini + idx_fim) // 2

    if arr[meio] == elemento:
        return arr[meio]

    elif elemento > arr[meio]:
        return busca_binaria(arr, elemento, meio + 1, idx_fim)

    elif elemento < arr[meio]:
        return busca_binaria(arr, elemento, idx_ini, meio - 1)

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

print('Linear')
print(busca_linear(a_int, 4))
print(busca_linear(a_int, 6))
print(busca_linear(a_str, "azul"))

print('Binary')
print(busca_binaria(a_int, 5))
print(busca_binaria(a_int, 2))
print(busca_binaria_iterativa(a_int, 2))
print(busca_binaria(a_int, 6))
print(busca_binaria_iterativa(a_int, 6))
print(busca_binaria(a_str, "azul"))