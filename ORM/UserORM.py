# coding=utf-8
__author__ = 'xbw'
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from BookORM import Book
from BorrowListORM import BorrowList
# 创建对象的基类:
Base = declarative_base()

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

    books = relationship(Book)
    borrowList = relationship("Borrowlist")
