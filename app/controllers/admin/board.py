from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.models import model as db
from app.middlewares.auth import admin_required


class BoardResource(Resource):
    @admin_required
    def get(self):
        obj_userdata = list()
        try:
            results = db.get_all("tb_board")
        except Exception:
            return response(200, message="Data Not Found")
        else:
            for i in results :
                data = {
                    "id_board": str(i['id_board']),
                    "serial" : i['serial_board'],
                    "nm_board" : i['nm_board']
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)


class BoardResourceById(Resource):
    @admin_required
    def get(self, id_board):
        obj_userdata = []
        results = db.get_by_id(
                    table="tb_board",
                    field="id_board",
                    value=id_board
                )

        for i in results :
            data = {
                    "id_board": str(i['id_board']),
                    "serial" : i['serial_board'],
                    "nm_board" : i['nm_board']
            }
            obj_userdata.append(data)
        return response(200, data=obj_userdata)


class BoardInsert(Resource):
    @admin_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nm_board', type=str, required=True)
        parser.add_argument('serial_board', type=str, required=True)
        args = parser.parse_args()

        data_insert = {
            "nm_board" : args['nm_board'],
            "serial_board" : args['serial_board']
        }
        try:
            result = db.insert(table="tb_board", data=data_insert)
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


class BoardRemove(Resource):
    @admin_required
    def delete(self, id_board):
        try:
            db.delete(
                    table="tb_board", 
                    field='id_board',
                    value=id_board
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


class BoardUpdate(Resource):
    @admin_required
    def put(self, id_board):
        parser = reqparse.RequestParser()
        parser.add_argument('nm_board', type=str, required=True)
        parser.add_argument('serial_board', type=str, required=True)
        args = parser.parse_args()

        data = {
            "where":{
                "id_board": id_board
            },
            "data":{
                "nm_board" : args['nm_board'],
                "serial_board" : args['serial_board']
            }
        }
        try:
            db.update("tb_board", data=data)
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

