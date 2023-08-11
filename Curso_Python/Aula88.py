# Valores Trythy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis []  {}  set()
# Imutáveis ()  ""  0   0.0   None   False   range()
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
int = 0
float = 0.0
none = None
boolean = False
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{int=}', falsy(int))
print(f'{float=}', falsy(float))
print(f'{none=}', falsy(none))
print(f'{boolean=}', falsy(boolean))
print(f'{intervalo=}', falsy(intervalo))