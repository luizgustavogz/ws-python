# Herança simples - Relações entre classes
# Associação -> usa / Agregação -> tem
# Composição -> é dono de / Herança -> É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, derived class, child class
#
# MRO (Method Resolution Order)
#   -> Ordem de execução dos métodos
#   -> A ordem de execução dos métodos é definida pela ordem de herança
#   -> Cliente/Aluno > Pessoa > Object (builtin)
class Pessoa:
    cpf = '123.456.789-00'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Luiz', 'Cunha')
c1.falar_nome_classe()
a1 = Aluno('Larissa', 'Cardoso')
a1.falar_nome_classe()
# print(a1.cpf)
# help(Cliente)
