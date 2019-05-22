#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import re

class Iptv :

    def __init__ (self) :
        self.T = tools.Tools()

    def test (self) :
        itemName = 'cctv-高清频道 世界地理 fhd'
        result = self.fmtTitle(itemName)
        return result

    def fmtTitle (self, string) :
        pattern = re.compile(r"(cctv[-|\s]*\d*)*\s*?([^\w]*)\s*?(fhd|hd|sd)*", re.I)
        tmp = pattern.findall(string)[0]

        result = {
            'id'     : tmp[0].strip('-').strip(),
            'title'  : tmp[1].strip('-').strip(),
            'quality': tmp[2].strip('-').strip(),
        }

        return result

obj = Iptv()
str = obj.test()
print(str)
