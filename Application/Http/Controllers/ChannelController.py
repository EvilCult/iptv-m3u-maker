import subprocess, json, time
from Http import app
from flask import request

from Http.Models import ChannelModel

@app.route('/channel/list')
def channel_List():
    channelModel = ChannelModel()

    param = {
        "isdel": 0
    }

    result = channelModel.getListByParam(param, 'count')
    print(result)

    return 'test'
