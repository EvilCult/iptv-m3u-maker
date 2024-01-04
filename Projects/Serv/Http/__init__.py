# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Flask

from Http.Libs import Launch

app = Flask('__name__', static_url_path='')
app.debug = True

Launch().chkDB()

def after_request(res):
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST,DELETE,PATCH,PUT'
    res.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return res

app.after_request(after_request)

import Http.Controllers
import Http.Models
