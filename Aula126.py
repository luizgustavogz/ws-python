# __dict__ e vars para atributos e instâncias
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


dados = {'nome': 'Luiz', 'idade': 21}
p1 = Pessoa(**dados)
# p1.nome = 'EITA'
# # print(p1.idade)
# p1.__dict__['altura'] = 1.80
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.altura)
# print(p1.nome)

print(vars(p1))
print(p1.nome)
