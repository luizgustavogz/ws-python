import os
"""
Criando arquivos com Python
Usamos a função open para abrir um arquivo em Python
    Modos:
r (leitura) / w (escrita) / x (para criação), a (escreve ao final) /
b (binário) / t (modo texto) / + (leitura e escrita)
Context manager - with (abre e fecha)
    Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
    Vamos falar mais sobre o módulo OS, mas:
os.remove ou unlink - apaga o arquivo
ps.rename - troca o nome ou move o arquivo
    Vamos falar mais sobre o módulo JSON, mas:
json.dump - gera um arquivo json
json.load - lê um arquivo json
"""
# path_file = 'C:\\Users\\Luiz\\OneDrive\\workspaces\\ws-python\\'
# path_file += 'Aula116.txt'
path_file = 'Aula116.txt'

# file = open(path_file, 'w')
# ...
# file.close()


# with open(path_file, 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     file.seek(0, 0)
#     print(file.read())

#     print('Lendo:')
#     file.seek(0, 0)
#     print(file.readline(), end='')
#     print(file.readline().strip())
#     print(file.readline().strip())

#     print('\nReadlines:')
#     file.seek(0, 0)
#     for linha in file.readlines():
#         print(linha.strip())


# print('#' * 10)

# with open(path_file, 'r') as file:
#     print(file.read())


# Bom exemplo para arquivos de log
# with open(path_file, 'a+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

with open(path_file, 'w', encoding='utf8') as file:
    file.write('Atenção\n')
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(path_file)    # ou os.unlink(path_file)
# os.rename(path_file, 'Aula116_renomeado.txt')
