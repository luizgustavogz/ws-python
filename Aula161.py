# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementado seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values) -> None:
        for value in values:
            # self._data[len(self._data)] = value
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        # return len(self._data)
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('João', 'Pedro')
    lista[0] = 'Luiz'
    lista.append('Larissa')
    # print(lista[0])
    # print(len(lista))
    print('---//---')
    for item in lista:
        print(item)
    print('---//---')
    for item in lista:
        print(item)
    print('---//---')
