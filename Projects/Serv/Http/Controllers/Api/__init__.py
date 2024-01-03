# pyright: reportMissingModuleSource=false
from Http import app
from Http.Libs.Middlewares import auth_middleware

@app.before_request
def before_request():
    return auth_middleware()

from Http.Controllers.Api.TestController import test_blueprint
app.register_blueprint(test_blueprint)

from Http.Controllers.Api.LoginController import login_blueprint
app.register_blueprint(login_blueprint)

from Http.Controllers.Api.ChannelController import channel_blueprint
app.register_blueprint(channel_blueprint)

from Http.Controllers.Api.TvController import tv_blueprint
app.register_blueprint(tv_blueprint)

from Http.Controllers.Api.MappingController import mapping_blueprint
app.register_blueprint(mapping_blueprint)
