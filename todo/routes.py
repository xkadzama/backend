# from aiogram import Router
from flask import Blueprint


# admin = Router()
task_bp = Blueprint('tasks', __name__, template_folder='templates')

@task_bp.route('/all_tasks') # 127.0.0.1:5000/all_tasks
def get_all_tasks():
    return 'Все задачи!'

