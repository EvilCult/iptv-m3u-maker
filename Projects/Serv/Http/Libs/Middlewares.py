# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import request
import time, jwt, json

def auth_middleware():
    if request.path.startswith('/api/v1/login'):
        return None

    token = request.headers.get('Authorization')
    try :
        payload = jwt.decode(token, 'Attack.on.Titan', issuer='EvilCult', algorithms=['HS256'])
        #more check
    except:
        print('auth_middleware: token error')
        apiMsg = {
            'code': 1,
            'msg' : 'Access Denied',
            'data': {},
            'time': int(time.time())
        }

        return json.dumps(apiMsg), 401

    return None


