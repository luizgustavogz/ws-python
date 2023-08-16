"""
Entendendo os seus próprios módulos Python
O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O python conhece a pasta onde o __main__ está e as pastas abaixo dele
Ele não reconhece pastas e módulos acima do __main__ por padrão
O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
"""

# try:
#     import sys
#     sys.path.append('c:/Users/Luiz/OneDrive/workspaces/ws-python')    
# except ModuleNotFoundError:
#     ...
# import modulo_python_teste

import Aula97_m

print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')
