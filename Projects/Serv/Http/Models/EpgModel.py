# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class EpgModel(DB):
    table_name = 'epg'

    def findById(self, id):
        return self.select(id=id).fetch()

    def add(self, **kwargs):
        return self.save(**kwargs)

    def update(self, **kwargs):
        self.save(**kwargs)

    def delete(self, id):
        self.remove(id)

    def count(self):
        return self.counts(isdel=0).fetch()

    def findlist(self, page=1, limit=10):
        return self.select(isdel=0).orderBy('id desc').page(page, limit).fetch()

