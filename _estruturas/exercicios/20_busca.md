---
layout: page
title: Algoritmos de Busca
category: exercicio
subject: Listas Lineares
lesson: 8
---
Em sua biblioteca de funções/classes criar um novo arquivo ```busca.py``` para que possas importá-lo nos próximos exercícios.

# Problema
* Neste arquivo faça a implementação dos algoritmos de busca linear e binária conforme tempalte abaixo:

### Template
```python
def busca_linear(arr, elemento):
    return None

def busca_binaria(arr, elemento, idx_ini = -1, idx_fim = -1):

    # = -1 é o valor padrão do parâmetro
    # quando o parâmetro tem um valor padrã ele é opcional
    idx_ini = idx_ini if idx_ini >= 0 else 0
    idx_fim = idx_fim if idx_fim >= 0 else len(arr)

    return None

def busca_binaria_iterativa(arr, elemento):
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
```
### Exemplo

[Exemplo do Professor](https://github.com/thiagob/thiagob.github.io/blob/main/_estruturas/exercicios/20_busca.py)