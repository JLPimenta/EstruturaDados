# Inserir
# Remover
# Topo da pilha
from Node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

    def push(self, elem):  # O[1]
        # Insere um item no topo da pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):  # O[1]
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("A pilha está vazia.")

    def peek(self):  # O[1]
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia.")

    def index(self, elem):  # O[N]
        """Retorna o índice ou elemento na lista"""
        pointer = self.top
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} não está na lista".format(elem))
