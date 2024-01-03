# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class AdminModel(DB):
    table_name = 'admin'

    def findById(self, id):
        return self.select(id=id, isdel=0).fetch()

    def login(self, uname, pwd):
        pwd = pwd + 'ishouldaddsthhere'
        pwd = hashlib.sha256(pwd.encode()).hexdigest()

        admin = self.select(uname=uname, pwd=pwd).fetch()
        return admin[0] if len(admin) > 0 else None

    def update(self, **kwargs):
        self.save(**kwargs)
