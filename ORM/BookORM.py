# coding=utf-8
__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer ,DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Book(Base):
    # 表的名字:
    __tablename__ = 'books'

    def __init__(self,name,count=1):
        self.name = name
        self.count = count
        self.remainder = count
    def getContent(self):
        return {"name":self.name,"count":self.count,'remainder':self.remainder,'borrow':self.borrow,'reservation':self.reservation,'borrow_datetime':self.borrow_datetime,'reservation_datetime':self.reservation_datetime}

    # 表的结构:
    bid = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(45))
    count = Column(Integer,default=1)
    remainder = Column(Integer,default=1)
    borrow = Column(Integer,default=0)
    reservation = Column(Integer,default=0)

    ownerid = Column(Integer, ForeignKey('test.user.id'))