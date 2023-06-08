from flask import Blueprint, render_template, request
import db

user_bp = Blueprint('user', __name__, url_prefix='/user')

# user新規登録
@user_bp.route('/user_register')
def user_register():
    return render_template('user/user-register.html')

@user_bp.route('/user_register_exe', methods=['POST'])
def register_exe():
    name = request.form.get('name')
    mail = request.form.get('mail')
    pw = request.form.get('pw')
    
    db.insert_user(name, mail, pw)

# ログイン
@user_bp.route('/login-form')
def login_form():
    return render_template('user/login-form.html')

@user_bp.route('/login')
def login():
    mail = request.form.get('mail')
    pw = request.form.get('pw')
    return render_template('user/login.html', mail = mail, pw = pw)