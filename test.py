import psycopg2
from psycopg2 import extras
import sqlite3
import json

connection = psycopg2.connect(dbname='retailsalesdb',
                              user='postgres',
                              password='password',
                              host='127.0.0.1',
                              port='5432'
                              )
cursor=connection.cursor()

cursor.execute('SELECT * FROM products')

rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()

