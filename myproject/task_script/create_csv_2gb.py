import pandas as pd
import numpy as np
import os

def generate_large_csv(file_path, num_rows, chunk_size=100000):
    # Create a file handle to write the CSV
    with open(file_path, 'w') as f:
        # Write the header
        f.write('id,first_name,last_name,email,age\n')

        for start in range(0, num_rows, chunk_size):
            end = min(start + chunk_size, num_rows)
            chunk = pd.DataFrame({
                'id': np.arange(start, end),
                'first_name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], end - start),
                'last_name': np.random.choice(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown'], end - start),
                'email': np.random.choice(['example1@example.com', 'example2@example.com', 'example3@example.com'], end - start),
                'age': np.random.randint(18, 90, size=end - start)
            })

            chunk.to_csv(f, header=False, index=False)


if __name__ == "__main__":
    num_rows = 10000000 *3
    file_path = '/myproject/large_file.csv'
    generate_large_csv(file_path, num_rows)

    file_size = os.path.getsize(file_path) / (1024 * 1024 * 1024)
    print(f"Generated file size: {file_size:.2f} GB")
