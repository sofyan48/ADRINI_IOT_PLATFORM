from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.apikey_auth import apikey_required
from app.models import model as db
from app import db as dbq
import uuid

from flask import request


class SendModuls(Resource):
    @apikey_required
    def get(self, id_channels):
        args = request.args
        report = []
        data_widget = db.get_by_id("tb_widget", "id_channels",id_channels)
        for key in args :
            for i in data_widget:
                if i['nm_widget'] == key:
                    data_insert = {
                        "id_widget" : str(i['id_widget']),
                        "value_field" : args[key]
                    }
            message = []
            print(data_insert)
            try:
                result = db.insert(table="tb_moduls", data=data_insert)
            except Exception as e:
                message = {
                    "status": False,
                    "error": str(e)
                }
                report.append(message)
            else:
                message = {
                    "id" : result,
                    key : data_insert
                }
                report.append(message)
        return response(200, data=report)


class GetChannelsData(Resource):
    @apikey_required
    def get(self, id_channels):
        limit= request.args['count']
        if limit == "" or limit == "0":
            result_data= list()
            column = db.get_columns("v_moduls")
            try:
                result = list()
                query = """select * from v_moduls where id_channels="""+id_channels+""" order by created_at desc"""
                print(query)
                dbq.execute(query)
                rows = dbq.fetchall()
                for row in rows:
                    result.append(dict(zip(column, row)))
            except Exception as e:
                respons = {
                    "status": False,
                    "error": str(e)
                }
                return response(200, data=respons)
            else:
                for i in result :
                    data = {
                        "id_moduls": str(i['id_moduls']),
                        "id_channels" : str(i['id_channels']),
                        "id_widget" : str(i['id_widget']),
                        i['nm_widget'] : i['value_field'],
                        "created_at" : str(i['created_at']),
                    }
                    result_data.append(data)
                return response(200, data=result_data)
        else:
            result_data= list()
            column = db.get_columns("v_moduls")
            try:
                result = list()
                query = """select * from v_moduls where id_channels="""+id_channels+""" order by created_at desc limit """+limit
                print(query)
                dbq.execute(query)
                rows = dbq.fetchall()
                for row in rows:
                    result.append(dict(zip(column, row)))
            except Exception as e:
                respons = {
                    "status": False,
                    "error": str(e)
                }
                return response(200, data=respons)
            else:
                for i in result :
                    data = {
                        "id_moduls": str(i['id_moduls']),
                        "id_channels" : str(i['id_channels']),
                        "id_widget" : str(i['id_widget']),
                        i['nm_widget'] : i['value_field'],
                        "created_at" : str(i['created_at']),
                    }
                    result_data.append(data)
                return response(200, data=result_data)

class GetChannelDataByField(Resource):
    def get(self, id_channels,page):
        args = request.args
        
        field = None
        for i in args:
            if field is None:
                field = "nm_widget='"+args[i]+"'"
            else:
                field = field+" or nm_widget='"+args[i]+"'"
        result_data= list()
        
        column = db.get_columns("v_moduls")
        try:
            result = list()
            query = """select * from v_moduls where id_channels="""+id_channels+""" and """+field+""" order by created_at desc limit """+page
            dbq.execute(query)
            rows = dbq.fetchall()
            for row in rows:
                result.append(dict(zip(column, row)))
        except Exception as e:
            respons = {
                "status": False,
                "error": str(e)
            }
            return response(200, data=respons)
        else:
            arr_field = dict(args)
            for i in result :
                field = None
                for a in arr_field:
                    if arr_field[a][0] == i['nm_widget']:
                        field = arr_field[a][0]

                print(field)
                data = {
                    field : {
                        "id_moduls": str(i['id_moduls']),
                        "id_channels" : str(i['id_channels']),
                        "id_widget" : str(i['id_widget']),
                        i['nm_widget'] : i['value_field'],
                        "created_at" : str(i['created_at']),
                    }
                }
                result_data.append(data)
            return response(200, data=result_data)





