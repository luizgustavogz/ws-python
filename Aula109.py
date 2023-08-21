# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repetição de valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Larissa',
]
camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['masculino', 'feminino', 'unissex'],
    ['algodão', 'poliéster', 'linho'],
    ['estampada', 'lisa', 'listrada'],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
