from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.auth import jwt_required
from app.models import model as db
from app import db as dbq
import uuid

from flask import request


class SendModuls(Resource):
    def get(self, id_channels):
        args = request.args
        report = []
        results = db.get_by_id(
                    table="tb_moduls",
                    field="id_channels",
                    value=id_channels
                )
        for row in results :
            for key in args:
                message = []
                if row['nm_field'] == key:
                    data_insert = {
                        "id_channels" : id_channels,
                        "nm_field" : key,
                        "value_field" : args[key]
                    }
                    # print(data_insert)
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
                            "data": data_insert,
                            "id" : result
                        }
                        report.append(message)

                    # # kalo edit
                    # data = {
                    #     "where":{
                    #         "id_moduls": str(row['id_moduls'])
                    #     },
                    #     "data":{
                    #         "value_field" : args[key]
                    #     }
                    # }
                    # try:
                    #     db.update("tb_moduls", data=data)
                    # except Exception as e:
                    #     message = {
                    #         "status": False,
                    #         "error": str(e)
                    #     }
                    #     report.append(message)
                    # else:
                    #     message = {
                    #         "status": True,
                    #         "data": data
                    #     }
                    #     report.append(message)
        
        return response(200, data=report)

class GetChannelsData(Resource):
    def get(self, id_channels):
        obj_moduls = []
        limit= request.args['page']
        print(limit)
        if limit == "" or limit == "0":
            results = db.get_by_id(
                        table="tb_moduls",
                        field="id_channels",
                        value=id_channels
                    )

            for i in results :
                data = {
                    "id_moduls": str(i['id_moduls']),
                    "id_channels" : str(i['id_channels']),
                    i['nm_field'] : i['value_field'],
                    "created_at" : str(i['created_at']),
                }
                obj_moduls.append(data)
            return response(200, data=obj_moduls)
        else:
            result_data= list()
            column = db.get_columns("tb_moduls")
            limit= request.args['page']
            print(limit)
            try:
                result = list()
                query = """select * from tb_moduls where id_channels="""+id_channels+""" order by created_at desc limit """+limit
                print(query)
                dbq.execute(query)
                rows = dbq.fetchall()
                for row in rows:
                    result.append(dict(zip(column, row)))
            except Exception as e:
                respons = {
                    "status": False,
                    "messages": str(e)
                }
            else:
                for i in result :
                    data = {
                        "id_moduls": str(i['id_moduls']),
                        "id_channels" : str(i['id_channels']),
                        i['nm_field'] : i['value_field'],
                        "created_at" : str(i['created_at']),
                    }
                    result_data.append(data)
                respons = {
                    "status": True,
                    "messages": "Fine!"
                }
            finally:
                return response(200, data=result_data)





