# argparse.ArgumentParser para argumentos mais complexos
# Tutorial oficial: https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo', # Valor padrão
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+', # Recebe mais de um valor
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true',  # Recebe um valor booleano
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

# cls; venv\\Scripts\python Aula188.py -b 123
# cls; venv\\Scripts\python Aula188.py --help
# cls; venv\\Scripts\python Aula188.py -b "A" -b "B" -b "C"

print(args.verbose)
# cls; venv\\Scripts\python Aula188.py -b "A" -b "B" -b "C" -v