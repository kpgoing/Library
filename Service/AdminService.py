# coding=utf-8

from ORM.DBsession import DBSession
from ORM.tableORM import Admin

__author__ = 'xbw'
class AdminService(object):

    pass
    def loginCheckByORM(self, loginAdmin):
        session = DBSession()
        try:
            checkAdmin = session.query(Admin).filter(Admin.adminname == loginAdmin.adminname).one()
            if checkAdmin.password != loginAdmin.password:
                flag = False
            else:
                flag = True
            session.close()
            return flag
        except BaseException as e:
            session.close()
            return False



    def regiter(self, admin):
        session = DBSession()
# 创建新User对象:
        try:
            checkuser = session.query(Admin).filter(Admin.adminname == user.adminname).one()
            return False
        except:
            new_admin = Admin(adminname=admin.adminname,password=admin.password)
# 添加到session:
            session.add(new_admin)
# 提交即保存到数据库:
            session.commit()
# 关闭session:
            session.close()

            return True

