# coding=utf-8
from BooksORM import Book
import DBsession
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

    def addBook(self,book):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == book.name).one()
            checkbook.count = checkbook.count + book.count
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