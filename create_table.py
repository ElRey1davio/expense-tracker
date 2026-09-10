import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
database_url = os.environ.get("DATABASE_URL")

connection = psycopg2.connect(database_url)
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE expense (
                   id SERIAL PRIMARY KEY,
                   description TEXT NOT NULL,
                   amount NUMERIC NOT NULL
               );
               """)

connection.commit()

cursor.close()
connection.close()

print("Table create successfully")

