import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='aspire',
        database='mydatabase'  # Replace with your actual database name
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database:", record)

        # Query the existing table
        cursor.execute("SELECT * FROM my_table;")  # Replace with your actual table name
        rows = cursor.fetchall()

        print("Data in your_table_name:")
        for row in rows:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
