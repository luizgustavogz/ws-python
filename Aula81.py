"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python.
Porém, são funções anônimas, que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma única expressão.
"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Cunha'},
    {'nome': 'Larissa', 'sobrenome': 'Cardoso'},
    {'nome': 'João', 'sobrenome': 'Motta'}    ,
]

# def ordena(item):
#     return item['sobrenome']
# lista.sort(key=ordena)

def exibir(lista):
    for item in lista:
        print(item)
    print()

# lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)