# pyright: reportMissingModuleSource=false
import hashlib
from flask import Blueprint, request

from Http.Models import AdminModel

import json, time

login_blueprint = Blueprint("login_blueprint", __name__, url_prefix="/api/v1/login")

@login_blueprint.route('/', methods=['POST'])
def api_login():
    data = request.get_json()
    uname = data['uname']
    pwd = data['pwd']
    admin = AdminModel().login(uname, pwd)

    msg = {}
    if admin is None:
        return json.dumps({'code': 1, 'msg': '用户名或密码错误'}, ensure_ascii=False)
    else:
        msg['code'] = 0
        msg['msg'] = '登录成功'
        msg['token'] = hashlib.sha256((str(admin['id']) + str(time.time())).encode()).hexdigest()

    return json.dumps(msg, ensure_ascii=False)


