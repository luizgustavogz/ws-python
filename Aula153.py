# Método especial __call__
# callable é algo que pdoe ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe "callabe".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando,', self.phone)
        return 2134


call1 = CallMe(123456789)  # Chama a classe callable
retorno = call1('Luiz Gustavo')  # Chama a instância callable
print(retorno)
