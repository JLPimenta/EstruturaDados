from Node import Node


# Inserir no fim da fila
# Remover do início da fila
# Observar começo da fila
class QueueTest:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            response = ""
            pointer = self.first
            while pointer:
                response = response + str(pointer.data) + " "
                pointer = pointer.next
            return response
        else:
            return "A fila está vazia."

    def __str__(self):
        return self.__repr__()

    def push(self, elem):  # O[1]
        # Insere um elemento no final da fila
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):  # O[1]
        # Remove o primeiro elemento da fila
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        raise IndexError("A fila está vazia.")

    def peek(self):  # O[1]
        # Retorna o primeiro item da fila
        if self.first is not None:
            elem = self.first.data
            return elem
        raise IndexError("A fila está vazia.")
