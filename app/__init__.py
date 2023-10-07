import os
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = 'sqlite:///instance/app.db'
jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": []}})
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

if not os.path.exists('./instance/'):
    os.mkdir('./instance/')

from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(db)
Base.metadata.create_all(bind=engine)
session = scoped_session(sessionmaker(autoflush=False, bind=engine))
Base.session = session.query_property()


@app.teardown_appcontext
def shutdown_session(extension: None):
    session.remove()


from app import (
    auth,
    account,
    todo,
)

app.register_blueprint(auth.bp)
app.register_blueprint(account.bp)
app.register_blueprint(todo.bp)
