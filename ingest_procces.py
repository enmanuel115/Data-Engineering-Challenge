import pandas as pd
import glob
import os
import shutil

# Import CSV
path = r'test:\trip\raw'
all_files = glob.glob(os.path.join(path , "/*.csv"))

li = []
#status of the data ingestion
print("Reading all the files on the directory")
for filename in all_files:
    df = pd.read_csv(filename, index_col=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

# Connect to SQL Server

#status of the data ingestion
print("Connecting to the db")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=trip_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Insert DataFrame to Table

#status of the data ingestion
print("Inserting into the table")
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO trips (region, priorigin_coord, destination_coord, datetime, datasource)
                VALUES (?,?,?,?,?)
                ''',
                row.region, 
                row.priorigin_coord,
                row.destination_coord,
                row.datetime,
                row.datasource
                )
conn.commit()

# Move all the processed files
source_dir = r'test:\trip\raw'
target_dir = r'test:\trip\processed'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)