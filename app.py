from flask import Flask, render_template, redirect, url_for, request
import psycopg2

app = Flask(__name__)

# 初期画面
@app.route('/')
def book_index():
    return render_template('index.html')
# 新規登録
@app.route('/user_register')
def user_register():
    return render_template('user-register.html')


# ログイン
@app.route('/login-form')
def login_form():
    return render_template('login-form.html')

@app.route('/login')
def login():
    mail = request.form.get('mail')
    pw = request.form.get('pw')
    return render_template('login.html', mail = mail, pw = pw)


if __name__ == '__main__':
    app.run(debug = True)