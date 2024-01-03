# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class ChannelModel(DB):
    table_name = 'channel'

    def findById(self, id):
        return self.select(id=id, isdel=0).fetch()

    def add(self, **kwargs):
        return self.save(**kwargs)

    def update(self, **kwargs):
        self.save(**kwargs)

    def delete(self, id):
        self.remove(id)

    def count(self):
        return self.counts(isdel=0).fetch()

    def findpage(self, page=1, limit=10):
        return self.select(isdel=0).orderBy('id desc').page(page, limit).fetch()

    def findlist(self, **kwargs):
        orderBy = kwargs['orderBy'] if 'orderBy' in kwargs else 'id desc'
        page = kwargs['page'] if 'page' in kwargs else 1
        limit = kwargs['limit'] if 'limit' in kwargs else 100
        return self.select(**kwargs['where']).orderBy(orderBy).page(page, limit).fetch()

