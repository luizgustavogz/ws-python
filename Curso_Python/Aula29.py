"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
num_str = input('Vou dobrar o número que você digitar: ')

try:
    num_float = float(num_str)    
    print(f'FLOAT: {num_float:.2f}')
    print(f'O dobro de {num_str} é = {num_float * 2:.2f}')
except:
    print('Isso não é um número')

# if num_str.isdigit():
#     num_float = float(num_str)
#     print(f'O dobro de {num_str} é = {num_float * 2:.2f}')
# else:
#     print('Isso não é um número')