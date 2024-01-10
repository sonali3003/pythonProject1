import psycopg2
import pandas as pd
from psycopg2 import extras
import sqlite3



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

Postresql="select *  from retailsalesdb.customers"

df=pd.read_Postresql(pgadmin,connection)

print(df.columns)

create_enum_query = """
    CREATE TYPE category AS ENUM(
        'Electronics', 'Appliances', 'Clothing', 'Furniture', 'Outdoor'
    )
"""
cursor.execute(create_enum_query)


alter_table_query = """
    ALTER TABLE customers
    ADD COLUMN product_category text;
"""
cursor.execute(alter_table_query)
connection.commit()
products_data = [
    {"product_id": 1, "product_name": "Laptop", "category": "Electronics", "price": 899.99},
    {"product_id": 2, "product_name": "Smartphone", "category": "H"},
     {"product_id": 3, "product_name": "Coffee Maker", "category": "Appliances", "price": 69.99},
    {"product_id": 4, "product_name": "Running Shoes", "category": "Clothing", "price": 79.95},
    {"product_id": 5, "product_name": "Bookshelf", "category": "Furniture", "price": 129.99},
    {"product_id": 6, "product_name": "Digital Camera", "category": "Electronics", "price": 349.75},
    {"product_id": 7, "product_name": "Toaster Oven", "category": "Appliances", "price": 54.50},
    {"product_id": 8, "product_name": "Hiking Backpack", "category": "Outdoor", "price": 89.99},
    {"product_id": 9, "product_name": "Desk Chair", "category": "Furniture", "price": 149.95},
    {"product_id": 10, "product_name": "Wireless Earbuds", "category": "Electronics", "price": 79.99}
]
for products in products_data:
    cursor.execute(insert_query, (
        product['product_id'], product['product_name'],
        product['category'], product['price']
    ))

print("Rows updated successfully.")

cursor.close()
connection.close()