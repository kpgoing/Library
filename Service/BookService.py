# coding=utf-8
from ORM import DBsession
from ORM.tableORM import Book,BorrowList,User,ReservationList
from  sqlalchemy import func, and_
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
            checkBList = session.query(BorrowList).filter(BorrowList.blid == blid).one()
            checkBook = session.query(Book).filter(Book.bid == checkBList.bookid).one()

            if checkBook.reservation > checkBook.Unclaimed:
                checkBook.Unclaimed = checkBook.Unclaimed + 1
            else:
                checkBook.remainder = checkBook.remainder + 1
            checkBook.borrow = checkBook.borrow - 1
            if checkBook.reservation > 0:
                minTime = session.query(func.min(ReservationList.reservation_datetime).label('min_time')).filter(and_(ReservationList.bookid == checkBList.bookid,ReservationList.r_status == 0)).one()
                checkRList = session.query(ReservationList).filter(ReservationList.reservation_datetime == minTime.min_time).first()
                checkRList.r_status = 1
                session.add(checkRList)
            session.delete(checkBList)
            session.add(checkBook)
            session.commit()
            session.close()
            return True
        except BaseException as e:
            print e
            session.close()
            return False

    def reserveBook(self,userid,bookname):
        session = DBsession.DBSession()
        try:
            checkbook = session.query(Book).filter(Book.name == bookname).one()
            checkList = session.query(BorrowList.borrow_datetime).filter(BorrowList.bookid == checkbook.bid).order_by(BorrowList.borrow_datetime).all()
            print checkList
            if checkbook.remainder == 0 and checkbook.reservation < checkbook.count:
                checkbook.reservation = checkbook.reservation + 1
                reservationList = ReservationList(userid,checkbook.bid,checkbook.name,checkList[checkbook.reservation_order].borrow_datetime)
                checkbook.reservation_order = checkbook.reservation_order + 1
                session.add(reservationList)
                session.add(checkbook)
                session.commit()
                session.close()
                return 1
            else:
                return 0
        except BaseException as e :
            print e
            session.close()
            return 0

    def getreservedBook(self,userid,rlid):
        session = DBsession.DBSession()
        try:
            checkRList = session.query(ReservationList).filter(ReservationList.rlid == rlid).one()
            checkBook = session.query(Book).filter(Book.bid == checkRList.bookid).one()
            checkBook.Unclaimed = checkBook.Unclaimed - 1
            checkBook.reservation = checkBook.reservation - 1
            checkBook.borrow = checkBook.borrow + 1
            checkBook.reservation_order = checkBook.reservation_order - 1
            borrowList = BorrowList(userid,checkBook.bid,checkBook.name)
            session.add(borrowList)
            session.add(checkBook)
            session.delete(checkRList)
            session.commit()
            session.close()
            return True
        except BaseException as e:
            print e
            session.close()
            return False



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