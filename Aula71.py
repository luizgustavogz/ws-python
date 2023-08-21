"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:        
        total += numero
    return total

# soma1 = soma(1, 2, 3)
# print(soma1)

# soma2 = soma(4, 5, 6)
# print(soma2)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
soma3 = soma(*numeros)
print(soma3)

print(sum(numeros))
# print(*numeros)