from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.auth import jwt_required
from app.models import model as db


class UserBoardResource(Resource):
    @jwt_required
    def get(self):
        obj_userdata = list()
        
        try:
            results = db.get_all("tb_userboard")
        except Exception:
            return response(200, message="Data Not Found")
        else:
            for i in results :
                data = {
                    "id_userboard": str(i['id_userboard']),
                    "id_userdata" : str(i['id_userdata']),
                    "id_board" : str(i['id_board'])
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)


class UserBoardResourceById(Resource):
    @jwt_required
    def get(self, id_userboard):
        obj_userdata = []
        results = db.get_by_id(
                    table="tb_userboard",
                    field="id_board",
                    value=id_userboard
                )

        for i in results :
            data = {
                "id_userboard": str(i['id_userboard']),
                "id_userdata" : str(i['id_userdata']),
                "id_board" : str(i['id_board'])
            }
            obj_userdata.append(data)
        return response(200, data=obj_userdata)


class UserBoardInsert(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_board', type=str, required=True)
        parser.add_argument('id_userdata', type=str, required=True)
        args = parser.parse_args()

        data_insert = {
            "id_board" : args['id_board'],
            "id_userdata" : args['id_userdata']
        }
        try:
            result = db.insert(table="tb_userboard", data=data_insert)
        except Exception as e:
            message = {
                "status": False,
                "error": str(e)
            }
            return response(200, message=message)
        else:
            respon = {
                "data": data_insert,
                "id" : result
            }
            return response(200, data=respon)


class UserBoardRemove(Resource):
    @jwt_required
    def delete(self, id_widget):
        try:
            db.delete(
                    table="tb_userboard", 
                    field='id_userboard',
                    value=id_widget
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


class UserBoardUpdate(Resource):
    @jwt_required
    def put(self, id_userboard):
        parser = reqparse.RequestParser()
        parser.add_argument('id_board', type=str, required=True)
        parser.add_argument('id_userdata', type=str, required=True)
        args = parser.parse_args()

        data = {
            "where":{
                "id_userboard": id_userboard
            },
            "data":{
                "id_board" : args['id_board'],
                "id_userdata" : args['id_userdata']
            }
        }
        try:
            db.update("tb_userboard", data=data)
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

