import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_FILE_NAME
TABLE_NAME = 'customers'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# CRUD - Create  Read    Update  Delete
# SQL -  INSERT  SELECT  UPDATE  DELETE

# CUIDADO: Delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
# Reseta o autoincremento
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
conn.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'age INTEGER,'
    'weight REAL'
    ')'
)
conn.commit()

# Insere dados
# CUIDADO: SQL Injection
# ? é um binding/placeholder para o valor que será passado
sql = f'INSERT INTO {TABLE_NAME} (name, age, weight) VALUES (:name, :age, :weight)'

# cursor.execute(sql, ['João', 25, 75.5])

# cursor.executemany(
#     sql,
#     (
#         ('João', 25, 75.5), ('Maria', 30, 60.5)
#     )
# )

cursor.execute(sql, {'name': 'Luiz', 'age': 22, 'weight': 95.5})
cursor.executemany(sql, (
    {'name': 'João', 'age': 25, 'weight': 75.5},
    {'name': 'Maria', 'age': 30, 'weight': 60.5},
    {'name': 'José', 'age': 35, 'weight': 80.3},
    {'name': 'Joana', 'age': 63, 'weight': 55.78},
))
conn.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id IN (1,3)')
    conn.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        _id, name, age, weight = row
        print(_id, name, age, weight)

    cursor.close()
    conn.close()
