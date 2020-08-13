import subprocess
import json
from Http import app
from flask import request
import time
from concurrent.futures import ThreadPoolExecutor

from Http.Models import BotModel

executor = ThreadPoolExecutor(2)

@app.route('/bot')
def bot():
    botModel = BotModel()

    if botModel.getStat() == 0:
        executor.submit(realTask, 'test message')
        return 'Start'
    else:
        return 'Running'


@app.route('/bot/channel/run')
def botList():
    botModel = BotModel()

    result = {
        'err': 0,
        'msg': '',
        'data': [],
    }

    if botModel.getStat() == 0:
        executor.submit(realTask, 'channel')
        result['msg'] = 'start'
    else:
        result['err'] = 1
        result['msg'] = 'running'

    return json.dumps(result)

def realTask(spider):
    botModel = BotModel()

    botModel.setStat()

    try:
        subprocess.check_output(['scrapy', 'crawl', spider])
    except:
        pass

    botModel.setStat(False)
