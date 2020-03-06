#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
resourcePath = '/srv/iptv/http'

@app.route('/')
def index():
    return send_from_directory(resourcePath, 'tv.json')

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 9527,  
        debug = True 
    )

