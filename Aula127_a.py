# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados
import json

CAMINHO_ARQUIVO = 'Aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Luiz', 21)
p2 = Pessoa('João', 21)
p3 = Pessoa('Larissa', 23)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as file:
        print('Fazendo dump...')
        json.dump(bd, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    fazer_dump()
