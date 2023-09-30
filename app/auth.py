from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, \
    unset_jwt_cookies, jwt_required, get_jwt_identity
from flask import render_template, make_response

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/registration', methods=['GET', 'POST'])
@cross_origin()
def registration():
    if request.method == 'GET':
        return render_template('registration.html')

    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user is not None:
        return make_response('Username already exists!', 201)

    user = User(
        uuid=str(uuid4()),
        username=username,
        password=generate_password_hash(password),
    )

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user.uuid)
    refresh_token = create_refresh_token(identity=user.uuid)

    response = make_response('User created!', 200)

    response.set_cookie('access_token_cookie', access_token, secure=True, httponly=True, path='/')
    response.set_cookie('refresh_token_cookie', refresh_token, secure=True, httponly=True, 
                        path='/auth/refresh')

    return response


@bp.route('/login', methods=['GET', 'POST'])
@cross_origin()
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if not user:
        return make_response('User not found!', 401)
    
    if not check_password_hash(user.password, password):
        return make_response('Wrong password', 401)

    access_token = create_access_token(identity=user.uuid)
    refresh_token = create_refresh_token(identity=user.uuid)
    
    response = make_response('Login success!', 200)
    
    response.set_cookie('access_token_cookie', access_token, secure=True, httponly=True, path='/')
    response.set_cookie('refresh_token_cookie', refresh_token, secure=True, httponly=True, 
                        path='/auth/refresh')

    return response

@bp.route('/refresh', methods=['POST'])
@cross_origin()
@jwt_required()
def refresh():
    user_identity = get_jwt_identity()

    access_token = create_access_token(identity=user_identity)
    refresh_token = create_refresh_token(identity=user_identity)

    response = make_response('', 200)

    response.set_cookie('access_token_cookie', access_token, secure=True, httponly=True, path='/')
    response.set_cookie('refresh_token_cookie', refresh_token, secure=True, httponly=True, 
                        path='/auth/refresh')
    
    return response

@bp.route('/logout', methods=['GET', 'POST'])
@cross_origin()
@jwt_required()
def logout():
    response = make_response()
    unset_jwt_cookies(response)

    return response
