# pyright: reportMissingModuleSource=false
from Http import app
from flask import request

@app.route('/test', methods=['GET'])
def test():
    return 'this is a test message'