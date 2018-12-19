from flask_restful import Resource, reqparse, request
from app.helpers.rest import response
from app.helpers import cmd_parser as cmd
from app import psycopg2
from app.libs import utils
from app.models import model as db
from app.middlewares.auth import jwt_required
from app.helpers import endpoint_parse as ep


class TestPoint(Resource):
    def post(self):
        json_req = request.get_json(force=True)
        command = utils.get_command(request.path)
        command = command
        init_data = cmd.parser(json_req, command)
        a = ep.endpoint_parser(command, init_data)
        return response(200, data=a)