# pyright: reportMissingModuleSource=false
from Http.Libs import DB

class TestModel(DB):
    table_name = 'admin'

    def findById(self, id):
        return self.select(id=id, isdel=0).fetch()
