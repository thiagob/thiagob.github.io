class Nodo:

    # construtor
    def __init__(self):
        self.valor = None
        self.proximo = None

class ListaEncadeada:

    # construtor
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def adicionar(self, nodo):
        # lista vazia
        if self.vazia():
            # adiciona como primeiro
            self.primeiro = nodo
        else:
            # adiciona depois do último
            ultimo = self.ultimo()
            ultimo.proximo = nodo

        self.tamanho = self.tamanho + 1

    def vazia(self):
        # se não tem primeiro a lista está vazia
        if self.primeiro == None:
            return True
        else:
            return False

    # retorna quem é o último
    def ultimo(self):
        if self.vazia():
           return False
        else:
            # percorre até o nodo que não tem próximo (vulgo último)
            nodo = self.primeiro
            while nodo.proximo != None: # não tem próximo
                nodo = nodo.proximo
            return nodo

    def remover(self):
        # por enquanto só diminui a quantidade
        self.tamanho = self.tamanho - 1


# Cria Lista
lista = ListaEncadeada()

# Passo 1 : Criar Nodo
thiago = Nodo()
thiago.valor = 'Thiago'

# Passo #2 Associar o Nodo à Lista
lista.adicionar(thiago)

# Passo 1 : Criar Nodo
joao = Nodo()
joao.valor = 'João'

# Passo 2# Identificar a posição (é o método ultimo())
# Passo #3 Associar o Nodo à Lista
lista.adicionar(joao)

print('Tamanho da Lista: ' + str(lista.tamanho))

print('Primeiro Elemento da Lista (abaixo):')
print(lista.primeiro.valor)
print(lista.primeiro.proximo.valor)

lista.remover()
print('Tamanho da Lista: ' + str(lista.tamanho))


print('------------------------------------------------')



# EXEMPLO 1
n1 = Nodo()
n1.valor = 'Branco'

n2 = Nodo()
n2.valor = 'Azul'

n1.proximo = n2

print('Primeiro Elemento: ' + n1.valor)

print('Próximo Elemento: ' + n1.proximo.valor) # 'Azul'
print('Segundo Elemento: ' + n2.valor) # 'Azul'

if n2.proximo == None:
    print('n2 é o último elemento')
