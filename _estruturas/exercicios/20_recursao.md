---
layout: page
title: Exemplos de Recursão e Iteração
category: exercicio
subject: Listas Lineares
lesson: 8
---
Revisar, rodar e debugar os exemplos de iteração e recursão construídos em aula.

### Contagem regressiva
```python
import time

def conta_recursiva(n):
    # parada
    if n < 1:
        return

    # ação prioriamente dita
    print('>>> ' + str(n))
    time.sleep(1) # aguarda 1 segundo

    # recursão
    conta_recursiva(n - 1)


def conta_iterativa(n):
    for i in range(n):
        print(n - i)
        time.sleep(1) # aguarda 1 segundo
    return


# def conta_5():       
#     conta(5)

#     conta_4()

# def conta_4():       
#     conta(4)

#     conta_3()

# def conta_3():       
#     conta(3)

#     conta_2()

# def conta_2():       
#     conta(2)

#     conta_1()

# def conta_1():       
#     conta(1)

    
    

#conta_5()

conta_recursiva(5)
print('Feliz Ano NOVO!!')

conta_iterativa(5)
print('Feliz Ano NOVO!!')

#conta_4()
```

