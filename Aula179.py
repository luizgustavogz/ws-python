# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'Aula179.csv'

print('---- reader ----')
with open(CSV_PATH, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)

print('\n---- DictReader ----')
with open(CSV_PATH, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for line in reader:
        print(line['Nome'], line['Idade'], line['Endereço'])
