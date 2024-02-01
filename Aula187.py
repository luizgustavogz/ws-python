# sys.argv - Executando arquivos com argumentos no sistema
# sys.argv é uma lista que contém os argumentos passados para o script Python.
# Com sys.argv, você pode acessar os argumentos do script via linha de comando.
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltam argumentos')
else:
    try:
        print(f'Você passou os argumentos: {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça alguma coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
