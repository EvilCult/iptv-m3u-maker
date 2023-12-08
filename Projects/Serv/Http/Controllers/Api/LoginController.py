# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Blueprint, request
from Http.Models import AdminModel
import json, time, hashlib, datetime, jwt

login_blueprint = Blueprint("login_blueprint", __name__, url_prefix="/api/v1/login")

@login_blueprint.route('/', methods=['POST'])
def api_login():
    req = request.get_json()
    uname = req['uname']
    pwd = req['pwd']
    admin = AdminModel().login(uname, pwd)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {},
        'time': int(time.time())
    }

    if admin is None:
        apiMsg['code'] = 1
        apiMsg['msg'] = '用户名或密码错误'
    else:
        data = {
            'exp': datetime.datetime.now() + datetime.timedelta(days=7),
            'iat': datetime.datetime.now(),
            'iss': 'EvilCult',
            'data': {
                'uid': admin['id'],
                'uname': admin['uname'],
            },
        }
        token = jwt.encode(data, 'Attack.on.Titan', algorithm='HS256')

        admin['lastlogin'] = admin['logintime']
        admin['logintime'] = int(time.time())
        AdminModel().update(**admin)

        apiMsg['code'] = 0
        apiMsg['msg'] = '登录成功'
        apiMsg['data'] = token

    return json.dumps(apiMsg, ensure_ascii=False)


