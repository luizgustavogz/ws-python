""" 
Jogo da forca/palavra secreta
- Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palabra secreta, exiba a letra;
    - Se a letra digitada não estiver na palavra secreta, exiba *.
- Faça a contagem de tentativas do usuário.
"""
import os

print('Bem-vindo ao jogo da forca/palavra secreta!')
palavra_secreta = 'quadrado'
letras_acertadas = ''
num_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {num_tentativas} vezes')
        letras_acertadas = ''
        num_tentativas = 0

        sair = input('Deseja jogar novamente? [s]im ou [n]ão: ').lower().startswith('n')
        if sair is True:
            break