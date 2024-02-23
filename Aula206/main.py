# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# pip install pymysql
import os

import pymysql
import dotenv

dotenv.load_dotenv()

TABLE_NAME = os.environ['MYSQL_TABLE']

conn = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with conn:
    with conn.cursor() as cursor:
        # CREATE TABLE: Criando a tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL '
            ')'
        )
        # TRUNCATE TABLE: Limpa a tabela por completo
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    conn.commit()

    with conn.cursor() as cursor:
        # INSERT INTO: Adicionando dados na tabela
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) '
            'VALUES (%s, %s)'  # %s é um placeholder
        )
        data = ('Luiz', 21)
        cursor.execute(sql, data)
    conn.commit()
