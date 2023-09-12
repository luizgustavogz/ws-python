# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instancias) que podem ter
# seus próprios atributos e métodos.
# Os objetos gerados pela classse podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Cunha')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Cunha'
print(p1.nome, p1.sobrenome)

p2 = Pessoa('Larissa', 'Cardoso')
# p2.nome = 'Larissa'
# p2.sobrenome = 'Cardoso'
print(p2.nome, p2.sobrenome)
