from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.auth import jwt_required
from app.models import model as db
import uuid


class ModulsResource(Resource):
    @jwt_required
    def get(self):
        obj_userdata = list()
        
        try:
            results = db.get_all("tb_moduls")
        except Exception:
            return response(200, message="Data Not Found")
        else:
            for i in results :
                data = {
                    "id_moduls": str(i['id_moduls']),
                    "id_widget" : str(i['id_widget']),
                    "nm_field" : i['nm_field'],
                    "value_field" : i['value_field'],
                    "created_at" : str(i['created_at']),
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)


class ModulsResourceById(Resource):
    @jwt_required
    def get(self, id_moduls):
        obj_userdata = []
        results = db.get_by_id(
                    table="tb_moduls",
                    field="id_moduls",
                    value=id_moduls
                )

        for i in results :
            data = {
                "id_moduls": str(i['id_moduls']),
                "id_widget" : str(i['id_widget']),
                "nm_field" : i['nm_field'],
                "value_field" : i['value_field'],
                "created_at" : str(i['created_at']),
            }
            obj_userdata.append(data)
        return response(200, data=obj_userdata)


class ModulsInsert(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_widget', type=str, required=True)
        parser.add_argument('nm_field', type=str, required=True)
        parser.add_argument('value_field', type=str, required=True)
        args = parser.parse_args()


        data_insert = {
            "id_widget" : args['id_widget'],
            "nm_field" : args['nm_field'],
            "value_field" : args['value_field']
        }
        try:
            result = db.insert(table="tb_moduls", data=data_insert)
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


class ModulsRemove(Resource):
    @jwt_required
    def delete(self, id_moduls):
        try:
            db.delete(
                    table="tb_moduls", 
                    field='id_moduls',
                    value=id_moduls
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


class ModulsUpdate(Resource):
    @jwt_required
    def put(self, id_moduls):
        parser = reqparse.RequestParser()
        parser.add_argument('id_widget', type=str, required=True)
        parser.add_argument('nm_field', type=str, required=True)
        parser.add_argument('value_field', type=str, required=True)
        args = parser.parse_args()

        data = {
            "where":{
                "id_moduls": id_moduls
            },
            "data":{
                "id_widget" : args['id_widget'],
                "nm_field" : args['nm_field'],
                "value_field" : args['value_field']
            }
        }
        try:
            db.update("tb_moduls", data=data)
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

