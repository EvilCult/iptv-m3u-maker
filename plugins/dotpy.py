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

        sourcePath = './plugins/dotpy_source'
        with open(sourcePath, 'r') as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                line = lines[i].strip('\n')
                item = line.split(',', 1)

                print('Checking[' + str(i) + ']:' + str(item[0]))
                netstat = self.T.chkPlayable(item[1])

                if netstat > 0 :
                    info = self.T.fmtTitle(item[0])

                    data = {
                        'title'  : str(info['id']) if info['id'] != '' else str(info['title']),
                        'url'    : str(item[1]),
                        'quality': str(info['quality']),
                        'delay'  : netstat,
                        'level'  : info['level'],
                        'online' : 1,
                        'udTime' : self.now,
                    }
                    urlList.append(data)
                else :
                    pass # MAYBE later :P


        return urlList
