# Try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('Abrir arquivo.\n')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)    
except IndexError as errpr:
    print('IndexError')
except (NameError, ImportError):
    print('NameError ou ImportError')
else:
    print('Não houve exceção.')
finally:
    print('\nFechar arquivo.')
