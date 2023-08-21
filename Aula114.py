"""
Funções recursivas e recursividade
  - Funções que podem se chamar de volta
  - Úteis para dividir problemas grandes em partes menores
Toda função recursiva deve ter:
  - Um problema que possa ser dividido em partes menores
  - Um caso recursivo que resolve o pequeno problema
  - Um caso base que para a recursão
  - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.uol.com.br/matematica/fatorial.htm
"""

# import sys

# sys.setrecursionlimit(1004)

# def recursiva(start=0, stop=10):

#     print(start, stop)

#     # Caso base (caso de segurança/condição de parada)
#     # if start >= stop:
#     #     return stop
    
#     # Caso recursivo: contar até chegar ao final
#     start += 1
#     return recursiva(start, stop) # if start < stop else stop       # Caso base

# print(recursiva())
# # print(recursiva(0, 1001))


def factorial(n):
    # Caso base
    if n <= 1:
        return 1
    
    # Caso recursivo
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(100))
