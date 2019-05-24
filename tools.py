#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import re
import ssl
import io
import gzip
import random
import socket
import time
import area

socket.setdefaulttimeout(10.0)

class Tools (object) :

    def __init__ (self) :
        pass

    def getPage (self, url, requestHeader = [], postData = {}) :
        fakeIp = self.fakeIp()
        requestHeader.append('CLIENT-IP:' + fakeIp)
        requestHeader.append('X-FORWARDED-FOR:' + fakeIp)

        if postData == {} :
            request = urllib.request.Request(url)
        elif isinstance(postData, str) :
            request = urllib.request.Request(url, postData)
        else :
            request = urllib.request.Request(url, urllib.parse.urlencode(postData).encode('utf-8'))

        for x in requestHeader :
            headerType = x.split(':')[0]
            headerCon = x.replace(headerType + ':', '')
            request.add_header(headerType, headerCon)

        try :
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urllib.request.urlopen(request, context = ctx)
            header = response.headers
            body = response.read().decode('utf-8')
            code = response.code
        except urllib.error.HTTPError as e:
            header = e.headers
            body = e.read().decode('utf-8')
            code = e.code

        result = {
            'code': code,
            'header': header,
            'body': body
        }

        return result

    def fakeIp (self) :
        fakeIpList = []

        for x in range(0, 4):
            fakeIpList.append(str(int(random.uniform(0, 255))))

        fakeIp = '.'.join(fakeIpList)

        return fakeIp

    def fmtCookie (self, string) :
        result = re.sub(r"path\=\/.", "", string)
        result = re.sub(r"(\S*?)\=deleted.", "", result)
        result = re.sub(r"expires\=(.*?)GMT;", "", result)
        result = re.sub(r"domain\=(.*?)tv.", "", result)
        result = re.sub(r"httponly", "", result)
        result = re.sub(r"\s", "", result)

        return result

    def urlencode(self, str) :
        reprStr = repr(str).replace(r'\x', '%')
        return reprStr[1:-1]

    def gzdecode(self, data) :
        try:
            compressedstream = io.StringIO(data)
            gziper = gzip.GzipFile(fileobj = compressedstream)
            html = gziper.read()
            return html
        except :
            return data

    def fmtTitle (self, string) :
        pattern = re.compile(r"(cctv[-|\s]*\d*)*\s*?([^fhd|^hd|^sd|^\.m3u8]*)\s*?(fhd|hd|sd)*", re.I)
        tmp = pattern.findall(string)[0]

        result = {
            'id'     : tmp[0].strip('-').strip(),
            'title'  : tmp[1].strip('-').strip(),
            'quality': tmp[2].strip('-').strip(),
            'level'  : 4,
        }

        if result['id'] != '':
            pattern = re.compile(r"cctv[-|\s]*(\d*)", re.I)
            result['id'] = re.sub(pattern, "CCTV-\\1", result['id'])
            
            if '+' in result['title'] :
                result['id'] = result['id'] + str('+')

        Area = area.Area()
        result['level'] = Area.classify(str(result['id']) + str(result['title']))

        return result

    def chkPlayable (self, url) :
        try:
            startTime = int(round(time.time() * 1000))
            res = self.getPage(url)

            if res['code'] == 200 :
                endTime = int(round(time.time() * 1000))
                useTime = endTime - startTime
                return int(useTime)
            else:
                return 0
        except:
            return 0

