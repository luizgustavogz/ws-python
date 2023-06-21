# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática. Representados pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas imutáveis como valor interno

# s1 = set() # set vazio
# s1 = {'Luiz', 1, 2, 3} # set com dados


# Sets são eficientes para remover valores duplicados de iteráveis
#     - Seus valores serão sempre únicos;
#     - Não aceitam valores mutáveis;
#     - Eles não tem índexes;
#     - Eles não garantem ordem;
#     - Eles são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

    
# Métodos úteis:
# add, update, clear, discard
#     -> add(valor): adiciona um valor ao set
#     -> update(iteravel): adiciona vários valores ao set
#     -> clear(): limpa o set
#     -> discard(valor): remove um valor do set
#     -> copy(): retorna uma cópia do set
    
# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s2 = s1.copy()
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# print(s1)


# Operadores úteis:
# união | union - Une
#     -> union( | ): retorna a união de dois sets
# intersecção & intersection - Itens em ambos
#     -> intersection( & ): retorna a intersecção de dois sets
# diferença - Itens presentes penas no set da esquerda
#     -> difference( - ): retorna a diferença de dois sets
# diferença simétrica ^ symmetric_difference - Itens que não estão em ambos
#     -> symmetric_difference( ^ ): retorna a diferença simétrica de dois sets

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2    # {1, 2, 3, 4}
s3 = s1 & s2    # {2, 3}
s3 = s2 - s1    # {4}
s3 = s1 ^ s2    # {1, 4}
print(s3)