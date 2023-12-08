# pyright: reportMissingModuleSource=false
from Http.Libs import DB

class TestModel(DB):
    table_name = 'admin'

    def findById(self, id):
        return self.find(id)
