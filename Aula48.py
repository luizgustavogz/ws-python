"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append -> Adiciona um item ao final
    insert -> Adiciona um item no índice escolhido
    pop -> Remove do final ou do índice escolhido
    del -> Apaga um índice
    clear -> Limpa a lista
    extend -> Estende a lista
    + -> Concatena listas
Create, Read, Update, Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

"""
# print(bool([])) # falsy
# print(lista, type(lista))

# lista = [123, True, 'Luiz Gustavo', 1.2, []]
# lista[-3] = 'Larissa'
# print(lista)
# print(lista[2], type(lista[2]))

lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(70)
lista.pop()
lista.append(80)
ultimo_valor = lista.pop(3)
print(lista, 'Removido:', ultimo_valor)

lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)
"""

"""
Cuidado com dados mutáveis
= -> copiado o valor (imutáveis)
= -> aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Larissa', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)