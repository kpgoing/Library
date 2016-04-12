# coding=utf-8
__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Admin(Base):
    # 表的名字:
    __tablename__ = 'admin'

    def __init__(self,adminname,password):
        self.adminname = adminname
        self.password = password

    # 表的结构:
    id = Column(Integer, primary_key=True,autoincrement=True)
    adminname = Column(String(20))
    password = Column(String(20))
