from flask import Blueprint

frontend = Blueprint('index', __name__, url_prefix='/')

# frontend.register_blueprint()