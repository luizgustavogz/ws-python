# Desempacotamento em chaamdas de métodos e funções
string = 'ABCD'
lista = ['Luiz', 'Larissa', 1, 2, 3, 'Gustavo']
tupla = 'Python', 'é', 'legal'

salas = [['Maria', 'Helena', ], ['Elaine', ], ['Luiz', 'João', 'Larissa']]

# p, b, *_, ap, u = lista
# print(p, u)

# print(*lista) # print('Luiz', 'Larissa', 1, 2, 3, 'Gustavo')
# print(*string) # print('A', 'B', 'C', 'D')
# print(*tupla) # print('Python', 'é', 'legal')

print(*salas, sep='\n')