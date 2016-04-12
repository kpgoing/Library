# coding=utf-8
__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer
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

    def getContent(self):
        return {"name":self.name,"count":self.count}
    # 表的结构:
    Bid = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(45))
    count = Column(Integer)
