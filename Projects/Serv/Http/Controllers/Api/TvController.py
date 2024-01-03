# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import Blueprint, request
from Http.Models import TvModel, EpgModel, GuideModel
import json, time, requests, datetime, re

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

@tv_blueprint.route('/add/epg', methods=['PUT'])
def api_tv_addepg():
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
        addGuideData(res.text, epg_id)
        apiMsg = {
            'code': 0,
            'msg' : '',
            'data': tv_ids,
            'time': int(time.time())
        }

    return json.dumps(apiMsg)

def addTvData(data, epg_id, update=False):
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
        if not update:
            tv_id = TvModel().add(**tv)
            tv_ids.append(tv_id)
        else:
            tv_params = {
                'where': {
                    'tvgid': tv['tvgid'],
                    'epgid': tv['epgid']
                }
            }
            tv_counts = TvModel().count(**tv_params)
            if tv_counts == 0:
                tv_id = TvModel().add(**tv)
                tv_ids.append(tv_id)

    return tv_ids

def addGuideData(data, epg_id):
    guide_list = []

    data = data.replace('><', '>\n<')

    for line in data.split('\n'):
        line = line.strip()
        if line.startswith('<programme'):
            tv_id = re.findall(r'channel="(.*?)"', line)[0]

            start = re.findall(r'start="(.*?)"', line)[0]
            start = datetime.datetime.strptime(start, '%Y%m%d%H%M%S %z')
            start = int(start.timestamp())

            stop = re.findall(r'stop="(.*?)"', line)[0]
            stop = datetime.datetime.strptime(stop, '%Y%m%d%H%M%S %z')
            stop = int(stop.timestamp())

            guide = {
                'epgid'  : epg_id,
                'tvid'   : tv_id,
                'title'  : line.split('"')[1],
                'start'  : start,
                'stop'   : stop,
                'addtime': int(time.time())
            }
        elif line.startswith('<title'):
            guide['title'] = line.split('>')[1].split('<')[0]
            guide_list.append(guide)
        else:
            continue

    for guide in guide_list:
        GuideModel().add(**guide)

    return True

@tv_blueprint.route('/update', methods=['POST'])
def api_tv_update():
    req = request.get_json()

    if 'id' not in req:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    tv = {
        'id': req['id'],
    }

    if 'title' in req:
        tv['title'] = req['title']

    if 'icon' in req:
        tv['icon'] = req['icon']

    if 'category' in req:
        tv['category'] = req['category']

    TvModel().update(**tv)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': True,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@tv_blueprint.route('/list', methods=['GET'])
def api_tv_list():
    req = request.args

    page = req.get('page', 1)
    limit = req.get('limit', 20)
    orderBy = req.get('orderBy', 'tvgid')
    search = req.get('search', '')
    keyword = req.get('keyword', '')

    tvFilter = {
        'page': page,
        'limit': limit,
        'orderBy': orderBy,
        'where': {
            'isdel': 0
        }
    }
    if search != '':
        tvFilter['where'][str(search) + ' LIKE'] = keyword

    tv_list = TvModel().findlist(**tvFilter)
    tv_count = TvModel().count(**tvFilter)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {
            'list': tv_list,
            'count': tv_count
        },
        'time': int(time.time())
    }

    return json.dumps(apiMsg, ensure_ascii=False)

@tv_blueprint.route('/epg/list', methods=['GET'])
def api_tv_epg_list():
    req = request.args

    page = req.get('page', 1)
    limit = req.get('limit', 20)

    epg_list = EpgModel().findpage(page=page, limit=limit)
    epg_count = EpgModel().count()

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {
            'list': epg_list,
            'count': epg_count
        },
        'time': int(time.time())
    }

    return json.dumps(apiMsg, ensure_ascii=False)

@tv_blueprint.route('/guide/<path:tvid>', methods=['GET'])
def api_tv_list_guide(tvid=None):
    guideFilter = {
        'orderBy': 'start',
        'where': {
            'tvid': tvid
        }
    }

    guide_list = GuideModel().findlist(**guideFilter)
    guide_count = GuideModel().count(**guideFilter)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': {
            'list': guide_list,
            'count': guide_count
        },
        'time': int(time.time())
    }

    return json.dumps(apiMsg, ensure_ascii=False)

@tv_blueprint.route('/remove/<int:id>', methods=['DELETE'])
def api_tv_remove(id=None):
    req = request.args

    if id == None:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)


    tv = TvModel().findById(id=id)
    if len(tv) == 0:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    tv = tv[0]
    delInfo = {
        'id': id,
        'isdel': 1
    }
    TvModel().update(**delInfo)

    delInfo = {
        'tvid': tv['tvgid']
    }
    GuideModel().delete(**delInfo)

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': True,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@tv_blueprint.route('/remove/epg/<int:id>', methods=['DELETE'])
def api_tv_remove_epg(id):
    req = request.args

    if id == None:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    epg = EpgModel().findById(id=id)
    if len(epg) == 0:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    epg = epg[0]
    delInfo = {
        'id': id,
        'isdel': 1
    }
    EpgModel().update(**delInfo)
    TvModel().delete(epgid=epg['id'])
    GuideModel().delete(epgid=epg['id'])

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': True,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)

@tv_blueprint.route('/epg/update', methods=['POST'])
def api_tv_epg_update():
    req = request.get_json()

    if 'id' not in req:
        apiMsg = {
            'code': 1,
            'msg' : 'id error',
            'data': {},
            'time': int(time.time())
        }
        return json.dumps(apiMsg)

    ids = []
    if int(req['id']) == 0:
        for epg in EpgModel().findall():
            ids.append(epg['id'])
    else:
        ids.append(req['id'])

    for id in ids:
        epg = EpgModel().findById(id=id)
        if len(epg) == 0:
            continue

        epg = epg[0]
        res = requests.get(epg['url'])
        if res.status_code != 200:
            continue

        res.encoding = 'utf-8'
        addTvData(res.text, epg['id'], True)

        GuideModel().delete(epgid=epg['id'])
        addGuideData(res.text, epg['id'])

    apiMsg = {
        'code': 0,
        'msg' : '',
        'data': True,
        'time': int(time.time())
    }

    return json.dumps(apiMsg)
