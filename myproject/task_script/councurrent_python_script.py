import pandas as pd
import mysql.connector
from concurrent.futures import ThreadPoolExecutor
from mysql.connector import Error

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'aspire',
    'password': 'aspire@123',
    'database': 'mydatabase',
    'port': 3306,
}

def insert_data(data_chunk):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO my_table (first_name, last_name) VALUES (%s, %s)"
        cursor.executemany(query, data_chunk)
        connection.commit()
        print(f"Inserted {len(data_chunk)} rows")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def process_csv(file_path):
    # Read the CSV file in chunks
    chunksize = 1000
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        # Convert chunk to a list of tuples
        data_chunk = chunk[['first_name', 'last_name']].values.tolist()
        print(f"Processing chunk with {len(data_chunk)} rows")
        # Use ThreadPoolExecutor to insert data concurrently
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.submit(insert_data, data_chunk)

if __name__ == "__main__":
    csv_file_path = '/home/shaukatali/Desktop/aspire/aspire_assignment/myproject/users.csv'
    process_csv(csv_file_path)
