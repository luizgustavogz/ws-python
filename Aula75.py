"""
Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro
"""

# def duplicar(numero):    
#     return f'{numero} duplicado = {numero * 2}'   

# def triplicar(numero):   
#     return f'{numero} triplicado = {numero * 3}'    

# def quadruplicar(numero):    
#     return f'{numero} quadriplicado = {numero * 4}'    


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
