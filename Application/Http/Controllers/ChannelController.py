import subprocess, json, time
from Http import app
from flask import request

from Http.Models import ChannelModel

@app.route('/channel/list')
def channel_List():
    channelModel = ChannelModel()
    
    
