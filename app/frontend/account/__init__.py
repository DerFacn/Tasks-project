from flask import Blueprint
from .routes import info

account = Blueprint('account', __name__, url_prefix='/account')

account.add_url_rule('/info', 'info', info, methods=['GET'])
