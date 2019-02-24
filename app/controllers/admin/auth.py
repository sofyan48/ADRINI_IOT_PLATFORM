from flask_restful import Resource, reqparse, fields
from app.helpers.rest import response
from app.middlewares.auth import jwt_required
from flask_jwt_extended import (
                                JWTManager,
                                create_access_token,
                                get_jwt_identity,
                                jwt_refresh_token_required
                               )
import datetime
from app.models import model as db
from passlib.hash import pbkdf2_sha256


class UserloginInsert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userdata_id', type=str, required=True)
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        password_hash = pbkdf2_sha256.hash(args['password'])
        data_insert = {
            "id_userdata" : args['userdata_id'],
            "username" : args['username'],
            "password" : password_hash,
        }

        try:
            db.insert(table="tb_user", data=data_insert)
        except Exception as e:
            respon = {
                "status": False,
                "error": str(e)
            }
        else:
            data_insert = {
                "userdata_id" : args['userdata_id'],
                "username" : args['username'],
            }
            respon = {
                "status": True,
                "data": data_insert
            }
        return response(200, message=respon)

class UserTokenRefresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        ret = {'access_token': new_token}
        return response(200, data=ret)


class Usersignin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        args = parser.parse_args()

        username = args['username']
        password = args['password']

        user = db.get_by_id(
                    table= "tb_user", 
                    field="username",
                    value=username
                )

        expires = datetime.timedelta(hours=1)
        
        print(not user or not pbkdf2_sha256.verify(password, user[0]['password']) )
        
        if not user or not pbkdf2_sha256.verify(password, user[0]['password']):
            return response(status_code=401, message="Fuck You")
        else:
            if user[0]['access'] != 0:
                return response(status_code=401, message="Fuck You") 
            else:
                access_token = create_access_token(
                                                identity=user[0],
                                                expires_delta=expires
                                              )

                data = {
                    'username': user[0]['username'],
                    'apikey': "Bearer "+access_token,
                    'expires': str(expires)
                }
                return response(200, data=data)
