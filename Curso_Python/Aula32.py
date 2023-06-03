"""
Programa que peça um número inteiro, informe se é par ou ímpar. 
Caso não digite um número inteiro, informe que não é um número inteiro
"""
num_str = input('Digite um número inteiro: ')

try:
    num_int = int(num_str) % 2 == 0
    if num_int:
        print(f'O número {num_str} é par')
    else:
        print(f'O número {num_str} é ímpar')
except:
    print('Isso não é um número inteiro')


"""
Programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudação apropriada. Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora_str = input('Digite a hora atual (0-23): ')

try:
    hora = int(hora_str)
    if hora >= 0 and hora <= 11:
        print(f'Bom dia! São {hora} horas.')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde! São {hora} horas.')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite! São {hora} horas.')
    else:
        print('Não conheço essa hora')
except:
    print('Isso não é um número inteiro')


"""
Programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos 
escreva "Seu nome é curto". Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"
Maior que 6 escreva "Seu nome é muito grande"
"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais que um caractere')