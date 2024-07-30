import pandas as pd
from sqlalchemy import create_engine

# Database configuration
db_config = {
    'user': 'root',
    'password': 'aspire',
    'host': 'localhost',
    'port': 3306,
    'database': 'mydatabase'
}

# Create a connection string
connection_string = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# Create an engine using SQLAlchemy
engine = create_engine(connection_string)

def insert_data_to_mysql(file_path):
    # Read the CSV file in chunks
    chunksize = 100000
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        # Insert data into MySQL
        chunk.to_sql(name='t_csv', con=engine, if_exists='append', index=False)
        print(f"Inserted chunk with {len(chunk)} rows")

if __name__ == "__main__":
    # Path to our large CSV file
    csv_file_path = '/myproject/large_file.csv'
    insert_data_to_mysql(csv_file_path)
