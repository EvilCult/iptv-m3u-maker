from Http.Libs import DB

class ChannelModel:
    def __init__(self):
        self.db = DB()
        self.db.tbName = 'tvg_info'

    def getListByParam(self, param, typ):
        return self.db.getListByParam(param, typ)

    def getById(self, id):
        return self.db.getById(id)

    def updateById(self, id, data):
        return self.db.updateById(id, data)

    def delById(self, id):
        return self.db.delById(id)

    def addData(self, data):
        return self.db.addData(data)

