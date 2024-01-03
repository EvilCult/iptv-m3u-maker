# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Blueprint, request
from Http.Models import ChannelModel
import json, time, requests, datetime, re

mapping_blueprint = Blueprint("mapping_blueprint", __name__, url_prefix="/api/v1/mapping")

@mapping_blueprint.route('/find', methods=['GET'])
def api_mapping_find():
    req = request.args

    keyword = req.get('keyword', '')
    if keyword == '':
        apiMsg = {
            'code': 1,
            'msg' : 'keyword error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    mapping = ChannelModel().findlist(where={'title LIKE': keyword})


    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': mapping,
        'time': int(time.time())
    }

    return json.dumps(apiMsg, ensure_ascii=False)
