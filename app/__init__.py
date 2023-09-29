from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import click
from flask_jwt_extended import JWTManager


basedir = os.path.abspath(os.path.dirname(__file__))  # Database path
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['JWT_SECRET_KEY'] = 'secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

from app.models import User, Todo


@click.command('create-db')
def create_db():
    with app.app_context():
        db.create_all()
    click.echo('Database created!')


app.cli.add_command(create_db)


from app import auth
app.register_blueprint(auth.bp)
