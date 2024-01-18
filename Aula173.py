# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
OLD_FOLDER = os.path.join('C:\\', 'Users', 'Luiz',
                          'OneDrive', 'Imagens', 'Fotos')
NEW_FOLDER = os.path.join(DESKTOP, 'Fotos')

os.makedirs(NEW_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(OLD_FOLDER):
    for dir_ in dirs:
        new_directory_path = os.path.join(
            root.replace(OLD_FOLDER, NEW_FOLDER), dir_
        )
        os.makedirs(new_directory_path, exist_ok=True)

    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(
            root.replace(OLD_FOLDER, NEW_FOLDER), file
        )
        shutil.copy(old_file_path, new_file_path)
        # print(f'Arquivo {file} copiado com sucesso!')
