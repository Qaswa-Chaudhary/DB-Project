import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# creating database connection 

def connect_db():
    try:
        conn= mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database  = os.getenv('DB_NAME')
        )
        cursor = conn.cursor()
        print('Connected Successfully')
        return conn ,cursor
    except mysql.connector.Error as err:
        print(f'Error:{err}')

connect_db()