"""
Lista de listas e seus índices
"""

"""
salas = [
      # 0       # 1
    ['Maria', 'Helena', ], # 0
      # 0
    ['Elaine', ], # 1
      # 0     # 1       # 2
    ['Luiz', 'João', 'Larissa', (0, 10, 20, 30, 40)], # 2
]

print(salas)
print(salas[1][0]) # [lista][índice]
print(salas[0][1]) # [lista=0][índice=1] = Helena
print(salas[2][2]) # [lista=2][índice=2] = Larissa
print(salas[2][3][2]) # [lista=2][índice=3][índice da tupla=2] = 20
"""
salas = [['Maria', 'Helena', ], ['Elaine', ], ['Luiz', 'João', 'Larissa']]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
