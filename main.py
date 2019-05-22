#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import re

class Iptv :

    def __init__ (self) :
        self.T = tools.Tools()

    def getSourceA (self) :
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


            for item in sourceList :
                playable = self.chkPlayable(item[1])

                if playable == True :
                    info = self.fmtTitle(item[0])
                    print('title: ' + str(info['id']) + ' ' + str(info['title']))
                    print('url: ' + str(item[1]))
                else :
                    pass # MAYBE later :P
        else :
            pass # MAYBE later :P

    def chkPlayable (self, url) :
        try:
            res = self.T.getPage(url)

            if res['code'] == 200 :
                return True
            else:
                return False
        except:
            return False


    def baseFilter (self) :
        pass

    def fmtTitle (self, string) :
        pattern = re.compile(r"(cctv[-|\s]*\d*)*\s*?([^fhd|^hd|^sd|^\.m3u8]*)\s*?(fhd|hd|sd)*", re.I)
        tmp = pattern.findall(string)[0]

        result = {
            'id'     : tmp[0].strip('-').strip(),
            'title'  : tmp[1].strip('-').strip(),
            'quality': tmp[2].strip('-').strip(),
        }

        return result

obj = Iptv()
obj.getSourceA()
