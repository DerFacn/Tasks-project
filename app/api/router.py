from flask import Blueprint
from .account import account
from .auth import auth
from .todo import todo

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(account)
api.register_blueprint(auth)
api.register_blueprint(todo)
