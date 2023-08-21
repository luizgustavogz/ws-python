# from sys import path
# print(*path, sep='\n')

# import Aula99_package.modulo
# from Aula99_package import modulo
# from Aula99_package.modulo import *
# from Aula99_package.modulo import soma_do_modulo as sdm

# print(soma_do_modulo(1, 2))
# print(Aula99_package.modulo.soma_do_modulo(2, 3))
# print(modulo.soma_do_modulo(1, 2))
# print(sdm(2, 3))
# print(variavel)
# print(nova_variavel)

# from Aula99_package.modulo import soma_do_modulo, fala_oi

# fala_oi()


from Aula99_package import soma_do_modulo, fala_oi
print(soma_do_modulo(1, 2))
fala_oi()