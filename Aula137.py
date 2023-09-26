# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça uma ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, motor):
        self._fabricante = motor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor = Motor('1.0')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor = Motor('2.0')
focus.fabricante = ford
focus.motor = motor
print(focus.nome, focus.fabricante.nome, focus.motor.nome)
