# pyright: reportMissingModuleSource=false
from flask import Blueprint

from Http.Models import TestModel
from Http.Libs.Middlewares import auth_middleware


import json, time

channel_blueprint = Blueprint("channel_blueprint", __name__, url_prefix="/api/v1/channel")

@channel_blueprint.route('/<int:id>', methods=['GET'])
@auth_middleware
def api_channel_info(id):
    Test = TestModel()

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': Test.findById(str(id)),
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
