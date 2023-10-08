from flask import Blueprint
from .routes import registration, login, refresh, logout

auth = Blueprint('auth', __name__, url_prefix='/auth')

auth.add_url_rule('/registration', 'registration', registration, methods=['POST'])
auth.add_url_rule('/login', 'login', login, methods=['POST'])
auth.add_url_rule('/refresh', 'refresh', refresh, methods=['POST'])
auth.add_url_rule('/logout', 'logout', logout, methods=['GET'])
# TODO Не знаю как сделать, чтобы прям в корнях лежало, пока просто тотальный реформат проекта делаю
