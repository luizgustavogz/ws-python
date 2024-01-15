# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

path = os.path.join('C:\\', 'Users', 'Luiz', 'OneDrive', 'Imagens', 'Fotos')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        path_folder = os.path.join(root, file_)
        print('  ', the_counter, 'File:', path_folder)
        # os.unlink(path_folder) # deleta os arquivos
