from flask import request
import time, jwt, json

def auth_middleware(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        try :
            payload = jwt.decode(token, 'Attack.on.Titan', issuer='EvilCult', algorithms=['HS256'])
            #more check
        except:
            apiMsg = {
                'code': 1,
                'msg' : 'Access Denied',
                'data': {},
                'time': int(time.time())
            }

            return json.dumps(apiMsg), 401

        result = func(*args, **kwargs)
        return result

    return wrapper
