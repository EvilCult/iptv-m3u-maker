# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class GuideModel(DB):
    table_name = 'guide'

    def findById(self, id):
        return self.select(id=id, isdel=0).fetch()

    def add(self, **kwargs):
        return self.save(**kwargs)

    def update(self, **kwargs):
        self.save(**kwargs)

    def delete(self, id):
        self.remove(id)

    def count(self, **kwargs):
        return self.counts(**kwargs['where']).fetch()

    def findlist(self, **kwargs):
        return self.select(**kwargs['where']).orderBy(kwargs['orderBy']).fetch()

