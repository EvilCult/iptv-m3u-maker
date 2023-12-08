# pyright: reportMissingModuleSource=false
from flask import Blueprint, request
from Http.Models import ChannelModel
import json, time

channel_blueprint = Blueprint("channel_blueprint", __name__, url_prefix="/api/v1/channel")

@channel_blueprint.route('/add', methods=['POST'])
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

@channel_blueprint.route('/add/txt', methods=['POST'])
def api_channel_addtxt():
    req = request.get_json()

    channel_list = []
    channel_name = ''
    channel_url = ''
    for line in req['data'].splitlines():
        if line.startswith('#EXTINF:'):
            channel_name = line.split(',')[1]
        elif line.startswith('http'):
            channel_url = line
            channel_list.append({'title': channel_name, 'url': channel_url})

    channel_ids = []
    for channel in channel_list:
        channel_ids.append(ChannelModel().add(**channel))

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': channel_ids,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
