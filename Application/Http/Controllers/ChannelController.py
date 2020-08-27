import json
from Http import app
from flask import request

from Http.Models import ChannelModel

@app.route('/channel/list/', methods=['GET'])
@app.route('/channel/list/<page>', methods=['GET'])
def channel_List(page = 1):
    channelModel = ChannelModel()

    tmp = {
        'err': 0,
        'data': [],
        'count': 0,
        'msg':'',
    }

    param = {
        "isdel": 0
    }

    typ = {
        'p': page,
        'ps': 20,
        'order': 'id ASC',
    }

    tmp['data'] = channelModel.getListByParam(param, typ)
    tmp['count'] = channelModel.getListByParam(param, 'count')

    res = json.dumps(tmp, ensure_ascii=False)

    return res
