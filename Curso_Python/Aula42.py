frase = 'O Python é uma linguagem de programação multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''
while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i += 1
        continue

    qtd = frase.count(letra)

    if qtd_mais_vezes < qtd:
        qtd_mais_vezes = qtd
        letra_mais_vezes = letra
    
    i += 1
    
print(f'A letra que apareceu mais vezes foi: "{letra_mais_vezes}" (total {qtd_mais_vezes}x)')