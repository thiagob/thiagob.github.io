def busca_linear(arr, elemento):
    for idx, val in enumerate(arr):
        if val == elemento:
            return val

    return None

def busca_binaria_recursiva(arr, elemento_buscado, inicio, fim):

    # quando o inicio e fim se transpassam, quer dizer que o elemento não está na lista
    if fim < inicio:
        return None

    # começamos assim
    # posicao_meio = len(arr) // 2
    posicao_meio = (inicio + fim) // 2
    valor_meio = arr[posicao_meio]

    if elemento_buscado == valor_meio:
        return valor_meio
    elif elemento_buscado > valor_meio:
        # busca à direita do meio + 1 até o final
        return busca_binaria_recursiva(arr, elemento_buscado, posicao_meio + 1, fim)
        #                                                     ================ >>>
    elif elemento_buscado < valor_meio:
        # busca à esquerda da inicio até o meio - 1
        return busca_binaria_recursiva(arr, elemento_buscado, inicio, posicao_meio - 1)
        #                                                        <<<  ================        

def busca_binaria_iterativa(arr, elemento):
    return None

a_str = ["amarelo", "azul", "branco", "roxo", "verde", "vermelho", "violeta"]
# posição   0         1        2       | 3 |     [4         5           6]

# arr[meio] a cor que está na posição meio (3) >> arr[3] = roxo
# tamanho do array = 7
# meio >> 7 // 2 = 3 ("//" quer dizer divide e arredonda para baixo)

print('Binaria')

# inicio = 0, fim = 6
print(busca_binaria_recursiva(a_str, "roxo", 0, 6)) 
# inicio = 0, fim = 6
print(busca_binaria_recursiva(a_str, "vermelho", 0, 6))
# inicio = 0, fim = 6
print(busca_binaria_recursiva(a_str, "azul", 0, 6))

# inicio = 0, fim = 6
print(busca_binaria_recursiva(a_str, "branco", 0, 6))

# inicio = 0, fim = 6
print(busca_binaria_recursiva(a_str, "violeta", 0, 6))

######################
# cor que não existe
######################

# inicio = 0, fim = 6
print(busca_binaria_recursiva(a_str, "bege", 0, 6))

# ["amarelo", "azul", "branco", "roxo", "verde", "vermelho", "violeta"]
# >                                |                                  <
# >             |             <     
#                     >       <     bege < branco
#                     >       <     bege < branco
#                   < >             fim = 1, inicio = 2>> quer dizer que o elemento não está na lista



# array com número par
a_str.append("rosa")
a_str.sort()

print(a_str)

print(busca_binaria_recursiva(a_str, "vermelho", 0, len(a_str) - 1))
print(busca_binaria_recursiva(a_str, "violeta", 0, len(a_str) - 1))