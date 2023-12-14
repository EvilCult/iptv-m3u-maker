# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class TvModel(DB):
    table_name = 'tv'

    def findById(self, id):
        return self.select(id=id, isdel=0).fetch()

    def add(self, **kwargs):
        return self.save(**kwargs)

    def update(self, **kwargs):
        self.save(**kwargs)

    def delete(self, **kwargs):
        self.rmall(**kwargs)

    def count(self, **kwargs):
        return self.counts(isdel=0).fetch()

    def findlist(self, **kwargs):
        return self.select(**kwargs['where']).orderBy(kwargs['orderBy']).page(kwargs['page'], kwargs['limit']).fetch()
