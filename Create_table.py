import pyodbc

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=test\SQLEXPRESS;'
                      'Database=trip_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE trips (
			trip_id int primary key IDENTITY(1,1),
			region nvarchar(50),
			priorigin_coord geography,
            destination_coord geography,
            datetime datetime,
            datasource nvarchar(50)
			)
               ''')