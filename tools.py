#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import re
import ssl
import os
import platform
import sys
import io
import gzip
import random
import socket

socket.setdefaulttimeout(10.0)

class Tools :

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

	def isWin (self) :
		osType = platform.system()

		if osType == 'Windows' :
			return True
		else :
			return False
