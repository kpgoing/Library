# coding=utf-8
import logging

import flask
from flask import Flask, request, render_template, session,redirect,url_for

from Service.UserService import UserService
# from UserORM import User
# from BookORM import Book
from ORM.tableORM import User,Admin, Book
from Service.BookService import BookService
from util.ResponseBody import ResponseBody
# from AdminORM import Admin
from Service.AdminService import AdminService
app = Flask(__name__)
log = logging.getLogger('api')
log.setLevel(logging.DEBUG)
def initlog():
    serverst = logging.StreamHandler()
    serverch = logging.FileHandler("server.log")
    serverch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)-12s : %(name)-8s - %(funcName)s - %(levelname)-8s - %(message)s')
    serverch.setFormatter(formatter)
    serverst.setFormatter(formatter)
    log.addHandler(serverch)
    log.addHandler(serverst)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWXsd13123123/,?RTsdaffsaf'
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

#made by form
@app.route('/loginbyform', methods=['GET','POST'])
def signin():
    if request.method == 'GET':
        return  render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username,password)
        userService = UserService()
        # userDao = UserDao()
        if userService.loginCheckByORM(user):
            return render_template('books.html', username=username)
        else:
            return render_template('login.html', message='Bad username or password', username=username)
#made by ajax
@app.route('/login', methods=['POST','GET'])
def userLogin():
    if request.method == 'GET':
        if 'userid' in session:
            log.info('%s is get the /login and be redirected to /books',session['userid'])
            return redirect(url_for('userBooks'))
        else:
            return render_template('login.html')
    if request.method == 'POST':
        text = request.get_json()
        user = User(text['username'],text['password'])
        userService = UserService()
        userid = userService.loginCheckByORM(user)
        if userid != -1:
            session['userid'] = userid
            return ResponseBody(1,None).getContent()
        else:
            return  ResponseBody(0,None).getContent()

@app.route('/getusername',methods=['POST'])
def getUsername():
    if 'userid' in session:
        userService = UserService()
        data = userService.getName(session['userid'])
        return ResponseBody(1,data).getContent()

@app.route('/jump', methods=['POST'])
def userjump():
    return render_template('register.html')

@app.route('/library')
def userBooks():
    if 'userid' in session:
        return render_template('library.html')
    else:
        return flask.redirect(flask.url_for('userLogin'))

@app.route('/register', methods=['POST'])
def userRegister():
    username = request.form['username']
    password = request.form['password']
    user = User(username,password)
    userService = UserService()
    if userService.regiter(user):
        return render_template('login.html', username=username)
    else:
        return render_template('register.html',message='Bad username or password', username=username)


@app.route('/logout',methods=['POST'])
def userLogout():
    # 如果会话中有用户名就删除它。
    session.pop('userid', None)
    return redirect(url_for('userLogin'))
@app.route('/admin', methods=['POST','GET'])
def adminLogin():
    if request.method == 'GET':
        if 'adminname' in session:
            # log.info('%s is get the /login and be redirected to /books',session['username'])
            return redirect(url_for('adminBooks'))
        else:
            return render_template('adminlogin.html')
    if request.method == 'POST':
        text = request.get_json()
        admin = Admin(text['adminname'],text['password'])
        adminService = AdminService()
        if adminService.loginCheckByORM(admin):
            session['adminname'] = admin.adminname
            return ResponseBody(1,None).getContent()
        else:
            return ResponseBody(0,None).getContent()

@app.route('/library/borrow',methods=['POST'])
def borrowBook():
    data = request.get_json()
    bookService = BookService()
    flag = bookService.borrowBook(session['userid'],data['bookname'])
    myres = ResponseBody(flag,None)
    return  myres.getContent()

@app.route('/library/showborrowedbook',methods=['POST'])
def showBorrowBook():
    bookService = BookService()
    borrowBooks = bookService.getonesbooks(session['userid'])
    myres = ResponseBody(1,borrowBooks)
    return  myres.getContent()

@app.route('/library/return',methods=['POST'])
def returnBook():
    data = request.get_json()
    bookService = BookService()
    flag = bookService.returnBook(data['blid'])
    myres = ResponseBody(flag,None)
    return  myres.getContent()

@app.route('/library/reserve',methods=['POST'])
def reserveBook():
    data = request.get_json()
    bookService = BookService()
    flag = bookService.reserveBook(session['userid'],data['bookname'])
    myres = ResponseBody(flag,None)
    return  myres.getContent()

@app.route('/library/getreservedBook',methods=['POST'])
def getreservedBook():
    data = request.get_json()
    bookService = BookService()
    flag = bookService.getreservedBook(session['userid'],data['rlid'])
    myres = ResponseBody(flag,None)
    return  myres.getContent()

@app.route('/library/showreservation',methods=['POST'])
def showreserveBook():
    bookService = BookService()
    borrowBooks = bookService.getonesreservation(session['userid'])
    myres = ResponseBody(1,borrowBooks)
    return  myres.getContent()

@app.route('/admin/book')
def adminBooks():
    if 'adminname' in session:
        return render_template('books.html')
    else:
        return flask.redirect(flask.url_for('adminLogin'))
@app.route('/admin/register', methods=['POST'])
def adminRegister():
    adminname = request.form['adminname']
    password = request.form['password']
    admin = Admin(adminname,password)
    adminService = AdminService()
    if adminService.regiter(admin):
        session['adminname'] = admin.username
        return redirect(url_for('adminBooks'))
    else:
        return render_template('adminregister.html',message='Bad username or password', adminname=adminname)
@app.route('/adminjump', methods=['POST'])
def adminJump():
    return render_template('adminregister.html')


@app.route('/admin/logout',methods=['POST'])
def adminLogout():
    # 如果会话中有用户名就删除它。
    session.pop('adminname', None)
    return redirect(url_for('adminLogin'))

@app.route('/allbooks',methods=['POST','GET'])
def getAllBooks():
    bookService = BookService()
    data = bookService.getAllBooks()
    myres = ResponseBody(1,data)
    return  myres.getContent()
@app.route('/admin/addbook',methods=['POST'])
def addBook():
    data = request.get_json()
    bookService = BookService()
    book = Book(data['name'])
    bookService.addBook(book)
    return ResponseBody(1,data).getContent()
@app.route('/admin/deletebook',methods=['POST'])
def deleteBook():
    data = request.get_json()
    bookService = BookService()
    book = Book(data['name'])
    bookService.deleteBook(book)
    return ResponseBody(1,data).getContent()
if __name__ == '__main__':
    initlog()
    app.debug = True
    app.run()