from functools import wraps
from app.helpers.rest import *
from app import redis_store
from flask import request
from app.models import model as db
import hashlib



def apikey_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'apikey' not in request.headers:
            return response(400, message=" Invalid access apikey ")
        else:
            access_token = db.get_by_id(
                    table="tb_channels",
                    field="channels_key",
                    value=request.headers['apikey']
                )
            if not access_token:
                return response(400, message=" Invalid access apikey ")

        return f(*args, **kwargs)
    return decorated_function