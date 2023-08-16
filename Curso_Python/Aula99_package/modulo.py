__all__ = [
    'variavel',
    'soma_do_modulo',
    'nova_variavel',
]

# Importa o módulo_b.py para o módulo.py, assim, o módulo.py pode usar a função fala_oi() do módulo_b.py
from Aula99_package.modulo_b import fala_oi # from .modulo_b import fala_oi

# Apenas importa o módulo_b.py do diretório atual
# from modulo_b import fala_oi

variavel = 'variável do módulo'

def soma_do_modulo(x, y):
    return x + y

nova_variavel = 'nova variável do módulo'

# fala_oi()
