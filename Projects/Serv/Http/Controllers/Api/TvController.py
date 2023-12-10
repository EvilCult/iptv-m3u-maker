# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Blueprint, request
from Http.Models import TvModel, EpgModel
import json, time, requests, chardet

tv_blueprint = Blueprint("tv_blueprint", __name__, url_prefix="/api/v1/tv")

@tv_blueprint.route('/add', methods=['PUT'])
def api_tv_add():
    req = request.get_json()

    tv = {
        'tvgname': req['tvgname'] if 'tvgname' in req else '',
        'tvgid': req['tvgid'] if 'tvgid' in req else 0,
        'title': req['title'] if 'title' in req else (req['tvgname'] if 'tvgname' in req else ''),
        'icon': req['icon'] if 'icon' in req else '',
        'category': req['category'] if 'category' in req else 0
    }

    tv_id = TvModel().add(**tv)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': tv_id,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@tv_blueprint.route('/add/url', methods=['PUT'])
def api_tv_addurl():
    req = request.get_json()

    url = req['url']

    res = requests.get(url)
    if res.status_code != 200:
        apiMsg = {
            'code': 1,
            'msg' : 'url error',
            'data': {},
            'time': int(time.time())
        }
    else:
        res.encoding = 'utf-8'
        epg = {
            'title': req['title'] if 'title' in req else 'untitled',
            'url': url,
            'addtime': int(time.time())
        }
        epg_id = EpgModel().add(**epg)
        tv_ids = addTvData(res.text, epg_id)

        apiMsg = {
            'code': 0,
            'msg' : '',
            'data': tv_ids,
            'time': int(time.time())
        }

    return json.dumps(apiMsg)

def addTvData(data, epg_id):
    tv_list = []
    tv_tvgid = ''
    tv_tvgname = ''

    data = data.replace('><', '>\n<')

    for line in data.split('\n'):
        line = line.strip()
        if line.startswith('<tv'):
            continue
        elif line.startswith('<channel'):
            tv_tvgid = line.split('"')[1]
        elif line.startswith('<display-name'):
            tv_tvgname = line.split('>')[1].split('<')[0]
        elif line.startswith('</channel'):
            tv = {
                'tvgname': tv_tvgname,
                'tvgid': tv_tvgid,
                'title': tv_tvgname,
                'icon': '',
                'epgid': epg_id,
                'category': 0
            }
            tv_list.append(tv)
        else:
            continue

    tv_ids = []
    for tv in tv_list:
        tv_id = TvModel().add(**tv)
        tv_ids.append(tv_id)

    return tv_ids
