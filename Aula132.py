# @property + @setter - getter e setter no modo Pythônico
#   - Como getter
#   - Para evitar quebrar código cliente
#   - Para habilitar setter
#   - Para executar ações ao obter um atributo
# Atributos que começam com um ou dois underlines são privados
# não devem ser usados fora da classe.
class Caneta:
    def __init__(self, cor):
        # private / protected
        # self._cor = cor
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no Getter')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('Estou no Setter')
        # if valor == 'Rosa':
        #     raise ValueError('Cor inválida')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print('Cor da tinta:', caneta.cor)
print('Cor da tampa:', caneta.cor_tampa)
