import sqlite3
from sqlite3.dbapi2 import connect
from flask_restful import Resource, reqparse
class User: 
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor =  connection.cursor()
        
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor =  connection.cursor()
        
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, type=str, help="Username is required")
        parser.add_argument('password', required=True, type=str, help="Password is required")
        
        data = parser.parse_args()

        existingUser = User.find_by_username(data['username']);
        print(existingUser)
        if existingUser is not None:
            return {'message': 'User already exists'}, 400

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "INSERT INTO users VALUES (null, ?,?)"
        cursor.execute(query, (data['username'], data['password']))

        conn.commit()
        conn.close()
        return {"message": "User created successfully"}, 201