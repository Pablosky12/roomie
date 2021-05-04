from flask import Flask, request
from flask_jwt import JWT
from flask_restful import Resource, Api 

from house import House
from user import UserRegister
from auth import authenticate, identity


app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)

jwt =  JWT(app, authenticate, identity)


# class User(Resource):
#     def get(self, name):
#         item = next(filter(lambda x: x["username"] == name, users), None)

#         return {"item": item}, 200 if item is not None else 404

#     def post(self, name):
#         if next(filter(lambda x: x["username"] == name, users), None) is not None:
#             return {
#                 "message": f"A user with that name ({name}) already exists"
#             }, 400
        
#         data = request.get_json()
#         user = {
#             "username": data["username"],
#             "salary": data["salary"],
#             "password": data["password"],
#         }
#         users.append(user)
#         return user, 201
#     def delete(self, name):
#         global users
#         users = list(filter(lambda x: x['name'] != name, users))
#         return {'message': 'user deleted'}



# class UserList(Resource):
#     def get(self):
#         return users


# api.add_resource(User, "/user/<string:name>")
api.add_resource(UserRegister, "/register")
api.add_resource(House, "/house/<string:name>")
# api.add_resource(UserList, "/users")

app.run(port=5000, debug=True)