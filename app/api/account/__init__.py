from flask import Blueprint
from .routes import info

from app.misc.config import Config


account = Blueprint('account', __name__, url_prefix='/account', template_folder=Config.TEMPLATE_ABS)

account.add_url_rule('/info', 'info', info, methods=['GET'])
