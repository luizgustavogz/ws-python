# Yield from
def gen1():
    yield 1
    yield 2
    yield 3
    print('Fim gen1')

def gen2(gen=None):
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Fim gen2')

def gen3():
    yield 10
    yield 20
    yield 30
    print('Fim gen3')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for n in g1:
    print(n)
print()

for n in g2:
    print(n)
print()

for n in g3:
    print(n)
print()