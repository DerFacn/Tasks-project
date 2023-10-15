from flask import Blueprint
from .routes import registration, login, refresh, logout

from app.misc.config import Config


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder=Config.TEMPLATE_ABS)

auth.add_url_rule('/registration', 'registration', registration, methods=['POST'])
auth.add_url_rule('/login', 'login', login, methods=['POST'])
auth.add_url_rule('/refresh', 'refresh', refresh, methods=['GET', 'POST'])
auth.add_url_rule('/logout', 'logout', logout, methods=['GET'])