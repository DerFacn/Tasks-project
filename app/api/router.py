from flask import Blueprint
from .account import account
from .auth import auth
from .tasks import tasks

from app.misc.config import Config


api = Blueprint('api', __name__, url_prefix='/api', template_folder=Config.TEMPLATE_ABS)

api.register_blueprint(account)
api.register_blueprint(auth)
api.register_blueprint(tasks)
