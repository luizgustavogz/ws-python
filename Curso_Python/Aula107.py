"""
Exercício - Unir listas
Crie uma função zipper (como zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado:
[(Salvador, BA), (Ubatuba, SP), (Belo Horizonte, MG)]
"""

# from itertools import zip_longest

# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(cidades, estados)))
# print(list(zip_longest(cidades, estados, fillvalue='Sem Cidade')))


# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]

# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(cidades, estados))



"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

====================== Resultado
lista_soma = [2, 4, 6, 8]
"""

from itertools import zip_longest

l1 = [10, 2, 3, 4, 5]
l2 = [12, 2, 3, 6, 50, 60, 70]

def soma_listas(l1, l2):
    print('Soma listas curtas (zip):')
    return [x + y for x, y in zip(l1, l2)]

def soma_listas_longas(l1, l2):
    print('\nSoma listas longas (zip_longest):')
    return [x + y for x, y in zip_longest(l1, l2, fillvalue=0)]

print(f'Listas originais: \nL1: {l1}\nL2: {l2}\n')
print(soma_listas(l1, l2))
print(soma_listas_longas(l1, l2))


# lista_soma = []
# for i in range(len(l2)):
#     lista_soma.append(l1[i] + l2[i])
# print(lista_soma)


# lista_soma = []
# for i, _ in enumerate(l2):
#     lista_soma.append(l1[i] + l2[i])
# print(lista_soma)
