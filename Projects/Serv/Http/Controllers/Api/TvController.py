# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Blueprint, request
from Http.Models import ChannelModel
import json, time, requests

tv_blueprint = Blueprint("tv_blueprint", __name__, url_prefix="/api/v1/tv")

@tv_blueprint.route('/add', methods=['PUT'])
def api_tv_add():
    req = request.get_json()

    channel = {
        'title': req['title'],
        'url': req['url'],
        'addtime': int(time.time()),
    }

    tv_id = ChannelModel().add(**channel)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': tv_id,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
