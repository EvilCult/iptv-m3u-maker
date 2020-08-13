import subprocess
import json
from Http import app
from flask import request

from Http.Models import BotModel

@app.route('/bot')
def bot():
    return 'Bot'

@app.route('/bot/channel/run')
def botList():
    botModel = BotModel()

    if botModel.getStat() == 0:
        botModel.setStat()

        spider_name = "channel"
        subprocess.check_output(['scrapy', 'crawl', spider_name])

        botModel.setStat(False)
    else:
        return 'Done'

