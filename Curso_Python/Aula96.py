# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/pt-br/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# platform = 'A minha'
# print(sys.platform)
# print(platform)


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# print(platform)


# alias 1 - import nome_modulo as alias

# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as alias

# from sys import exit as ex 
# from sys import platform as pf

# print(pf)


# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da lingaguem


# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: 

from sys import *

print(platform)
exit()
