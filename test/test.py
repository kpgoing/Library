# coding=utf-8
from ORM import UserORM

__author__ = 'xbw'
session = UserORM.DBSession()
# 创建新User对象:
new_user = UserORM.User(username='Bobb', password='123')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()