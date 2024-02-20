import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_FILE_NAME

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# SQL

cursor.close()
conn.close()
