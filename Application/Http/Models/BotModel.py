from Http.Libs import DB

class BotModel:
    def __init__(self):
        self.db = DB()

    def getStat(self):
        sql = 'select * from setting where id = 1'
        result = self.db.query(sql)[0]

        return result[2]

    def setStat(self, running=True):
        if running:
            sql = 'UPDATE setting SET bot = 1 where id = 1'
        else:
            sql = 'UPDATE setting SET bot = 0 where id = 1'
        return self.db.exec(sql)
