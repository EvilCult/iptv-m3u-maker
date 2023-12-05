# pyright: reportMissingModuleSource=false
from Http.Libs import DB

class TestModel(DB):
    table_name = 'test'

    def findById(self, id):
        return self.find(id)
