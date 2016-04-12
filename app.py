# coding=utf-8
import logging
import flask
from flask import Flask, request, render_template, session,redirect,url_for
from UserService import UserService
from UserORM import User
from BooksORM import Book
from BookService import BookService
from ResponseBody import ResponseBody
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
def signin2():
    if request.method == 'GET':
        if 'username' in session:
            log.info('%s is get the /login2 and be redirected to /books',session['username'])
            return redirect(url_for('books'))
        else:
            return render_template('login2.html')
    if request.method == 'POST':
        text = request.get_json()
        user = User(text['username'],text['password'])
        userService = UserService()
        if userService.loginCheckByORM(user):
            session['username'] = user.username
            return ResponseBody(1,None).getContent()
        else:
            return render_template('login.html', message='Bad username or password', username=text.username)
# @app.route('/admin', methods=['POST','GET'])
# def signin2():
#     if request.method == 'GET':
#         if 'admin' in session:
#             # log.info('%s is get the /login2 and be redirected to /books',session['username'])
#             return redirect(url_for('/admin/managerbooks'))
#         else:
#             return render_template('admin.html')
#     if request.method == 'POST':
#         text = request.get_json()
#         user = User(text['admin'],text['password'])
#         adminService = AdminService()
#         if userService.loginCheckByORM(user):
#             session['username'] = user.username
#             return ResponseBody(1,None).getContent()
#         else:
#             return render_template('login.html', message='Bad username or password', username=text.username)
@app.route('/jump', methods=['POST'])
def jump():
    return render_template('register.html')

@app.route('/book')
def books():
    if 'username' in session:
        return render_template('books.html')
    else:
        return flask.redirect(flask.url_for('signin2'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User(username,password)
    userService = UserService()
    if userService.regiter(user):
        return render_template('login2.html', username=username)
    else:
        return render_template('register.html',message='Bad username or password', username=username)


@app.route('/book/allbooks',methods=['POST','GET'])
def getAllBooks():
    bookService = BookService()
    data = bookService.getAllBooks()
    myres = ResponseBody(1,data)
    return  myres.getContent()
@app.route('/book/addbook',methods=['POST'])
def addBook():
    data = request.get_json()
    bookService = BookService()
    book = Book(data['name'])
    bookService.addBook(book)
    return ResponseBody(1,data).getContent()
@app.route('/book/deletebook',methods=['POST'])
def deleteBook():
    data = request.get_json()
    bookService = BookService()
    book = Book(data['name'])
    bookService.deleteBook(book)
    return ResponseBody(1,data).getContent()
@app.route('/logout',methods=['POST'])
def logout():
    # 如果会话中有用户名就删除它。
    session.pop('username', None)
    return redirect(url_for('signin2'))
if __name__ == '__main__':
    initlog()
    app.run()