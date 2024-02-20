import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_FILE_NAME
TABLE_NAME = 'customers'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

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

cursor.close()
conn.close()
