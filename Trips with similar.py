import pyodbc 

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=test\SQLEXPRESS;'
                      'Database=trip_db;'
                      'Trusted_Connection=yes;')
                      
#Trips with similar origin, destination, and time of day should be grouped together
cursor = conn.cursor()
cursor.execute('SELECT region, origin_coord, destination_coord, datetime, datasource FROM trips group by origin_coord, destination_coord, datetime')

for i in cursor:
    print(i)
