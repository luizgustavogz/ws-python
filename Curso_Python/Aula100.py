""" 
Exercícios
1 - Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)

2 - Ordene os produtos por nome decrescente (do maior pro menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

3 - Ordene os produtos por preço crescente (do menor pro maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
import copy

from Aula100_package import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda produto: produto['nome'],
#     reverse=True
# )

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda produto: produto['nome'], reverse=True)

# produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda produto: produto['preco']
# )

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda produto: produto['preco'])


print('Produtos originais:', *produtos, sep='\n')
print()
print('Novos produtos (10% aumento do preço):', *novos_produtos, sep='\n')
print()
print('Produtos ordenados por nome decrescente:', *produtos_ordenados_por_nome, sep='\n')
print()
print('Produtos ordenados por preço crescente:', *produtos_ordenados_por_preco, sep='\n')
print()
