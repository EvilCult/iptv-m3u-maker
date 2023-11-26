# pyright: reportMissingModuleSource=false
from flask import Flask

app = Flask('__name__', static_url_path='')
app.debug = True

def after_request(res):
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST,DELETE,PATCH,PUT'
    res.headers['Access-Control-Allow-Headers'] = 'Authorization'
    return res

app.after_request(after_request)

import Http.Controllers
import Http.Models
