import time
from Http.Libs import DB

class LogModel:
    def __init__(self):
        self.db = DB()

    def add(self, msg, typ = 'info'):
        sql = (
            'INSERT INTO "log" '
            '("typ", "msg", "udtime") '
            'VALUES (?, ?, ?)'
        )

        values = (
            typ,
            msg,
            int(time.time())
        )
        result = self.db.exec(sql, values)

        return result

    def get(self, count):
        sql = 'SELECT * FROM log ORDER BY udtime LIMIT %s' % (count)

        return self.db.query(sql)
