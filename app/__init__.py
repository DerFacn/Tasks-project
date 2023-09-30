from os.path import abspath, dirname
from os.path import exists as file_exists

from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


basedir = abspath(dirname(__file__))  # Database path
app = Flask(__name__)

cors = cors = CORS(app, resources={r"/*": {"origins": "*"}})
csrf = CSRFProtect(app)

# cors.cross_origin(
# origins = '*', 
# methods = ['GET', 'POST'],
# headers = None, 
# supports_credentials = False, 
# max_age = None, 
# send_wildcard = True, 
# always_send = True, 
# automatic_options = False
# )

db_filename = 'app.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['JWT_SECRET_KEY'] = 'secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

from app.models import User, Todo

if not file_exists('./instance/' + db_filename):
    with app.app_context():
        db.create_all()
        print('\nDATABASE INITIALIZED\n')


from app import auth
from app import todo

app.register_blueprint(auth.bp)
app.register_blueprint(todo.bp)