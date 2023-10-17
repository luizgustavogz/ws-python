# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender várias outras classes
#
# Herança Simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
#
# Herança Múltipla e Mixins:
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# Problema do diamante:
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
#     A
#   /   \
#  B     C
#   \   /
#     D
#
# Python 3 usa C3 superclass linearization algorithm para gerar o MRO.
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos,
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)
class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    # def quem_sou(self):
    #     print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
# print(D.__mro__)
print(D.mro())
