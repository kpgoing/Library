# coding=utf-8
from UserDao import UserDao
import UserORM
from UserORM import User
from DBsession import DBSession
__author__ = 'xbw'
class UserService(object):

    pass

    def logincheck(self , user):
        userdao = UserDao()
        print userdao.findByName(user.username)
        if user.password == userdao.findByName(user.username)[2]:
            return True
        else:
            return False

    def loginCheckByORM(self, loginUser):
        session = DBSession()
        try:
            checkuser = session.query(User).filter(User.username == loginUser.username).one()
            print checkuser.username
            if checkuser.password != loginUser.password:
                flag = False
            else:
                flag = True
            session.close()
            return flag
        except:
            session.close()
            return False



    def regiter(self, user):
        session = DBSession()
# 创建新User对象:
        try:
            checkuser = session.query(UserORM.User).filter(UserORM.User.username == user.username).one()
            return False
        except:
            new_user = UserORM.User(username=user.username,password=user.password)
# 添加到session:
            session.add(new_user)
# 提交即保存到数据库:
            session.commit()
# 关闭session:
            session.close()

            return True

