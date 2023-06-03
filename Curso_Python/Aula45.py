"""
For por "debaixo dos panos" - Como o for funciona/é executado
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> entrega o próximo valor
iter -> entrega seu iterador
"""

# texto = iter('Luiz') # .__iter__()
# print(next(texto)) # .__next__()


texto = 'Luiz' # iterável
iterator = iter(texto) # iterator

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

# for letra in texto:
#     print(letra)