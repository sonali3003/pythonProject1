# Write a script in python that will connect to db & process bulk upload of customers data in Customers table


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

data = [
    #{"customer_id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "+1234567890"},
{"customer_id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "phone_number": "+9876543210"},
{"customer_id": 3, "first_name": "Robert", "last_name": "Johnson", "email": "robert.johnson@example.com", "phone_number": "+1122334455"},
{"customer_id": 4, "first_name": "Emily", "last_name": "Williams", "email": "emily.williams@example.com", "phone_number": "+9988776655"},
{"customer_id": 5, "first_name": "David", "last_name": "Brown", "email": "david.brown@example.com", "phone_number": "+1122337788"},
{"customer_id": 6, "first_name": "Sophia", "last_name": "Davis", "email": "sophia.davis@example.com", "phone_number": "+4455667788"},
{"customer_id": 7, "first_name": "Michael", "last_name": "Miller", "email": "michael.miller@example.com", "phone_number": "+1122339900"},
{"customer_id": 8, "first_name": "Emma", "last_name": "Wilson", "email": "emma.wilson@example.com", "phone_number": "+7766554433"},
{"customer_id": 9, "first_name": "Daniel", "last_name": "Moore", "email": "daniel.moore@example.com", "phone_number": "+1122331122"},
{"customer_id": 10, "first_name": "Olivia", "last_name": "Taylor", "email": "olivia.taylor@example.com", "phone_number": "+1122334455"},
{"customer_id": 11, "first_name": "Christopher", "last_name": "Anderson", "email": "christopher.anderson@example.com", "phone_number": "+1122336677"},
{"customer_id": 12, "first_name": "Ava", "last_name": "White", "email": "ava.white@example.com", "phone_number": "+1122338899"},
{"customer_id": 13, "first_name": "Matthew", "last_name": "Jones", "email": "matthew.jones@example.com", "phone_number": "+1122334455"},
{"customer_id": 14, "first_name": "Sofia", "last_name": "Brown", "email": "sofia.brown@example.com", "phone_number": "+1122336677"},
{"customer_id": 15, "first_name": "Andrew", "last_name": "Davis", "email": "andrew.davis@example.com", "phone_number": "+1122338899"},
{"customer_id": 16, "first_name": "Isabella", "last_name": "Clark", "email": "isabella.clark@example.com", "phone_number": "+1122334455"},
{"customer_id": 17, "first_name": "Joshua", "last_name": "Hill", "email": "joshua.hill@example.com", "phone_number": "+1122336677"},
{"customer_id": 18, "first_name": "Madison", "last_name": "Baker", "email": "madison.baker@example.com", "phone_number": "+1122338899"},
{"customer_id": 19, "first_name": "Ethan", "last_name": "Cooper", "email": "ethan.cooper@example.com", "phone_number": "+1122334455"},
{"customer_id": 20, "first_name": "Avery", "last_name": "Evans", "email": "avery.evans@example.com", "phone_number": "+1122336677"}
]
cursor=connection.cursor()
cursor
values = [(c['customer_id'], c['first_name'], c['last_name'], c['email'], c['phone_number']) for c in data]

update_query = """UPDATE Customers
            SET column_to_update = 'new_value'
            WHERE flag = 1;
        """
    cursor.execute(update_query)
    connection.commit()
    print("Update successful for rows with flag value 1.")

except psycopg2.Error as e:
    print(f"Error updating data: {e}")
    connection.rollback()  # Rollback changes if an error occurs


#Commit changes and close connections
connection.commit()
cursor.close()
connection.close()