# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y): # Função interna que guarda o valor de x e recebe o valor de y
        return funcao(x, y)
    return interna  # Retorna a função interna sem executar ela


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_10 = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_10(10))
