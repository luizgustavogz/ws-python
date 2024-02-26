# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# pip install pymysql
import os

import dotenv
import pymysql
import pymysql.cursors

dotenv.load_dotenv()

TABLE_NAME = os.environ['MYSQL_TABLE']

conn = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
    # cursorclass=pymysql.cursors.SSDictCursor,
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

    # Inserindo um valor usando placeholder e um iterável
    with conn.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) '
            'VALUES (%s, %s)'  # %s é um placeholder
        )
        data = ('Luiz', 21)
        cursor.execute(sql, data)
    conn.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with conn.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) '
            'VALUES (%(nome)s, %(idade)s)'
        )
        data = {
            "nome": "Gustavo",
            "idade": 27,
        }
        cursor.execute(sql, data)
    conn.commit()

    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with conn.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) '
            'VALUES (%(nome)s, %(idade)s)'
        )
        # Iterando sobre um dicionário
        data = (
            {"nome": "Larissa", "idade": 24, },
            {"nome": "Rogerio", "idade": 54, },
            {"nome": "Rose", "idade": 77, },
        )
        cursor.executemany(sql, data)
    conn.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with conn.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, age) '
            'VALUES (%s, %s)'
        )
        # Tupla de tuplas
        data = (
            ("Gemini", 102, ),
            ("Cortana", 3, ),
            ("Luiz", 21, ),
        )
        cursor.executemany(sql, data)
    conn.commit()

    """
    # Lendo os dados da tabela com SELECT
    with conn.cursor() as cursor:
        min_id = int(input("Digite o valor mínimo para o id: "))
        max_id = int(input("Digite o valor máximo para o id: "))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )

        cursor.execute(sql, (min_id, max_id))
        print(cursor.mogrify(sql, (min_id, max_id)))
        result = cursor.fetchall()

        for row in result:
            print(row)
    """

    # Apagando com DELETE, WHERE e placeholders
    with conn.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '
        )
        cursor.execute(sql, (1,))
        conn.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)

    # Editando com UPDATE, WHERE e placeholders
    with conn.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name = %s, age = %s '
            'WHERE id = %s '
        )
        cursor.execute(sql, ('Eleonor', 92, 5))
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)

        # for row in cursor.fetchall():
        #     print(row)

        # print("\nCursor Scroll")
        # cursor.scroll(0, mode='absolute')
        # for row in cursor.fetchall():
        #     print(row)

        # for row in cursor.fetchall_unbuffered():
        #     print(row)

        #     if row['id'] >= 3:
        #         break

        # print('\nFor 2: ')
        # # cursor.scroll(-1)
        # for row in cursor.fetchall_unbuffered():
        #     print(row)

        data = cursor.fetchall()

        for row in data:
            print(row)

        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()

        print('resultFromSelect:', resultFromSelect)
        print('len(data):', len(data))
        print('rowcount:', cursor.rowcount)
        print('lastrowid:', cursor.lastrowid)
        print('lastrowid na mão:', lastIdFromSelect)
        print('rownumber:', cursor.rownumber)

    conn.commit()
