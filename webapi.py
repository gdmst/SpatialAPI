from flask_restful import Resource, Api, reqparse
import pymssql
from flask import Flask, render_template, request, make_response
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from operationdb import OperationDB
app = Flask(__name__)
api = Api(app)

audio_put_arg = reqparse.RequestParser()
audio_put_arg.add_argument("url", type = str, help = "url of the audio")
#audio_put_arg.add_argument('audio', type=werkzeug.datastructures.FileStorage, location='files')
audio = {}

query = OperationDB('localhost', 'root', 'root', 'AirPollution')

class Connect_DB(Resource):
    def get(self):
        conn = pymssql.connect(server='localhost', user='root', password='root', database='AirPollution')
        cursor = conn.cursor(as_dict=True)

        cursor.execute('SELECT DISTINCT city FROM dbo.AirPollution')
        city = ""
        for row in cursor:
            city = (row['city'])
            #print("city=%s" % city)
        
        return {'city': city}

class View_City(Resource):
    def get(self):
        conn = pymssql.connect(
            server='localhost', user='root', password='root', database='AirPollution')
        cursor = conn.cursor(as_dict=True)

        cursor.execute('SELECT city, country FROM dbo.AirPollution')
        reponse = []
        for row in cursor:
            city = (row['city'])
            country = (row['country'])
            #print("city=%s" % city)
            row = {

                'city': city,
                'coutry': country
            }
            reponse.append(row)
        return reponse

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)


class Query2(Resource):
    def get(self):
        result = query.Query()
        return result

api.add_resource(Home, '/')
api.add_resource(Connect_DB, '/connect_db')
api.add_resource(View_City, '/viewCity')
api.add_resource(Query2, '/query2')
if __name__ == "__main__":
    app.run(debug=True)