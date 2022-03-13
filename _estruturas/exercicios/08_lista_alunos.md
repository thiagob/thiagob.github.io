---
layout: page
title: Lista de alunos
category: exercicio
subject: Python
class_number: 2
---
1. Criar uma classe Aluno que possua os seguintes atributos:
    * Nome: string
    * Curso: string
2. Montar uma lista (array) contendo 3 alunos diferentes
3. Percorrer esta lista imprimindo os nomes dos alunos e do curso

### Exemplo de solução

```python
class Aluno:

    nome = ''
    curso = ''


joao = Aluno()
joao.nome = 'João'
joao.curso = 'Economia'

maria = Aluno()
maria.nome = 'Maria'
maria.curso = 'Matemática'

jose = Aluno()
jose.nome = 'José'
jose.curso = 'Administração'

alunos = [joao, maria, jose]

for a in alunos:
    print('Aluno: ' + a.nome + ' | Curso: ' + a.curso)
```
