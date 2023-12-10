# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class TvModel(DB):
    table_name = 'tv'

    def findById(self, id):
        return self.find(id)

    def add(self, **kwargs):
        self.data = kwargs
        self.save()
        return self.data['id']

    def update(self, **kwargs):
        self.data = kwargs
        self.save()

    def delete(self, id):
        self.remove(id)

    def count(self, **kwargs):
        return self.counts(**kwargs)

    def findlist(self, page=1, limit=10):
        return self.select(page, limit)

    def findlistbywhere(self, **kwargs):
        return self.where(**kwargs)
