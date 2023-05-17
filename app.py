from flask import Flask, render_template, redirect, url_for, request, session
from methods import get_user, get_videos, get_video, check_email, check_login, check_name
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] ='SECRET_KEY'

conn = sqlite3.connect('db.sqlite', check_same_thread=False)
cursor = conn.cursor()


# 首頁
@app.route('/')
def home():
    videos = get_videos()
    return render_template('home.html', videos = videos)
# 登入
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.values['email']
        pwd = request.values['pwd']
        print(email,pwd)
        if check_login(email,pwd):
            session['user'] = get_user(email)
            session['email'] = email
            return redirect(url_for('home'))
        else:
            error = '信箱或密碼錯誤!'
            print(error)
        return render_template('login.html',error = error)
    return render_template('login.html', error = error)
##########################################################
# 註冊
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = False
    if request.method == 'POST':
        email = request.values['email']
        name = request.values['name']
        pwd = request.values['pwd']
        che_pwd = request.values['che_pwd']
        print(email,name,pwd,che_pwd)
        if check_email(email):
            if check_name(name):
                if che_pwd == pwd:
                    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, pwd))
                else:
                    error = '密碼錯誤!'
            else:
                error = '名字已註冊'
        else:
            error = '信箱已註冊!'
            print(error)
        return render_template('register.html',error = error)
    return render_template('register.html',error = error)
# 用戶
@app.route('/author/<string:user>')
def author(user):
    user
    return render_template('author.html', user = user)
# 影片
@app.route('/video/<int:video_id>')
def video(video_id):
    video = get_video(video_id)
    print(video)
    return render_template('video.html', video = video)
# 登出
@app.route('/logout')
def logout():
    session.pop('email')
    session.pop('user')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=5500)