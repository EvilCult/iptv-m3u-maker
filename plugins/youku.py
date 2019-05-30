#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import time
import re

class Source (object) :

    def __init__ (self):
        self.T = tools.Tools()
        self.now = int(time.time() * 1000)

    def getSource (self) :
        urlList = []

        url = 'https://list.youku.com/category/show/c_96.html'
        req = [
            'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
            'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'upgrade-insecure-requests: 1',
            'cookie: __ysuid=1540876852049YWA; __aysid=1559125737129tko; cna=iK1MFHdGNCACAdr3tQLvfWyB; _uab_collina=155912582425707377578055; yseidcount=1; juid=01dc1iku0414jb; ysestep=2; ystep=2; __ayft=1559193264281; __arpvid=1559193264282uJi2mp-1559193264434; __ayscnt=1; __aypstp=1; __ayspstp=9; P_ck_ctl=42B48D36975844B47D704789EF1B626C; isg=BG5utJpDvrYTl8rTl-ad8dTiv8I6b6UxM4jYMJg3inGsew7VAP96ez95Mq8yhyqB',
        ]
        res = self.T.getPage(url, req)

        if res['code'] == 200 :
            pattern = re.compile(r"window\.__INITIAL_DATA__(.*?)categoryFilter\":{\"", re.I|re.S)
            contentJS = pattern.findall(res['body'])

            pattern = re.compile(r"\"title\":\"(.*?)\".*?\"videoId\":\"(.*?)\"", re.I|re.S)
            movList = pattern.findall(contentJS[0])
            movList = movList[1]
            for mov in movList :
                info = self.getVideoInfo('XNDIwMDAyMzE3Mg==')
                print(info)

        return urlList

    def getVideoInfo (self, videoId) :
        infoUrl = 'https://ups.youku.com/ups/get.json?&ccode=0501&client_ip=0.0.0.0&client_ts=1559195109&utid=QM7jEAtFLzkCAdr3tQK%2BqDe4&vid='

        info = ''
        try:
            res = self.T.getPage(infoUrl + videoId, ['Referer:http://c-h5.youku.com/'])
            print(res)
            if res['body'] == '' :
                info = False
        except:
            info = False

        return info
