# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos um determinado
# número de coisas.
# Enums têm membris e seus valores são constantes.
# Enums em Python:
#     - São um conjunto de nomes simbólicos (membros) ligados a valores únicos;
#     - Podem ser iterados para retornar seus membros canônicos na ordem
#         de definição.
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
# diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e outras
# coisas relacionadas com tipo.
# Para obter os dados:
# chave = Classe.chave.name, Class(valor), Classe['chave']
# valor = Classe.chave.value
def mover(direcao):
    print(f'Movendo para {direcao}')


mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')
