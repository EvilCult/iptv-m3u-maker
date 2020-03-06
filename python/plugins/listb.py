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
        self.siteUrl = str('http://m.iptv807.com/')

    def getSource (self) :
        urlList = []

        url = self.siteUrl
        req = [
            'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
        ]
        res = self.T.getPage(url, req)

        if res['code'] == 200 :
            pattern = re.compile(r"<li><a href=\"(.*?)\" data-ajax=\"false\">.*?<\/a><\/li>", re.I|re.S)
            postList = pattern.findall(res['body'])

            for post in postList :
                url = self.siteUrl + post
                req = [
                    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                ]
                res = self.T.getPage(url, req)

                if res['code'] == 200 :
                    pattern = re.compile(r"<li><a href=\"(.*?)\" data-ajax=\"false\">(.*?)<\/a><\/li>", re.I|re.S)
                    channelList = pattern.findall(res['body'])
                    threads = []

                    for channel in channelList :
                        channelUrl = self.siteUrl + channel[0]
                        thread = threading.Thread(target = self.detectData, args = (channel[1], channelUrl, ), daemon = True)
                        thread.start()
                        threads.append(thread)

                    for t in threads:
                        t.join()

                else :
                    pass # MAYBE later :P

    def detectData (self, title, url) :
        req = [
            'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        ]

        info = self.T.fmtTitle(title)

        playInfo = self.T.getPage(url, req)
        pattern = re.compile(r"<option value=\"(.*?)\">.*?<\/option>", re.I|re.S)
        playUrlList = pattern.findall(playInfo['body'])

        if len(playUrlList) > 0 :
            playUrl = playUrlList[0]
            midM3uInfo = self.T.getPage(playUrl, req)

            pattern = re.compile(r"url: '(.*?)',", re.I|re.S)
            midM3uUrlList = pattern.findall(midM3uInfo['body'])
            if len(midM3uUrlList) > 0 :
                midM3uUrl = midM3uUrlList[0]

                if midM3uUrl != '' :
                    m3u = self.T.getRealUrl(midM3uUrl)

                    try :
                        m3u.index('migu.php?token=')
                    except :
                        if m3u != '' :
                            netstat = self.T.chkPlayable(m3u)
                        else :
                            netstat = 0

                        if netstat > 0 :
                            cros = 1 if self.T.chkCros(m3u) else 0
                            data = {
                                'title'  : str(info['id']) if info['id'] != '' else str(info['title']),
                                'url'    : str(m3u),
                                'quality': str(info['quality']),
                                'delay'  : netstat,
                                'level'  : str(info['level']),
                                'cros'   : cros,
                                'online' : 1,
                                'udTime' : self.now,
                            }
                            self.addData(data)
                            self.T.logger('正在分析[ %s ]: %s' % (str(info['id']) + str(info['title']), m3u))
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
