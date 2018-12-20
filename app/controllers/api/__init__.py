from flask import Blueprint
from flask_restful import Api
from .moduls import *


api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)
api.add_resource(SendModuls, '/send/<id_channels>')
api.add_resource(GetChannelsData, '/get/channels/<id_channels>')
api.add_resource(GetChannelDataByField, '/get/<id_channels>/limit/<page>')
