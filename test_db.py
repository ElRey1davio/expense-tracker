import os
from dotenv import load_dotenv
import psycopg2



# This looks for a .env file and loads the variables into the system environment
load_dotenv()

# Now you can access it anywhere using os.environ
database_url = os.environ.get("DATABASE_URL")
print(len(database_url))
print(database_url.startswith("postgresql://"))


#reaches out over the internet to neon database,
# opens a live connection using the adress+password in your env file
connection = psycopg2.connect(database_url)

#sends a trivial sql command "give me number 1"
cursor = connection.cursor()
cursor.execute("SELECT 1;")

#after running a query, we call bacck for it with:
result = cursor.fetchone()
print("Test query result:", result)




#close db
cursor.close()
connection.close()

