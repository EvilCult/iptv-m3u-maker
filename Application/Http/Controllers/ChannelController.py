import json
from Http import app
from flask import request

from Http.Models import ChannelModel

@app.route('/channel/list/', methods=['GET'])
@app.route('/channel/list/<page>', methods=['GET'])
def channel_List(page = 1):
    channelModel = ChannelModel()

    param = {
        "isdel": 0
    }

    typ = {
        'p': page,
        'ps': 20,
        'order': 'id ASC',
    }

    result = channelModel.getListByParam(param, typ)

    return json.dumps(result, ensure_ascii=False)
