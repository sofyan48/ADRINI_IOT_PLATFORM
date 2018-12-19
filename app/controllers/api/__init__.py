from flask import Blueprint
from flask_restful import Api
from .user import *
from .auth import *

from .test import *


api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)
api.add_resource(UserdataResource, '/user')
api.add_resource(UserdataResourceById, '/user/<userdata_id>')
api.add_resource(UserdataInsert, '/user')
api.add_resource(UserdataUpdate, '/user/<userdata_id>')
api.add_resource(UserdataRemove, '/user/<userdata_id>')

api.add_resource(Usersignin, '/sign')
api.add_resource(UserTokenRefresh, '/sign/token')
api.add_resource(UserloginInsert, '/user/add')

# POINT FITURED TRY
api.add_resource(TestPoint, '/point_test')

