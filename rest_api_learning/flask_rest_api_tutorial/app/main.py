from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Create a engine for connecting to SQLite3
engine = create_engine("sqlite:///salaries.db")

app = Flask(__name__)
api = Api(app)

class Department_Meta(Resource):
    def get(self):
        print("INSIDE Department_Meta")
        # Connect to Database
        connection = engine.connect()
        # Perform query and return JSON Data
        query = connection.execute("select distinct DEPARTMENT from salaries")
        return { "departments" : [i[0] for i in query.cursor.fetchall()] }

class Departmental_Salary(Resource):
    def get(self, department_name):
        connection = engine.connect()
        query = connection.execute("select * from salaries where Department='%s'"%department_name.upper())
        # Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = { "data": [dict(zip(tuple (query.keys()) , i)) for i in query.cursor] }
        # return "hola"
        return result
        # We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

api.add_resource(Departmental_Salary, "/departments/<string:department_name>")
api.add_resource(Department_Meta, "/departments")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
