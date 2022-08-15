import pyodbc 

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=test\SQLEXPRESS;'
                      'Database=trip_db;'
                      'Trusted_Connection=yes;')
                      
#Develop a way to obtain the weekly average number of trips for an area, defined by abounding box (given by coordinates) or by a region.
cursor = conn.cursor()
cursor.execute('SELECT AVG(trips) AS avg_trips, region FROM (SELECT count(1) as trips, region, DATEPART(wk , datetime) as week'
                'FROM trips group by region, DATEPART(wk , datetime))A GROUP BY region')

for i in cursor:
    print(i)
