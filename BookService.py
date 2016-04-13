# coding=utf-8
from tableORM import Book,BorrowList,User
import DBsession
from sqlalchemy import and_
__author__ = 'xbw'
class BookService(object):

    pass

    def getAllBooks(self):
        session = DBsession.DBSession()
        try:
            books = session.query(Book).all()
            realbooks = []
            for book in books:
                realbooks.append(book.getContent())
            session.close()
            return realbooks
        except:
            session.close()
            return None

    def borrowBook(self,userid,bookname):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book.name == bookname).one()
            checkuser = session.query(User.id == userid).one()
            checkbook.remainder = checkbook.remainder - 1
            checkbook.borrow = checkbook.borrow + 1
            borrowList = BorrowList(userid,checkbook.id)
            return 1
        except:
            session.close()
            return 0

    def returnBook(self,userid,bookname):
        session = DBsession.DBSession()
        try:
            checkBook = session.query(Book.name == bookname).one()
            checkUser = session.query(User.id == userid).one()
            checkList = session.query(BorrowList).filter_by(and_(BorrowList.userid==userid,BorrowList.bookid==checkBook.bid)).all()

            checkBook.remainder = checkBook.remainder + 1
            checkBook.borrow = checkBook.borrow - 1
            session.delete(checkList)
            session.commit()
            session.close()
            return True
        except:
            session.close()
            return False

    def getonesbooks(self,userid):
        session = DBsession.DBSession()
        try:
            checkUser = session.query(User.id == userid).one()
            borrowList = checkUser.borrowList
            reallist = []
            for item in borrowList:
                reallist.append(item.getContent())
            session.close()
            return reallist
        except:
            session.close()
            return None



    def addBook(self,book):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == book.name).one()
            checkbook.count = checkbook.count + book.count
            checkbook.remainder = checkbook.count
            session.add(checkbook)
        except:
            session.add(book)
        finally:
            session.commit()
            session.close()
            return True

    def deleteBook(self,book):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == book.name).one()
            checkbook.count = checkbook.count - book.count
            if checkbook.count == 0:
                session.delete(checkbook)
            else:
                session.add(checkbook)
        except:
            pass
        finally:
            session.commit()
            session.close()
            return True