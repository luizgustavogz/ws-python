# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# pip install pymysql
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='db_python',
)

with conn:
    with conn.cursor() as cursor:
        # SQL
        print(cursor)
