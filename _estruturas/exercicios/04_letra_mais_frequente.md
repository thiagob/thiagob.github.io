---
layout: page
title: Letra mais frequente
category: exercicio
subject: Python
class_number: 1
---
Desenvolver uma rotina que percorra uma string e imprima¹qual é a letra mais frequente e a quantidade de vezes que foi encontrada.

Exemplo

    texto = "agua mole, pedra dura, tanto bate ate que fura"
    # 'a'
    # 8 vezes
    
¹ print()

### Exemplos de solução


```python
import string
import random

texto = "agua mole, pedra dura, tanto bate ate que fura"

def limpa_texto(texto):
    texto = texto.replace(' ', '').replace(',', '').upper()
    #print(texto)
    return texto

def letra_mais_frequente_forca_bruta(texto):
    texto = limpa_texto(texto)
    interacoes = 0

    letra = texto[0]
    max = 0

    for lt in texto:
        contagem = 0

        for lt2 in texto:
            # faz a contagem das iterações para comparar as soluções
            interacoes += 1

            if lt == lt2:
                contagem += 1

        if contagem > max:
            max = contagem
            letra = lt

    return [letra, max, interacoes]

def letra_mais_frequente_hash(texto):
    texto = limpa_texto(texto)
    interacoes = 0

    # {'a': 8, 'g': 1, 'u': 4, 'm': 1, 'o': 2, 'l': 1, 'e': 5, 'p': 1, 'd': 2, 'r': 3, 't': 4, 'n': 1, 'b': 1, 'q': 1, 'f': 1}
    letras = {}
    letra = texto[0]
    max = 0

    for lt in texto:
        # faz a contagem das iterações para comparar as soluções
        interacoes += 1 

        if lt not in letras:
            letras[lt] = 0

        letras[lt] += 1

        if letras[lt] > max:
            max = letras[lt]
            letra = lt

    return [letra, max, interacoes]


print('# Força bruta')
print(letra_mais_frequente_forca_bruta(texto))

print('# Hash')
print(letra_mais_frequente_hash(texto))

# gera string randomica de 10 mil caracteres
random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10000))
#print(random_string)

print('# Força bruta')
print(letra_mais_frequente_forca_bruta(random_string))

print('# Hash')
print(letra_mais_frequente_hash(random_string))
```
