# Problema dos parâmetros mutáveis em funções Python
# def add_clients(name, list=[]):  # Com o parâmetro mutável, a lista é criada uma única vez
# Com o parâmetro None, a lista é criada a cada chamada da função
def add_clients(name, list=None):
    if list is None:
        list = []
    list.append(name)
    return list


client1 = add_clients('Luiz')
add_clients('João', client1)
add_clients('Fernando', client1)
client1.append('Maria')

client2 = add_clients('Larissa')
add_clients('Maria', client2)

client3 = add_clients('Moreira')
add_clients('Vivi', client3)

print(client1)
print(client2)
print(client3)
