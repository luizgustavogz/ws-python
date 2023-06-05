"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Luiz', 'Larissa', 'João']
lista.append('Maria')

# lista_enumerada = enumerate(lista)
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for item in enumerate(lista):
#     indice, nome, = item
#     print(indice, nome)

for indice, nome in enumerate(lista):     
    print(indice, nome)