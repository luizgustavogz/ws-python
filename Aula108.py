# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(start=10, step=8)
r1 = range(8, 100, 8)

# print('c1', hasattr(c1, '__iter__'))    # É um iterável
# print('c1', hasattr(c1, '__next__'))    # É um iterator
# print('r1', hasattr(r1, '__iter__'))    # É um iterável
# print('r1', hasattr(r1, '__next__'))    # Não é um iterator

print('Count')
for i in c1:
    if i > 100:
        break
    print(i)

print('\nRange')
for i in r1:    
    print(i)
