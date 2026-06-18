from flask import Flask, render_template
from todo.routes import task_bp
from auth.routes import auth_bp
from profiles.routes import profile_bp

from flask_login import LoginManager, current_user

from database.engine import db
from database.models.todo import Task
from database.models.auth import User


app = Flask(__name__)
login_manager = LoginManager() # <---

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fjadfgdhf'

db.init_app(app)
login_manager.init_app(app) # <---

app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')


with app.app_context():
    db.create_all()


@login_manager.user_loader # <---
def load_user(user_id): # <---
    return User.query.filter_by(id=int(user_id)).first() # <--- user


@app.route('/')
def main():
    return render_template('main.html', current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)