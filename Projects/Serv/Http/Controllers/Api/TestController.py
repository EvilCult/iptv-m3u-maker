# pyright: reportMissingModuleSource=false
from flask import Blueprint

from Http.Models import TestModel

import json, time

test_blueprint = Blueprint("test_blueprint", __name__, url_prefix="/api/v1/test")

@test_blueprint.route('/<int:id>', methods=['GET'])
def api_test_info(id):
    Test = TestModel()
    result = Test.findById(str(id))
    return json.dumps(result.data)