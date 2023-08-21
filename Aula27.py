"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [inicio:fim:passo] [::]
Obs.: a função len retorna a quantidade de caracteres de uma string
"""
variavel = 'Olá mundo'
print(variavel[4:9]) # 'mundo'
print(variavel[4:]) # 'mundo'

print(variavel[0:5]) # 'Olá m'
print(variavel[:5]) # 'Olá m'

print(variavel[-8:-2]) # 'lá mun'

print(len(variavel))
print(len(variavel[3]))


print(variavel[0:9:2]) # 'Oámno'
print(variavel[::-1]) # 'odnum álO'
print(variavel[-1:-10:-1]) # 'odnum álO'