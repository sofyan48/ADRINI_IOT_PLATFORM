from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.models import model as db
from app.middlewares.auth import admin_required
import uuid


class ChannelsResource(Resource):
    @admin_required
    def get(self):
        obj_userdata = list()
        try:
            results = db.get_all("tb_channels")
        except Exception:
            return response(200, message="Data Not Found")
        else:
            for i in results :
                data = {
                    "id_channels": str(i['id_channels']),
                    "id_userboard" : str(i['id_userboard']),
                    "nm_channels" : i['nm_channels'],
                    "channels_key" : i['channels_key']
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)


class ChannelsResourceById(Resource):
    @admin_required
    def get(self, id_channels):
        obj_userdata = []
        results = db.get_by_id(
                    table="tb_channels",
                    field="id_channels",
                    value=id_channels
                )

        for i in results :
            data = {
                "id_channels": str(i['id_channels']),
                "id_userboard" : str(i['id_userboard']),
                "nm_channels" : i['nm_channels'],
                "channels_key" : i['channels_key']
            }
            obj_userdata.append(data)
        return response(200, data=obj_userdata)


class ChannelsInsert(Resource):
    @admin_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nm_channels', type=str, required=True)
        parser.add_argument('id_userboard', type=str, required=True)
        args = parser.parse_args()

        random_string = uuid.uuid4()
        raw_token = '{}{}'.format(random_string, args['id_userboard'])

        data_insert = {
            "nm_channels" : args['nm_channels'],
            "id_userboard" : args['id_userboard'],
            "channels_key" : raw_token,
        }
        try:
            result = db.insert(table="tb_channels", data=data_insert)
        except Exception as e:
            message = {
                "status": False,
                "error": str(e)
            }
            return response(200, message=message)
        else:
            respon = {
                "data": data_insert,
                "id" : result,
                "apikey": raw_token
            }
            return response(200, data=respon)


class ChannelsRemove(Resource):
    @admin_required
    def delete(self, id_channels):
        try:
            db.delete(
                    table="tb_channels", 
                    field='id_channels',
                    value=id_channels
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


class ChannelsUpdate(Resource):
    @admin_required
    def put(self, id_channels):
        parser = reqparse.RequestParser()
        parser.add_argument('nm_channels', type=str, required=True)
        parser.add_argument('id_userboard', type=str, required=True)
        args = parser.parse_args()

        data = {
            "where":{
                "id_channels": id_channels
            },
            "data":{
                "id_userboard" : args['id_userboard'],
                "nm_channels" : args['nm_channels']
            }
        }
        try:
            db.update("tb_channels", data=data)
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

