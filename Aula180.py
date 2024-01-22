# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'Aula180.csv'

clients_list = [
    {'Nome': 'Luiz Gustavo', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# with open(CSV_PATH, 'w', encoding='utf-8') as file:
#     columns_name = clients_list[0].keys()
#     writer = csv.DictWriter(
#         file,
#         fieldnames=columns_name
#     )
#     writer.writeheader()

#     for client in clients_list:
#         print(client)
#         writer.writerow(client)

clients_list = [
    ['Luiz Gustavo', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]

with open(CSV_PATH, 'w', encoding='utf-8') as file:
    # columns_name = lista_clients[0].keys()
    columns_name = ['Nome', 'Endereço']
    writer = csv.writer(file)

    writer.writerow(columns_name)

    for client in clients_list:
        writer.writerow(client)
