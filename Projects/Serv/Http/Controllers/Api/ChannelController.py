# pyright: reportMissingModuleSource=false
from flask import Blueprint, request
from Http.Models import ChannelModel
import json, time, requests

channel_blueprint = Blueprint("channel_blueprint", __name__, url_prefix="/api/v1/channel")

@channel_blueprint.route('/add', methods=['PUT'])
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

@channel_blueprint.route('/add/txt', methods=['PUT'])
def api_channel_addtxt():
    req = request.get_json()

    channel_ids = addChannelData(req['data'])

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': channel_ids,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@channel_blueprint.route('/add/url', methods=['PUT'])
def api_channel_addurl():
    req = request.get_json()

    url = req['url']

    res = requests.get(url)
    if res.status_code != 200:
        apiMsg = {
            'code': 1,
            'msg' : 'url error',
            'data': {},
            'time': int(time.time())
        }
    else:
        channel_ids = addChannelData(res.text)

        apiMsg = {
            'code': 0,
            'msg' : '',
            'data': channel_ids,
            'time': int(time.time())
        }

    return json.dumps(apiMsg)

def addChannelData(data):
    channel_list = []
    channel_name = ''
    channel_url = ''
    for line in data.splitlines():
        if line.startswith('#EXTINF:'):
            channel_name = line.split(',')[1]
        elif line.startswith('http'):
            channel_url = line
            channel_list.append({'title': channel_name, 'url': channel_url})

    channel_ids = []
    for channel in channel_list:
        channel_ids.append(ChannelModel().add(**channel))

    return channel_ids

@channel_blueprint.route('/list', methods=['GET'])
def api_channel_list():
    Channel = ChannelModel()

    req = request.args

    page = req.get('page', 1)
    limit = req.get('limit', 20)


    Channel = ChannelModel()

    channel_list = Channel.findlist(page, limit)
    channel_count = Channel.count()

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {
            'list': channel_list,
            'count': channel_count
        },
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@channel_blueprint.route('/info/<int:id>', methods=['GET'])
def api_channel_info(id):
    channel = ChannelModel().findById(id)

    if len(channel) > 0:
        apiMsg = {
            'code': 0,
            'msg' : '',
            'data': channel[0],
            'time': int(time.time())
        }
    else :
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }

    return json.dumps(apiMsg)

@channel_blueprint.route('/update', methods=['POST'])
def api_channel_update():
    req = request.get_json()

    if 'id' not in req:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    channel = {
        'id': req['id'],
    }

    if 'title' in req:
        channel['title'] = req['title']

    if 'url' in req:
        channel['url'] = req['url']

    if 'alive' in req:
        channel['alive'] = req['alive']

    if 'ping' in req:
        channel['ping'] = req['ping']

    ChannelModel().update(**channel)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {},
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@channel_blueprint.route('/delete', methods=['DELETE'])
def api_channel_delete():
    req = request.get_json()

    if 'id' not in req:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    #soft delete
    channel = {
        'id': req['id'],
        'isdel': '1'
    }
    ChannelModel().update(**channel)

    #real delete
    #ChannelModel().delete(req['id'])

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {},
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
