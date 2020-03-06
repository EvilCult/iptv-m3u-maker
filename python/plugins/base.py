#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import time
import re
import db
import threading

class Source (object) :

    def __init__ (self):
        self.T = tools.Tools()
        self.now = int(time.time() * 1000)

    def getSource (self) :
        urlList = []

        url = 'https://www.jianshu.com/p/2499255c7e79'
        req = [
            'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
        ]
        res = self.T.getPage(url, req)

        if res['code'] == 200 :
            pattern = re.compile(r"<code(.*?)</code>", re.I|re.S)
            tmp = pattern.findall(res['body'])

            pattern = re.compile(r"#EXTINF:0,(.*?)\n#EXTVLCOPT:network-caching=1000\n(.*?)\n", re.I|re.S)

            sourceList = pattern.findall(tmp[0])
            sourceList = sourceList + pattern.findall(tmp[1])

            threads = []
            for item in sourceList :
                thread = threading.Thread(target = self.detectData, args = (item[0], item[1], ), daemon = True)
                thread.start()
                threads.append(thread)
            for t in threads:
                t.join()
        else :
            pass # MAYBE later :P

        return urlList

    def detectData (self, title, url) :
        info = self.T.fmtTitle(title)
        
        netstat = self.T.chkPlayable(url)

        if netstat > 0 :
            cros = 1 if self.T.chkCros(url) else 0
            data = {
                'title'  : str(info['id']) if info['id'] != '' else str(info['title']),
                'url'    : str(url),
                'quality': str(info['quality']),
                'delay'  : netstat,
                'level'  : str(info['level']),
                'cros'   : cros,
                'online' : 1,
                'udTime' : self.now,
            }
            
            self.addData(data)
            self.T.logger('正在分析[ %s ]: %s' % (str(info['id']) + str(info['title']), url))
        else :
            pass # MAYBE later :P

    def addData (self, data) :
        DB = db.DataBase()
        sql = "SELECT * FROM %s WHERE url = '%s'" % (DB.table, data['url'])
        result = DB.query(sql)

        if len(result) == 0 :
            data['enable'] = 1
            DB.insert(data)
        else :
            id = result[0][0]
            DB.edit(id, data)
