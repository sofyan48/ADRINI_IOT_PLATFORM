from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
from app.models import model as db
from app.middlewares.auth import login_required


class BoardResource(Resource):
    @login_required
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