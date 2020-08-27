from flask import Flask

app = Flask('__name__', static_url_path='')

def after_request(res):
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

app.after_request(after_request)

import Http.Controllers
import Http.Models
