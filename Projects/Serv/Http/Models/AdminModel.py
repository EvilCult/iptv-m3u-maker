# pyright: reportMissingModuleSource=false
import hashlib
from Http.Libs import DB

class AdminModel(DB):
    table_name = 'admin'

    def findById(self, id):
        return self.find(id)

    def login(self, uname, pwd):
        pwd = pwd + 'ishouldaddsthhere'
        pwd = hashlib.sha256(pwd.encode()).hexdigest()

        admin = self.where(uname=uname, pwd=pwd)
        return admin[0] if len(admin) > 0 else None
