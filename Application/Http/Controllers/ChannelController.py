import subprocess, json, time
from Http import app
from flask import request

from Http.Models import ChannelModel

@app.route('/channel/list')
def channel_List():
    channelModel = ChannelModel()

    param = {
        'num': '1',
        'title': 'abc',
        'group': '央视',
    }

    result = channelModel.updateById(1, param)
    print(result)

    return 'test'
