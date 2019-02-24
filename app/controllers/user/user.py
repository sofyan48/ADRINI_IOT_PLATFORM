from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.auth import jwt_required, get_jwt_identity
from app.models import model as db
from app import db as dbq


class UserdataResource(Resource):
    @jwt_required
    def get(self):
        id_userdata = str(get_jwt_identity())
        obj_userdata = list()
        column = db.get_columns('tb_userdata')
        try:
            results = list()
            query = "select * from tb_userdata where id_userdata='"+id_userdata+"'"
            dbq.execute(query)
            rows = dbq.fetchall()
            for row in rows:
                print(row)
                results.append(dict(zip(column, row)))
        except Exception as e:
            return response(200, message=str(e))
        else:
            for i in results :
                data = {
                    "id_userdata": str(i['id_userdata']),
                    "email" : i['email'],
                    "first_name" : i['first_name'],
                    "last_name" : i['last_name'],
                    "location" : i['location']
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)

class UserdataRemove(Resource):
    @jwt_required
    def delete(self, userdata_id):
        try:
            db.delete(
                    table="tb_userdata", 
                    field='id_userdata',
                    value=userdata_id
                )
        except Exception as e:
            message = {
                "status": False,
                "error": str(e)
            }
        else:
            message = "removing"

        finally:
            return response(200, message=message)


class UserdataUpdate(Resource):
    @jwt_required
    def put(self, userdata_id):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('location', type=str, required=True)
        args = parser.parse_args()

        data = {
            "where":{
                "userdata_id": userdata_id
            },
            "data":{
                "email" : args['email'],
                "first_name" : args['first_name'],
                "last_name" : args['last_name'],
                "location" : args['location']
            }
        }

        
        try:
            db.update("tb_userdata", data=data)
        except Exception as e:
            message = {
                "status": False,
                "error": str(e)
            }
        else:
            message = {
                "status": True,
                "data": data
            }
        finally:
            return response(200, message=message)

