# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class ChannelModel(DB):
    table_name = 'channel'

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

    def count(self):
        return self.counts()

    def findlist(self, page=1, limit=10):
        return self.select(page, limit)
