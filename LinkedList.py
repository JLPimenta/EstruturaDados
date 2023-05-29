# sequencial = []
# sequencial.append(10)
from Node import Node

#
class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):  # O[N]
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("Index está fora do tamanho da lista")

    def __setitem__(self, index, value):  # O[N]
        pointer = self._getNode(index)
        if pointer:
            pointer.data = value
        else:
            raise IndexError("Index está fora do tamanho da lista")

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + "-> "
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index está fora do tamanho da lista")
        return pointer

    def index(self, elem):  # O[N]
        """Retorna o índice ou elemento na lista"""
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} não está na lista".format(elem))

    def append(self, elem):  # O[N] ->
        if self.head:
            # Já possui elementos? Executa esse bloco
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira vez
            self.head = Node(elem)
            self._size = self._size + 1

    def insert(self, index, elem):  # Insere um novo elemento na lista em qualquer posição
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem):  # Remove um item da lista
        if self.head is None:
            raise ValueError("{} não está na lista".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
        return True


if __name__ == '__main__':
    lista = LinkedList()
    lista.append(7)
    lista.append(10)
    lista.append(54)
    lista.append(9)
    lista.append(31)
