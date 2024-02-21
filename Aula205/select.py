import sqlite3

from main import DB_FILE, TABLE_NAME

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
print('Select all:')
for row in cursor.fetchall():
    _id, name, age, weight = row
    print(_id, name, age, weight)

print('---')

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = 3')
print('Select one:')
row = cursor.fetchone()
_id, name, age, weight = row
print(_id, name, age, weight)


cursor.close()
conn.close()
