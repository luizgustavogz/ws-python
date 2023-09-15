# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes conveções:
#   public -> (sem underline)
#       Pode ser usado em qualquer lugar.
#   protected -> _ (um underline)
#       NÃO DEVE ser usado fora da classe ou sublcasses.
#   private -> __ (dois underlines)
#       "name mangling" (desfiguração de nomes) em Python
#       SÓ DEVE ser usado na classe em que foi declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'

    def public_method(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__private)
        self.__private_method()
        return 'public_method'

    def _protected_method(self):
        print('_protected_method')
        return '_protected_method'

    def __private_method(self):
        print('__private_method')
        return '__private_method'


f = Foo()
# print(f.public)
print(f.public_method())
