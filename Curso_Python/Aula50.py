"""
Exercício
Exiba os índices da lista
"""
lista = ['Luiz', 'Larissa', 'João']
lista.append('Maria')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

# for nome in lista:
#     print(lista.index(nome), nome, type(nome))