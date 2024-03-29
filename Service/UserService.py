# coding=utf-8
from ORM.DBsession import DBSession
from ORM.tableORM import User
from UserDao import UserDao

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
                flag = -1
            else:
                flag = checkuser.id
            session.close()
            return flag
        except BaseException as e:
            print e
            session.close()
            return -1

    def getName(self,userid):
        session = DBSession()
        try:
            checkUser = session.query(User.username).filter(User.id == userid).one()
            return checkUser.username
        except BaseException as e:
            print e
            return None


    def regiter(self, user):
        session = DBSession()
# 创建新User对象:
        try:
            checkuser = session.query(User).filter(User.username == user.username).one()
            return False
        except BaseException as e:
            new_user = User(username=user.username,password=user.password)
# 添加到session:
            session.add(new_user)
# 提交即保存到数据库:
            session.commit()
# 关闭session:
            session.close()

            return True

