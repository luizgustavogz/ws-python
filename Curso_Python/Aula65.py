"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornan None (nada).
"""

# def Print():
#     print('Hello World')
#     print('Hello World1')
#     print('Hello World2')
#     print('Hello World3')

# Print()


# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Gustavo')
saudacao('Larissa')
saudacao('João')
saudacao()