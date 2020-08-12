import subprocess
from Http import app
from flask import request

@app.route('/bot')
def bot():
    return 'crawl!!'

@app.route('/bot/channel/run')
def botList():
    spider_name = "channel"
    subprocess.check_output(['scrapy', 'crawl', spider_name])

