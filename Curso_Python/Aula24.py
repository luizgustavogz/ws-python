# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  p y t h o n
# -6-5-4-3-2-1

"""
nome = 'Python'
# print(nome[2])
# print(nome[-4])
print('Py' in nome)
print('zo' in nome)
print(10 * '-')
print('Py' not in nome)
print('zo' not in nome)
"""

nome = input('Digite seu nome: ')
encontrar = input('Qual letra deseja encontrar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')