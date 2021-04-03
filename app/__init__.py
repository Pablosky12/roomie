from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, id):
        return {'user': id}

api.add_resource(User, '/user/<string:name>')
