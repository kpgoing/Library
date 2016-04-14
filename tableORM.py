# coding=utf-8
import datetime

__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer,DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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


# 定义User对象:
class Book(Base):
    # 表的名字:
    __tablename__ = 'book'

    def __init__(self,name,count=1):
        self.name = name
        self.count = count
        self.remainder = count
    def getContent(self):
        return {"name":self.name,"count":self.count,'remainder':self.remainder,'borrow':self.borrow,'reservation':self.reservation}

    # 表的结构:
    bid = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(45))
    count = Column(Integer,default=1)
    remainder = Column(Integer,default=1)
    borrow = Column(Integer,default=0)
    reservation = Column(Integer,default=0)

    ownerid = Column(Integer, ForeignKey('user.id'))

# 定义User对象:
class BorrowList(Base):
    # 表的名字:
    __tablename__ = 'borrowlist'

    def __init__(self,userid,bookid,bookname):
        self.userid = userid
        self.bookid = bookid
        self.bookname = bookname
        self.borrow_datetime = datetime.datetime.now()
    def getContent(self):
        return {"blid":self.blid,"userid":self.userid,'bookid':self.bookid,'bookname':self.bookname,'borrow_datetime':self.borrow_datetime}

    # 表的结构:
    blid = Column(Integer, primary_key=True,autoincrement=True)
    userid = Column(Integer, ForeignKey('user.id'))
    bookid = Column(Integer, ForeignKey('book.bid'))
    bookname = Column(String(45))
    borrow_datetime = Column(DateTime)
    # reservation_datetime = Column(DateTime)
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    def __init__(self,username,password):
        self.username = username
        self.password = password

    # 表的结构:
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(20))
    password = Column(String(20))

    books = relationship("Book")
    borrowList = relationship("BorrowList")