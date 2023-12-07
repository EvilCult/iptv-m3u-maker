# pyright: reportMissingModuleSource=false
from Http import app
from flask import request

from Http.Controllers.Api.TestController import test_blueprint
app.register_blueprint(test_blueprint)

from Http.Controllers.Api.LoginController import login_blueprint
app.register_blueprint(login_blueprint)

from Http.Controllers.Api.ChannelController import channel_blueprint
app.register_blueprint(channel_blueprint)
