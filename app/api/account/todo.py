from flask import Blueprint, request
from app import session
from app.misc.models import Todo


bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/create', methods=['POST'])
def create_todo():
    return ''


@bp.route('/complete/<todo_id>', methods=['PUT'])
def complete_todo():
    return ''


@bp.route('/delete/<todo_id>', methods=['DELETE'])
def delete_todo():
    return ''
