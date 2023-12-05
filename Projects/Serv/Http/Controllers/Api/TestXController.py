# pyright: reportMissingModuleSource=false
from flask import Blueprint

from Http.Models import TestModel

import json, time

testx_blueprint = Blueprint("testx_blueprint", __name__, url_prefix="/api/v1/testx")

@testx_blueprint.route('/<int:id>', methods=['GET'])
def api_test_info(id):
    return json.dumps({"id": id, "name": "test", "time": time.time()})
    # Test = TestModel()
    # result = Test.findById(str(id))
    # return json.dumps(result.data)
