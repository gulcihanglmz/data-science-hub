import pandas as pd
import sqlite3

df = pd.read_csv(r"D:\3.sınıf\Advance computer programming\dataset\cleaned_dataset.csv")

# Connect to the SQLite database
conn = sqlite3.connect('network_activity_data.db')

# Insert the first 10 rows into the database
df.to_sql('network_activity_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

