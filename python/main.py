#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory
import tools
import iptv

class Main (object):
    def __init__ (self) :
        pass

    def scan (self):
        Crawler = iptv.Iptv()
        Crawler.run()

    def site (self):
        web = Flask(__name__)
        resourcePath = '/srv/iptv/http'

        @web.route('/')
        def index():
            return send_from_directory(resourcePath, 'index.html')

        @web.route('/m3u8')
        def m3u8():
            return send_from_directory(resourcePath, 'tv.m3u8')

        @web.route('/json')
        def json():
            return send_from_directory(resourcePath, 'tv.json')

        @web.route('/log')
        def log():
            return send_from_directory(resourcePath, 'log.txt')

        web.run(
            host = '0.0.0.0',
            port = 9527,  
            debug = False 
        )

    def run (self):
        t = tools.Tools()
        t.logger('123')

if __name__ == '__main__':
    App = Main()
    App.site()

