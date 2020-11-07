from Model.Users import UserModal
import sqlite3
from flask_restful import Resource, reqparse


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str, required=True, help="this feild can't be left blank!"
    )
    parser.add_argument(
        'password',
        type=str, required=True, help="this feild can't be left blank!"
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        user = UserModal(data['username'],data['password'])

        user.save_to_db()

        return{"message": "user created successfully"}, 201
