from flask import Blueprint
from .routes import create_todo, complete_todo, delete_todo

todo = Blueprint('/todo', __name__, url_prefix='/todo')

todo.add_url_rule('/create', 'create', create_todo, methods=['POST'])
todo.add_url_rule('/complete/<todo_id>', 'complete', complete_todo, methods=['PUT'])
todo.add_url_rule('/delete/<todo_id>', 'delete', delete_todo, methods=['DELETE'])
