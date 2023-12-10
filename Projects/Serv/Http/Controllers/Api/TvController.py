# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Blueprint, request
from Http.Models import TvModel
import json, time, requests

tv_blueprint = Blueprint("tv_blueprint", __name__, url_prefix="/api/v1/tv")

@tv_blueprint.route('/add', methods=['PUT'])
def api_tv_add():
    req = request.get_json()

    tv = {
        'tvgname': req['tvgname'] if 'tvgname' in req else '',
        'tvgid': req['tvgid'] if 'tvgid' in req else 0,
        'title': req['title'] if 'title' in req else (req['tvgname'] if 'tvgname' in req else ''),
        'icon': req['icon'] if 'icon' in req else '',
        'category': req['category'] if 'category' in req else 0
    }

    tv_id = TvModel().add(**tv)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': tv_id,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
