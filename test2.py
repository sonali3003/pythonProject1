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

cursor= connection.cursor()

deactivate_query = """
    UPDATE customers
    SET status = 'Inactive'  
    WHERE status = 'Active';  
    """

cursor.execute(deactivate_query)

print("Customers deactivated successfully.")

connection.commit()
cursor.close()
connection.close()
