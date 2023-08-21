def executa(funcao, *args):
    return funcao(*args)


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica
# duplica = cria_multiplicador(2)

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))


# def soma(x, y):
#     return x + y
# print(soma(2, 3))

print(
    executa(
        lambda x, y: x + y, 2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        2, 3, 4, 5, 6, 7, 8, 9, 10
    )
)