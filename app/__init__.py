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


from .api.router import api
app.register_blueprint(api)
