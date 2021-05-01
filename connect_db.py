import pymssql
conn = pymssql.connect(server='localhost', user='root', password='root', database='AirPollution') 
cursor = conn.cursor(as_dict=True)

cursor.execute('SELECT DISTINCT city FROM dbo.AirPollution' )
for row in cursor:
  print("city=%s" % (row['city']))