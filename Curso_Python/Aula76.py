 # Dicionários em Python (tipo dict)
 # Dicionários são estruturas de dados do tipo par de "chave" e "valor"
 # Chaves podem ser considerados como "índice" que vimos na lista
 # e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.
 # O valor por ser de qualquer tipo, incluindo outro dicionário.
 # Usamos as chaves -> {} ou a classe dict para criar dicionários
 # Imutáveis: str, int, float, bool, tuple
 # Mutável: dict, list

"""     Exemplo de dicionário
# pessoa = dict(nome='Luiz Gustavo', sobrenome='Oliveira')

pessoa = {
    'nome': 'Luiz Gustavo',
    'sobrenome': 'Oliveira',
    'idade': 20,
    'altura': 1.83,
    'endereços': [
        {'Casa': 'Rua tal', 'numero': 123},
        {'Trabalho': 'Rua tal tal', 'numero': 321},
    ],
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
"""

"""     Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Gustavo'
pessoa['sobrenome'] = 'Oliveira'

print(pessoa[chave])

pessoa[chave] = 'João'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('Chave não existe')
else:
    print(pessoa['sobrenome'])
"""

"""     Métodos úteis dos dicionários em Python
len -> quantas chaves
keys -> iterável com as chaves
values -> iterável com os valores
items -> iterável com os itens (chave e valor)
setdefault -> insere uma chave e um valor padrão caso a chave não exista
copy -> retorna uma cópia rasa (shallow copy) do dicionário
get -> obtém uma chave
pop -> apaga um item com a chave especificada (del)
popitem -> apaga o último item inserido
update -> atualiza um dicionário com outro dicionário
"""
pessoa = {
    'nome': 'Luiz Gustavo',
    'sobrenome': 'Oliveira',
    'idade': 20,
}

print(len(pessoa))

print(list(pessoa.keys()))

print(list(pessoa.values()))
for valor in pessoa.values():
    print(valor)

print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

print(pessoa.get('nome'))
print(pessoa.get('nome', 'Chave não existe'))

nome = pessoa.pop('nome')
print(nome)
print(pessoa)

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

pessoa.update({
    'nome': 'novo valor',
    'altura': 1.83,
})
pessoa.update(nome='novo valor', altura=1.83)
tupla = ('nome', 'novo valor'), ('idade', 21)
pessoa.update(tupla)
lista = [['nome', 'novo valor'], ['idade', 21]]
pessoa.update(lista)
print(pessoa)

"""   deepcopy -> necessita do import copy -> retorna uma cópia profunda do dicionário
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)
"""