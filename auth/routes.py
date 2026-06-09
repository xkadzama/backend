from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import login_user, logout_user

from database.models.auth import User
from database.engine import db

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(username=username,  email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))

    return render_template('register.html')



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password') # 12345
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('tasks.get_all_tasks'))
        else:
            print('Неправильный логин или пароль')

    return render_template('login.html')


@auth_bp.route('/logout') # /auth/logout
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

