from flask import Blueprint, render_template


task_bp = Blueprint('tasks', __name__, template_folder='templates')

tasks_db = [
    {'id': 1, 'title': 'Купить хлеб', 'description': 'Успеть до закрытия'},
    {'id': 2, 'title': 'Заменить масло', 'description': 'Заехать в СТО'},
    {'id': 3, 'title': 'Выполнить ДЗ', 'description': 'До след. урок'},
    {'id': 4, 'title': 'Реализовать CRUD', 'description': 'Дедлайн до завтра'}
]

# CRUD - CREATE READ UPDATE DELETE

# READ
@task_bp.route('/')  # tasks/
def get_all_tasks():
    return render_template('tasks.html', tasks_db=tasks_db)


# READ
@task_bp.route('/task/<int:id>') # tasks/task/<int:id>
def detail_task(id):
    task_one = []
    for task in tasks_db:
        if task.get('id') == id:
            task_one.append(task)
    return render_template('detail.html', task_one=task_one)




