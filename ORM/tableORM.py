# coding=utf-8
import datetime

__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer,DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()



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


class Book(Base):
    # 表的名字:
    __tablename__ = 'book'

    def __init__(self,name,count=1):
        self.name = name
        self.count = count
        self.remainder = count
    def getContent(self):
        return {"bid":self.bid,"name":self.name,"count":self.count,'remainder':self.remainder,'borrow':self.borrow,'reservation':self.reservation,'Unclaimed':self.Unclaimed}

    # 表的结构:
    bid = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(45))
    count = Column(Integer,default=1)
    remainder = Column(Integer,default=1)
    borrow = Column(Integer,default=0)
    reservation = Column(Integer,default=0)
    Unclaimed = Column(Integer,default=0)
    reservation_order = Column(Integer,default=0)

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
        return {"blid":self.blid,"userid":self.userid,'bookid':self.bookid,'bookname':self.bookname,'borrow_datetime':self.borrow_datetime.strftime("%Y-%m-%d %H:%M:%S"),'return_datetime':(self.borrow_datetime + datetime.timedelta(days=45)).strftime("%Y-%m-%d %H:%M:%S")}

    blid = Column(Integer, primary_key=True,autoincrement=True)
    userid = Column(Integer, ForeignKey('user.id'))
    bookid = Column(Integer, ForeignKey('book.bid'))
    bookname = Column(String(45))
    borrow_datetime = Column(DateTime)

class ReservationList(Base):
    # 表的名字:
    __tablename__ = 'reservationlist'

    def __init__(self,userid,bookid,bookname,last_keep_datetime,r_status=0):
        self.userid = userid
        self.bookid = bookid
        self.bookname = bookname
        self.reservation_datetime = datetime.datetime.now()
        self.last_keep_datetime = last_keep_datetime + datetime.timedelta(days=55)
        self.r_status = r_status
    def getContent(self):
        return {"rlid":self.rlid,'bookid':self.bookid,'bookname':self.bookname,'reservation_datetime':self.reservation_datetime.strftime("%Y-%m-%d %H:%M:%S"),'last_keep_datetime':self.last_keep_datetime.strftime("%Y-%m-%d %H:%M:%S"),'r_status':self.r_status}

    # 表的结构:
    rlid = Column(Integer, primary_key=True,autoincrement=True)
    userid = Column(Integer, ForeignKey('user.id'))
    bookid = Column(Integer, ForeignKey('book.bid'))
    bookname = Column(String(45))
    reservation_datetime = Column(DateTime)
    last_keep_datetime = Column(DateTime)
    r_status = Column(Integer,default=0)
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

    borrowList = relationship("BorrowList")
    reservationList = relationship("ReservationList")