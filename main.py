#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
import db
import time
import re
from plugins import base
from plugins import lista

class Iptv (object):

    def __init__ (self) :
        self.T = tools.Tools()
        self.DB = db.DataBase()

    def run(self) :
        Base = base.Source()
        urlList = Base.getSource()
        for item in urlList :
            self.addData(item)
        self.outPut()
        print("DONE!!")

    def addData (self, data) :
        sql = "SELECT * FROM %s WHERE url = '%s'" % (self.DB.table, data['url'])
        result = self.DB.query(sql)

        if len(result) == 0 :
            self.DB.insert(data)
        else :
            id = result[0][0]
            self.DB.edit(id, data)

    def outPut (self) :
        sql = "SELECT * FROM %s GROUP BY title HAVING online = 1 ORDER BY id ASC" % (self.DB.table)
        result = self.DB.query(sql)

        with open('tv.m3u8', 'w') as f:
            f.write("#EXTM3U\n")
            for item in result :
                f.write("#EXTINF:-1,%s\n" % (item[1]))
                f.write("%s\n" % (item[3]))

obj = Iptv()
obj.run()





