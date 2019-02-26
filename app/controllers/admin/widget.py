from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.models import model as db
from app.middlewares.auth import admin_required


class WidgetResource(Resource):
    @admin_required
    def get(self):
        obj_userdata = list()
        try:
            results = db.get_all("tb_widget")
        except Exception:
            return response(200, message="Data Not Found")
        else:
            for i in results :
                data = {
                    "id_widget": str(i['id_widget']),
                    "nm_widget" : i['nm_widget'],
                    "id_channels": str(i['id_channels'])
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)


class WidgetResourceById(Resource):
    @admin_required
    def get(self, id_widget):
        obj_userdata = []
        results = db.get_by_id(
                    table="tb_widget",
                    field="id_widget",
                    value=id_widget
                )

        for i in results :
            data = {
                    "id_widget": str(i['id_widget']),
                    "nm_widget" : i['nm_widget'],
                    "id_channels": str(i['id_channels'])
                }
            obj_userdata.append(data)
        return response(200, data=obj_userdata)


class WidgetInsert(Resource):
    @admin_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nm_widget', type=str, required=True)
        parser.add_argument('id_channels', type=str, required=True)
        args = parser.parse_args()

        data_insert = {
            "nm_widget" : args['nm_widget'],
            "id_channels" : args['id_channels'],
        }
        try:
            result = db.insert(table="tb_widget", data=data_insert)
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


class WidgetRemove(Resource):
    @admin_required
    def delete(self, id_widget):
        try:
            db.delete(
                    table="tb_widget", 
                    field='id_board',
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


class WidgetUpdate(Resource):
    @admin_required
    def put(self, id_widget):
        parser = reqparse.RequestParser()
        parser.add_argument('nm_widget', type=str, required=True)
        args = parser.parse_args()

        data = {
            "where":{
                "id_widget": id_widget
            },
            "data":{
                "nm_widget" : args['nm_widget'],
                "id_channels" : args['id_channels'],
            }
        }
        try:
            db.update("tb_widget", data=data)
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

