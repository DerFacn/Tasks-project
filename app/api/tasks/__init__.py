from flask import Blueprint
from .routes import create_task, get_task, delete_task

from app.misc.config import Config


tasks = Blueprint('tasks', __name__, url_prefix='/tasks', template_folder=Config.TEMPLATE_ABS)

tasks.add_url_rule('/create', 'create', create_task, methods=['POST'])
tasks.add_url_rule('/get', 'get', get_task, methods=['GET'])
tasks.add_url_rule('/delete', 'delete', delete_task, methods=['POST'])
