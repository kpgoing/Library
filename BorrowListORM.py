# coding=utf-8
__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer ,DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class BorrowList(Base):
    # 表的名字:
    __tablename__ = 'borrowlist'

    def __init__(self,userid,bookid):
        self.userid = userid
        self.bookid = bookid
        self.borrow_datetime = datetime.datetime.now()
    def getContent(self):
        return {"blid":self.blid,"userid":self.userid,'bookid':self.bookid,'borrow_datetime':self.borrow_datetime}

    # 表的结构:
    blid = Column(Integer, primary_key=True,autoincrement=True)
    userid = Column(Integer, ForeignKey('user.id'))
    bookid = Column(Integer, ForeignKey('book.bid'))
    borrow_datetime = Column(DateTime)
    # reservation_datetime = Column(DateTime)
