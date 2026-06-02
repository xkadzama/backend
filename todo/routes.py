from flask import Blueprint, render_template, request, redirect, url_for

from database.engine import db
from database.models.todo import Task


task_bp = Blueprint('tasks', __name__, template_folder='templates')


# READ
@task_bp.route('/')  # tasks/
def get_all_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks_db=tasks)


# READ
@task_bp.route('/task/<int:id>') # tasks/task/<int:id>
def detail_task(id):
    task = Task.query.filter_by(id=id).first() # <---
    return render_template('detail.html', task_one=task)


# CREATE
@task_bp.route('/add', methods=['GET', 'POST'])  # /tasks/add
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task(title=title, description=description) # <---
        db.session.add(task) # <---
        db.session.commit() # <---
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')

# UPDATE
@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
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
def delete_task(id):
    task = Task.query.filter_by(id=id).first()  # <---
    db.session.delete(task) # <---
    db.session.commit() # <---
    return redirect(url_for('tasks.get_all_tasks'))

