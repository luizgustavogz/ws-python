# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# pip install pymysql
import os

import pymysql
import dotenv

dotenv.load_dotenv()

conn = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with conn:
    with conn.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL '
            ')'
        )
