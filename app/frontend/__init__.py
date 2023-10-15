from flask import Blueprint
from .router import *
from .account import account

from app.misc.config import Config


frontend = Blueprint('index', __name__, url_prefix='/', template_folder=Config.TEMPLATE_ABS)

frontend.add_url_rule('/registration', 'registration', registration, methods=['GET'])
frontend.add_url_rule('/login', 'login', login, methods=['GET'])
frontend.add_url_rule('/logout', 'logout', logout, methods=['GET'])

frontend.add_url_rule('/', 'start_page', start_page, methods=['GET'])
frontend.add_url_rule('/index', 'start_page', start_page, methods=['GET'])
frontend.add_url_rule('/index.html', 'start_page', start_page, methods=['GET'])

frontend.register_blueprint(account)