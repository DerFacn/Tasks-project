from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import cross_origin
from app.utils import response_json
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, \
    unset_jwt_cookies, jwt_required


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.get_json()

    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()

    if user is not None:
        return response_json('Username already exists!', 201)

    user = User(
        uuid=str(uuid4()),
        username=username,
        password=generate_password_hash(password),
    )

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user.uuid)
    refresh_token = create_refresh_token(identity=user.uuid)

    response = response_json('User created!', 200)

    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response


@bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if not user:
        return response_json('User not found!', 401)
    
    if not check_password_hash(user.password, password):
        return response_json('Wrong password', 401)

    access_token = create_access_token(identity=user.uuid)
    refresh_token = create_refresh_token(identity=user.uuid)
    
    response = response_json('Login success!', 200)
    
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response


@bp.route('/logout', methods=['GET', 'POST'])
@cross_origin()
@jwt_required()
def logout():
    response = response_json('success', 200)
    unset_jwt_cookies(response)
    
    return response
