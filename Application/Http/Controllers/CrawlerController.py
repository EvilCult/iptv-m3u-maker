from Http import app
from flask import request

@app.route('/crawl')
def crawl():
    return 'crawl!!'
