import sqlite3

from main import DB_FILE, TABLE_NAME

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    #     _id = row[0]
    #     name = row[1]
    #     age = row[2]
    #     weight = row[3]
    _id, name, age, weight = row
    print(_id, name, age, weight)


cursor.close()
conn.close()
