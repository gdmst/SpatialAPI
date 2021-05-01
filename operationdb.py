import pymssql  

class OperationDB:
    temp_server = ""
    temp_user = ""
    temp_password = ""
    temp_database = ""
    
    def __init__(self,temp_server,temp_user,temp_password,temp_database):
        self.temp_server = temp_server
        self.temp_user = temp_user
        self.temp_password = temp_password
        self.temp_database = temp_database
        

    def Search_Data(self):
        conn = pymssql.connect(server=self.temp_server, user=self.temp_user, password=self.temp_password, database=self.temp_database) 
        cursor = conn.cursor(as_dict=True)
        sql = 'SELECT * FROM dbo.students'
        cursor.execute(sql)
        for row in cursor:
            print("id=%d, name=%s" % (row['id'], row['name']))
        conn.close()

    def Query(self):
        conn = pymssql.connect(server=self.temp_server, user=self.temp_user, password=self.temp_password, database=self.temp_database) 
        cursor = conn.cursor(as_dict=True)
        sql = 'SELECT * FROM dbo.AirPollution' 
        cursor.execute(sql)
        response = []
        for row in cursor:
            col_city = (row['city'])
            col_country = (row['country'])
            #print("city=%s" % city)
            row = {
                'city': col_city,
                'country': col_country
            }
            response.append(row)
        conn.close()
        return response

    def Search_Where_Data(self,temp_name):
        conn = pymssql.connect(server=self.temp_server, user=self.temp_user, password=self.temp_password, database=self.temp_database) 
        cursor = conn.cursor(as_dict=True)
        sql = 'SELECT * FROM dbo.AirPollution WHERE city=%s'
        name = temp_name 
        cursor.execute(sql, name)
        response = []
        for row in cursor:
            col_id = (row['id'])
            col_name = (row['name'])
            #print("city=%s" % city)
            row = {

                'id': col_id,
                'name': col_name
            }
            response.append(row)
        conn.close()
        return response

    def Insert_Data(self,temp_num,temp_name):
        conn = pymssql.connect(server=self.temp_server, user=self.temp_user, password=self.temp_password, database=self.temp_database) 
        cursor = conn.cursor(as_dict=True)
        sql = 'INSERT INTO dbo.students VALUES (%d,%s)'
        number = temp_num
        name = temp_name 
        cursor.execute(sql, (number,name))
        conn.commit()
        conn.close()

    def Delete_Data(self,temp_num):
        conn = pymssql.connect(server=self.temp_server, user=self.temp_user, password=self.temp_password, database=self.temp_database) 
        cursor = conn.cursor(as_dict=True)
        sql = 'DELETE FROM dbo.students WHERE id=%s'
        number = temp_num
        cursor.execute(sql, number)
        conn.commit()
        conn.close()

    def Update_Where_Data(self,temp_num,temp_name):
        conn = pymssql.connect(server=self.temp_server, user=self.temp_user, password=self.temp_password, database=self.temp_database) 
        cursor = conn.cursor(as_dict=True)
        sql = 'UPDATE dbo.students SET name=%s WHERE id = %s'
        number = temp_num
        name = temp_name
        cursor.execute(sql,(name,number))
        conn.commit()
        conn.close()