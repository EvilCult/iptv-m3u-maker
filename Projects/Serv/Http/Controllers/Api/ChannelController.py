# pyright: reportMissingModuleSource=false
from flask import Blueprint, request

from Http.Models import ChannelModel
from Http.Libs.Middlewares import auth_middleware


import json, time

channel_blueprint = Blueprint("channel_blueprint", __name__, url_prefix="/api/v1/channel")

@channel_blueprint.route('/add', methods=['POST'])
@auth_middleware
def api_channel_add():
    req = request.get_json()

    channel = {
        'title': req['title'],
        'url': req['url'],
        'addtime': int(time.time()),
    }

    channel_id = ChannelModel().add(**channel)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': channel_id,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
