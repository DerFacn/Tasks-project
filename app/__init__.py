import os
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_jwt_extended import JWTManager
from app.misc.config import Config


app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": []}})
csrf = CSRFProtect(app)

from app.misc import jwt_exceptions_handler


if not os.path.exists('./alchemy-db'):
    os.makedirs('./alchemy-db')

from app.misc.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    'sqlite:///./alchemy-db/app.db'
)

Base.metadata.create_all(bind=engine)
session = scoped_session(sessionmaker(autoflush=False, bind=engine))
Base.session = session.query_property()


@app.teardown_appcontext
def shutdown_session(e=None):
    session.remove()


#импорт копонентов сайта
from .api.router import api
from .frontend import frontend

app.register_blueprint(api)
app.register_blueprint(frontend)