import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_FILE_NAME
TABLE_NAME = 'customers'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# CUIDADO: Delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
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
sql = f'INSERT INTO {TABLE_NAME} (name, age, weight) VALUES (?, ?, ?)'
# cursor.execute(sql, ['João', 25, 75.5])
cursor.executemany(
    sql,
    (
        ('João', 25, 75.5), ('Maria', 30, 60.5)
    )
)
conn.commit()
print(sql)

cursor.close()
conn.close()
