from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from auth import authenticate, identity

app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)

jwt =  JWT(app, authenticate, identity)

users = []
houses = [
    {
        'id': 0,
        'name': 'stiv'
    }
]



class User(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["username"] == name, users), None)

        return {"item": item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x["username"] == name, users), None) is not None:
            return {
                "message": f"A user with that name ({name}) already exists"
            }, 400
        
        data = request.get_json()
        user = {
            "username": data["username"],
            "salary": data["salary"],
            "password": data["password"],
        }
        users.append(user)
        return user, 201
    def delete(self, name):
        global users
        users = list(filter(lambda x: x['name'] != name, users))
        return {'message': 'user deleted'}

class House(Resource):
    def get(self, name):
        house = next(filter(lambda x: x["name"] == name, houses), None)

        return {"house": house}, 200 if house is not None else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, houses), None) is not None:
            return {
                "message": f"A house with that name ({name}) already exists"
            }, 400
        
        data = request.get_json()
        house = {
            "name": data["name"],
        }
        houses.append(house)
        return house, 201
    def put(self, name):
        parser =  reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="The name cannot be blank")

        house = next(filter(lambda x: x['name'] == name, houses), None)
        data = parser.parse_args()
        if house is  None:
            house = { 
                'name': data['name']
            }
            houses.append(house)
        else:
            house.update(data)
        return house
    def delete(self, name) :
        global houses
        houses = filter(lambda x: x['name'] != name, houses)
        return {'message': 'success'}




class UserList(Resource):
    def get(self):
        return users


api.add_resource(User, "/user/<string:name>")
api.add_resource(House, "/house/<string:name>")
api.add_resource(UserList, "/users")

app.run(port=5000, debug=True)