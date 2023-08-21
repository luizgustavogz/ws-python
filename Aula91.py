# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0):
#     yield 1     # Pausar a função e retornar o valor
#     print('Continuando...')
#     yield 2
#     print('Mais uma...')
#     yield 3
#     print('Fim')
#     return 'Acabou'

# gen = generator(n=0)
# for n in gen:
#     print(n)


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(maximum=100000)
for n in gen:
    print(n)
