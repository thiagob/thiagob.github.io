---
layout: page
title: Primeira em Árvore
category: exercicio
subject: Árvores
lesson: 13
---

Utilizando o exemplo escolhi no exercício 29, fazer a implementação da árvore utilizando a classe abaixo como exemplo. Existem muitas formas de fazer uma implementação de árvore, não precisa se limitar a esta ;).

O atritubuto Tipo define se o nó é apenas um nó, ou se é um nó raiz ou folha.

```
,---------------------------.
|NoArvoreBinaria            |
|---------------------------|
|+ Valor: String            |
|+ Tipo: String             |
|+ Nivel: Integer           |
|+ Esquerda: NoArvoreBinaria|
|+ Direita: NoArvoreBinaria |
`---------------------------'
```

```python
class NoArvoreBinaria:

    def __init__(self):
        self.valor = None
        self.tipo = None
        self.nivel = 0
        self.esquerda = None
        self.direita = None


# Exemplo:
# Raiz
raiz = NoArvoreBinaria()
raiz.tipo = "Raiz"
raiz.valor = "A"
raiz.nivel = 0  

print(raiz.tipo + ' - ' + raiz.valor)

# B 
b = NoArvoreBinaria()
b.tipo = "Folha"
b.valor = "B"
b.nivel = 1  

# Verão enxuta da impressão da área:
print('#   ' + raiz.direita.valor + ' (Nível ' + str(raiz.direita.nivel) + ' - ' + raiz.direita.tipo + ')')
print('#  /')
print('# ' + raiz.valor + ' (Nível ' + str(raiz.nivel) + ' - ' + raiz.tipo + ')')
print('#  \\')
print('#   ' + raiz.esquerda.valor + ' (Nível ' + str(raiz.esquerda.nivel) + ' - ' + raiz.esquerda.tipo + ')')

```