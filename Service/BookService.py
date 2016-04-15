# coding=utf-8
from ORM import DBsession
from ORM.tableORM import Book,BorrowList,User,ReservationList
from  sqlalchemy import func
__author__ = 'xbw'
class BookService(object):

    pass

    def getAllBooks(self):
        session = DBsession.DBSession()
        try:
            books = session.query(Book).all()
            realbooks = []
            for book in books:
                a = book.getContent()
                realbooks.append(book.getContent())
            session.close()
            return realbooks
        except BaseException as e:
            print e
            session.close()
            return None

    def borrowBook(self,userid,bookname):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == bookname).one()
            checkbook.remainder = checkbook.remainder - 1
            checkbook.borrow = checkbook.borrow + 1
            borrowList = BorrowList(userid,checkbook.bid,checkbook.name)
            session.add(borrowList)
            session.commit()
            session.close()
            return 1
        except BaseException as e :
            print e
            session.close()
            return 0

    def returnBook(self,blid):
        session = DBsession.DBSession()
        try:
            checkList = session.query(BorrowList).filter(BorrowList.blid == blid).one()
            checkBook = session.query(Book).filter(Book.bid == checkList.bookid).one()

            checkBook.remainder = checkBook.remainder + 1
            checkBook.borrow = checkBook.borrow - 1
            session.delete(checkList)
            session.commit()
            session.close()
            return True
        except BaseException as e:
            session.close()
            return False

    def reservationBook(self,userid,bookname):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == bookname).one()
            checkList = session.query(func.max(BorrowList.borrow_datetime)).filter(BorrowList.rlid == checkbook.bid).one()
            if checkbook.remainder == 0 and checkbook.reservation < checkbook.count:
                checkbook.reservation = checkbook.reservation + 1
                reservationList = ReservationList(userid,checkbook.bid,checkbook.name,checkList.borrow_datetime)
                session.add(reservationList)
                session.commit()
                session.close()
                return 1
            else:
                return 0
        except BaseException as e :
            print e
            session.close()
            return 0

    def getonesreservation(self,userid):
        session = DBsession.DBSession()
        try:
            checkUser = session.query(User).filter(User.id == userid).one()
            reservationList = checkUser.reservationList
            reallist = []
            for item in reservationList:
                reallist.append(item.getContent())
            session.close()
            return reallist
        except BaseException as e:
            print e
            session.close()
            return None


    def getonesbooks(self,userid):
        session = DBsession.DBSession()
        try:
            checkUser = session.query(User).filter(User.id == userid).one()
            borrowList = checkUser.borrowList
            # borrowList = session.query(BorrowList).filter(BorrowList.userid==userid).all()
            reallist = []
            for item in borrowList:
                reallist.append(item.getContent())
            session.close()
            return reallist
        except BaseException as e:
            print e
            session.close()
            return None



    def addBook(self,book):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == book.name).one()
            checkbook.count = checkbook.count + book.count
            checkbook.remainder = checkbook.count
            session.add(checkbook)
        except BaseException as e:
            print e
            session.add(book)
        finally:
            session.commit()
            session.close()
            return True

    def deleteBook(self,book):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == book.name).one()
            checkbook.count = checkbook.count - 1
            checkbook.remainder = checkbook.borrow - 1
            if checkbook.count == 0:
                session.delete(checkbook)
            else:
                session.add(checkbook)
        except BaseException as e:
            print e
            pass
        finally:
            session.commit()
            session.close()
            return True