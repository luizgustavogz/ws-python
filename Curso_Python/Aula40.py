""" Calculadora com while """
while True:    
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ - / *): ')

    numeros_validos = None
    num2_float = 0
    num1_float = 0
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except: 
        numeros_validos = None

    if numeros_validos is None:
        print('Você não digitou um número válido.')
        continue

    operadores_validos = '+-/*'
    if operador not in operadores_validos:
        print('Você não digitou um operador válido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')
    else:
        print('Operador inválido.')

    sair = input('Você deseja sair? [s]im ou [n]ão: ').lower().startswith('s')
    
    if sair is True:
        break