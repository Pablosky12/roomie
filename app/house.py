import sqlite3
from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


class House: 
    def __init__(self, _id, name, users) -> None:
        self.id = _id
        self.name = name
        self.users = users

class House(Resource):

    getParser = reqparse.RequestParser()
    getParser.add_argument("name", required=True, type=str, help="Name is required")
    # @jwt_required()
    def get(self, name):
        data = House.getParser.parse_args()
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM houses h WHERE h.name = ?"

        result = cursor.execute(query, (data["name"],));
        house = result.fetchone()
        
        conn.close()

        if house:
            return {'house': {'id': house[0], 'name': house[1]}}
        else:
            return {'message': "house not found"}, 404
        

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


