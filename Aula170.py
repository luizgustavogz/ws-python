# os.listdir para navegar em caminhos
# C:\Users\Luiz\OneDrive\Imagens\Fotos
# path = r'C:\\Users\\Luiz\\OneDrive\\Imagens\\Fotos'
import os

path = os.path.join('C:\\', 'Users', 'Luiz', 'OneDrive', 'Imagens', 'Fotos')
print(path)

for folder in os.listdir(path):
    path_folder = os.path.join(path, folder)
    print(folder)

    if not os.path.isdir(path_folder):
        continue

    for item in os.listdir(path_folder):
        print('  ', item)
