from flask import Blueprint
from flask_restful import Api
from .user import *
from .auth import *
from .test import *
from .board import *
from .channels import *
from .moduls import *
from .widget import *
from .userBoard import *


admin_blueprint = Blueprint("admin", __name__, url_prefix='/admin')
api = Api(admin_blueprint)

# User
api.add_resource(UserdataResource, '/user')
api.add_resource(UserdataResourceById, '/user/<userdata_id>')
api.add_resource(UserdataInsert, '/user')
api.add_resource(UserdataUpdate, '/user/<userdata_id>')
api.add_resource(UserdataRemove, '/user/<userdata_id>')

api.add_resource(Usersignin, '/sign')
api.add_resource(UserTokenRefresh, '/sign/token')
api.add_resource(UserloginInsert, '/user/add')

# Board
api.add_resource(BoardResource, '/board')
api.add_resource(BoardResourceById, '/board/<id_board>')
api.add_resource(BoardInsert, '/board')
api.add_resource(BoardUpdate, '/board/<id_board>')
api.add_resource(BoardRemove, '/board/<id_board>')

# User Board
api.add_resource(UserBoardResource, '/userboard')
api.add_resource(UserBoardResourceById, '/userboard/<id_userboard>')
api.add_resource(UserBoardInsert, '/userboard')
api.add_resource(UserBoardUpdate, '/userboard/<id_userboard>')
api.add_resource(UserBoardRemove, '/userboard/<id_userboard>')


# Channels
api.add_resource(ChannelsResource, '/channels')
api.add_resource(ChannelsResourceById, '/channels/<id_channels>')
api.add_resource(ChannelsInsert, '/channels')
api.add_resource(ChannelsUpdate, '/channels/<id_channels>')
api.add_resource(ChannelsRemove, '/channels/<id_channels>')

# Moduls
api.add_resource(ModulsResource, '/moduls')
api.add_resource(ModulsResourceById, '/moduls/<id_moduls>')
api.add_resource(ModulsInsert, '/moduls')
api.add_resource(ModulsUpdate, '/moduls/<id_moduls>')
api.add_resource(ModulsRemove, '/moduls/<id_moduls>')

# POINT FITURED TRY
api.add_resource(TestPoint, '/point_test')

