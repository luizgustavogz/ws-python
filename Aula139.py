# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, derived class, child class

# class MinhaString(str):
#     def upper(self):
#         print('Chamou o upper')
#         return super().upper()  # super(MinhaString, self)


# string = MinhaString('Luiz')
# print(string.upper())


class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('Classe A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('Classe B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('Burlei o sistema...')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()
        super(B, self).metodo()  # Explícito, classe inicial B
        # super(A, self).metodo()  # object
        # A.metodo(self)
        # B.metodo(self)
        print('Classe C')


c = C('Atributo', 'Qualquer')
print(c.atributo, c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
