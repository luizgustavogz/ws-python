""" 
i = 0
tamanho = len(texto)
while i < tamanho:
    print(texto[i], i)
    i += 1 
"""
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')