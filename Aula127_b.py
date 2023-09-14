import json

from Aula127_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as file:
    pessoas = json.load(file)

    for pessoa in pessoas:
        p = Pessoa(**pessoa)
        print(p.nome, p.idade)
