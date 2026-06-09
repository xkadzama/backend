from flask import Blueprint, render_template, request, redirect, url_for

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