# Context Manager com classes
# Você pode implementar seus próprios protocolos apenas implementando os
# dunder methods que o Python vai usar.
# Isso é chamado de Duck Typing. Um conceito relacionado com tipagem dinâmica
# onde o Python não está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna
# como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__ devem ser
# implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o traceback.
# Se ele retornar True, exceção no with será suprimida.
#
# Exemplo:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        if self._arquivo is not None:
            self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print (class_exception)
        # print (exception_)
        # print (traceback_)
        # exception_.add_note('Minha nota')

        # return True  # Suprime a exceção


# instancia = MyOpen('Aula149.txt', 'w')
# with instancia as obj:
with MyOpen('Aula149.txt', 'w') as obj:  # obj recebe o retorno do método __enter__
    obj.write('Linha 1\n')
    obj.write('Linha 2\n')
    obj.write('Linha 3\n')
    print('WITH', obj)
