class Node: 
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None

class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    def adicionar(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def exibir(self):
        atual = self.inicio

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')

n1.proximo = n2
n2.proximo = n3