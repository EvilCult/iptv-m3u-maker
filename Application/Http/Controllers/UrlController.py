from Http import app
from flask import request

from Http.Models import UrlModel

@app.route('/url/test')
def url_test():
    urlModel = UrlModel()

    return urlModel.test()

@app.route('/url/list')
def url_list():

    return '/url/list'