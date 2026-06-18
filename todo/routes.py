from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import login_required, current_user

from database.engine import db
from database.models.todo import Task


task_bp = Blueprint('tasks', __name__, template_folder='templates')


# Сделать отображение задач только для авторов этих задач

@task_bp.route('/')  # tasks/
@login_required
def get_all_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks_db=tasks)


# READ
@task_bp.route('/task/<int:id>') # tasks/task/<int:id>
@login_required
def detail_task(id):
    task = Task.query.filter_by(id=id).first() # <---
    return render_template('detail.html', task_one=task)


# CREATE
@task_bp.route('/add', methods=['GET', 'POST'])  # /tasks/add
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task(title=title, description=description, user_id=current_user.id) # <---
        db.session.add(task) # <---
        db.session.commit() # <---
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')

# UPDATE
@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_task(id):
    task = Task.query.filter_by(id=id).first() # <---
    # ---------------- POST -------------------
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title:
            task.title = title # <---
        if description:
            task.description = description # <---
        db.session.commit() # <---

    return render_template('update.html', task_one=task) # <---


# DELETE
@task_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id).first()  # <---
    db.session.delete(task) # <---
    db.session.commit() # <---
    return redirect(url_for('tasks.get_all_tasks'))

