from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, \
    unset_jwt_cookies, jwt_required


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({'message': 'Username already exists!'})

    user = User(
        public_id=str(uuid4()),
        username=username,
        password=generate_password_hash(password),
        admin=False,
    )
    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity=user.public_id)
    refresh_token = create_refresh_token(identity=user.public_id)

    response = jsonify('User created!')

    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found!'}), 401
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Wrong password'}), 401

    access_token = create_access_token(identity=user.public_id)
    refresh_token = create_refresh_token(identity=user.public_id)
    response = jsonify('Login success!')
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response, 201


@bp.route('/logout', methods=['GET', 'POST'])
@jwt_required()
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200
