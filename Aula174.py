# os + shutil - Apagando e copiando pastas com Python
# Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
OLD_FOLDER = os.path.join('C:\\', 'Users', 'Luiz',
                          'OneDrive', 'Imagens', 'Fotos')
NEW_FOLDER = os.path.join(DESKTOP, 'Fotos')

shutil.rmtree(NEW_FOLDER, ignore_errors=True)
shutil.copytree(OLD_FOLDER, NEW_FOLDER)
shutil.move(NEW_FOLDER, os.path.join(DESKTOP, 'Fotos2'))

# os.makedirs(NEW_FOLDER, exist_ok=True)

# for root, dirs, files in os.walk(OLD_FOLDER):
#     for dir_ in dirs:
#         new_directory_path = os.path.join(
#             root.replace(OLD_FOLDER, NEW_FOLDER), dir_
#         )
#         os.makedirs(new_directory_path, exist_ok=True)

#     for file in files:
#         old_file_path = os.path.join(root, file)
#         new_file_path = os.path.join(
#             root.replace(OLD_FOLDER, NEW_FOLDER), file
#         )
#         shutil.copy(old_file_path, new_file_path)
