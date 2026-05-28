from flask import Flask
from todo.routes import task_bp

from database.engine import db
from database.models.todo import Task

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()


app.register_blueprint(task_bp, url_prefix='/tasks')

@app.route('/')
def main():
    return '<h1> Главная страница! </h1>'


if __name__ == '__main__':
    app.run(debug=True)