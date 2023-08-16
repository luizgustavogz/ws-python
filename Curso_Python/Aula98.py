import importlib

import Aula98_m

print(Aula98_m.variavel)

for i in range(10):
    importlib.reload(Aula98_m)
    print(i)

print('Fim')
