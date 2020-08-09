from Http import app
from flask import request

from Http.Models import UrlModel

@app.route('/')
def start():
    return 'Welcome!!'


@app.route('/url/list')
def url_list():
    urlModel = UrlModel()

    return urlModel.test()