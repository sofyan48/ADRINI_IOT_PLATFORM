from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.auth import jwt_required, get_jwt_identity
from app.models import model as db
from app import db as dbq


class UserBoardResource(Resource):
    @jwt_required
    def get(self):
        obj_userdata = list()
        id_userdata = str(get_jwt_identity())
        column = db.get_columns('v_userboard')
        try:
            results = list()
            query = "select * from v_userboard where id_userdata='"+id_userdata+"'"
            dbq.execute(query)
            rows = dbq.fetchall()
            for row in rows:
                print(row)
                results.append(dict(zip(column, row)))
        except Exception as e:
            return response(401, message=str(e))
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
        id_userdata = str(get_jwt_identity())
        column = db.get_columns('v_userboard')
        try:
            results = list()
            query = "select * from v_userboard where id_userdata='"+id_userdata+"' and id_userboard='"+id_userboard+"'"
            dbq.execute(query)
            rows = dbq.fetchall()
            for row in rows:
                print(row)
                results.append(dict(zip(column, row)))
        except Exception as e:
            return response(401, message=str(e))
        else:
            for i in results :
                data = {
                    "id_userboard": str(i['id_userboard']),
                    "id_userdata" : str(i['id_userdata']),
                    "id_board" : str(i['id_board'])
                }
                obj_userdata.append(data)
            return response(200, data=obj_userdata)
