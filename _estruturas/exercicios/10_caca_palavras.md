---
layout: page
title: Caça-palavras
category: exercicio
subject: Python
lesson: 3
---
Carregar o caça-palavras em uma matriz e percorrer linhas e colunas até encontrar a palavra Python.
Ao encontrar a palavra, retornar a posição (linha e coluna) e a direção (se vertical ou horizontal).

```
XSXPKWPJMKSTLXRMRHBL
KJTTZQCQSNDZBZQMZKKR
FBTGILXBGCEHIBMKRXHS
KGUJMJRQDIUDBOLCSNRZ
ZZPKBPPLMUEXXAMDSGHZ
MMUQNZYFPDOMTSJEPJZF
DCDJXITPNKMROBMPUZIC
PABYZJHARGTGFWNNGIUH
HWEWWTOKCLHSWHMJHWBE
ZASURRNKORXGIDYHYLRR
```

### Exemplo de solução

```python
# abre o arquivo em modo leitura 'r'
f = open("slides/aula_03/cacapalavra.txt", "r")

# retorna conteúdo do arquivo em um array de strings
matriz = f.readlines()

# fecha o arquivo
f.close()


for lin, linha in enumerate(matriz):
    for col, val in enumerate(linha):
        if val == 'P':

            # Busca PYTHON na horizontal
            # --------------------------

            # Verifica se PYTHON cabe na horizontal
            if col + 5 < len(linha):

                if linha[col + 1] == 'Y' \
                        and linha[col + 2] == 'T' \
                        and linha[col + 3] == 'H' \
                        and linha[col + 4] == 'O' \
                        and linha[col + 5] == 'N':

                    print("Palavra Python encontrada!")
                    print("Linha: " + str(lin + 1))
                    print("Coluna: " + str(col + 1))
                    print("Orientação: vertical")
                    print(linha[:col] + ">>" + linha[col:])

            # Busca PYTHON na vertical
            # ------------------------

            # Verifica se PYTHON cabe na vertical
            if lin + 5 < len(matriz):

                if matriz[lin + 1][col] == 'Y' \
                        and matriz[lin + 2][col] == 'T' \
                        and matriz[lin + 3][col] == 'H' \
                        and matriz[lin + 4][col] == 'O' \
                        and matriz[lin + 5][col] == 'N':

                    print("Palavra Python encontrada!")
                    print("Linha: " + str(lin + 1))
                    print("Coluna: " + str(col + 1))
                    print("Orientação: vertical")

                    for i in range(6):
                        print(matriz[lin + i][:col] + "|" + matriz[lin + i][col] + "|" + matriz[lin + i][col+1:].strip())


# Palavra Python encontrada!
# Linha: 5
# Coluna: 7
# Orientação: vertical
# ZZPKBP|P|LMUEXXAMDSGHZ
# MMUQNZ|Y|FPDOMTSJEPJZF
# DCDJXI|T|PNKMROBMPUZIC
# PABYZJ|H|ARGTGFWNNGIUH
# HWEWWT|O|KCLHSWHMJHWBE
# ZASURR|N|KORXGIDYHYLRR
```
