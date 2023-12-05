# pyright: reportMissingModuleSource=false
from Http import app
from flask import request

from Http.Controllers.Api.TestController import test_blueprint
app.register_blueprint(test_blueprint)

from Http.Controllers.Api.TestXController import testx_blueprint
app.register_blueprint(testx_blueprint)
