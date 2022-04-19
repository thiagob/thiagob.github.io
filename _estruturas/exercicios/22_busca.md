---
layout: page
title: Algoritmos de Busca
category: exercicio
subject: Listas Lineares
lesson: 8
---
Em sua biblioteca de funções/classes criar um novo arquivo ```busca.py``` para que possas importá-lo nos próximos exercícios.

# Problema
* Neste arquivo faça a implementação dos algoritmos de busca linear e binária **recursiva** tempalte abaixo.
### Template

```python
def busca_linear(arr, elemento):
    return None

def busca_binaria_recursiva(arr, elemento_buscado, inicio, fim):
    return None

a_str = ["amarelo", "azul", "branco", "roxo", "verde", "vermelho", "violeta"]

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

########################################
# array com quantidade par de elementos
########################################
a_str.append("rosa")
a_str.sort()

print(a_str)

print(busca_binaria_recursiva(a_str, "vermelho", 0, len(a_str) - 1))
print(busca_binaria_recursiva(a_str, "violeta", 0, len(a_str) - 1))
```

### Exemplo

[Exemplo do Professor](https://github.com/thiagob/thiagob.github.io/blob/main/_estruturas/exercicios/22_busca.py)