# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# lista = []
# for num in range(10):
#     lista.append(num)
# print(lista)


    # List Comprehension
# lista = [num for num in range(10)]  
# print(lista)

# lista = [
#     num * 2 for num in range(10)    
# ]
# print(lista)


    # Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

    # Filtro de dados em list comprehension (Filtro a direita do for)
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 > 10)
]
p(novos_produtos)

"""
Anotações:
    Mapeamento
Pegar um dado e ter a possibilidade de transformar esse dado
jogando numa outra lista (ou outro iterável) do mesmo tamanho.
    Filtro
Pode ou não pegar um dado e incluir numa outra lista (ou outro iterável)
"""