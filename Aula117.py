import json

pessoa = {
    'nome': 'Luiz Gustavo',
    'sobrenome': 'Oliveira Cunha',
    'enderecos': [
        {'rua': 'Rua 1', 'numero': 123},
        {'rua': 'Rua 2', 'numero': 321},
    ],
    'altura': 1.80,
    'idade': 21,
    'numeros_preferidos': [5, 7, 18, 22],
    'dev': True,
    'nada': None,
}

with open('Aula117.json', 'w', encoding='utf8') as file:
    json.dump(pessoa, file, ensure_ascii=False, indent=2)


with open('Aula117.json', 'r', encoding='utf8') as file:
    pessoa = json.load(file)
    # print(pessoa)
    print(pessoa['nome'])
