# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi1 = multiplica(1, 2, 3, 4, 5)
print(multi1)
print(multiplica(10, 2, 3, 4, 5))


# Crie uma função que fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é Par'
    return f'{numero} é Ímpar'

outro_par_impar = par_ou_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_ou_impar(3))
print(par_ou_impar(15))
print(par_ou_impar(16))

print(par_ou_impar is outro_par_impar)