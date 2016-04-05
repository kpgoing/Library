from flask import Flask, request, render_template
from UserService import UserService
from UserORM import User
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def signin_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    user = User(username,password)
    userService = UserService()
    # userDao = UserDao()
    if userService.loginCheckByORM(user):
        return render_template('signin-ok.html', username=username)
    else:
        return render_template('login.html', message='Bad username or password', username=username)

@app.route('/jump', methods=['POST'])
def jump():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User(username,password)
    userService = UserService()
    if userService.regiter(user):
        return render_template('login.html', username=username)
    else:
        return render_template('register.html',message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()