from flask import Flask
from todo.routes import task_bp
from auth.routes import auth_bp

from flask_login import LoginManager # <---

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


with app.app_context():
    db.create_all()


@login_manager.user_loader # <---
def load_user(user_id): # <---
    return User.query.filter_by(id=int(user_id)).first() # <---


@app.route('/')
def main():
    return '<h1> Главная страница! </h1>'


if __name__ == '__main__':
    app.run(debug=True)