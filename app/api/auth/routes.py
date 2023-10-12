from flask import request, make_response
from app.misc.models import User
from app import session
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, \
    get_jwt_identity


def registration():

    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        return {'message': 'Username is required!'}, 422
    elif not password:
        return {'message': 'Password is required!'}, 422
    
    # Check if user already exist
    user = session.query(User).filter_by(username=username).first()
    if user is not None:
        return {'message': 'User already exist!'}, 409
    
    # Creating new user
    user = User(
        uuid=str(uuid4()),
        username=username,
        password=generate_password_hash(password),
    )
    # Add and send our new user to the database
    session.add(user)
    session.commit()
    # Create tokens
    access_token = create_access_token(identity=user.uuid)
    refresh_token = create_refresh_token(identity=user.uuid)

    response = make_response('User created!', 200)

    response.set_cookie('access_token_cookie', access_token, secure=True, httponly=True, path='/')
    response.set_cookie('refresh_token_cookie', refresh_token, secure=True, httponly=True, 
                        path='/auth/refresh')

    return response


def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = session.query(User).filter_by(username=username).first()

    if not user:
        return {'message': 'User with this username don\'t exists!'}, 401
    
    if not check_password_hash(user.password, password):
        return {'message': 'Wrong password!'}, 401

    access_token = create_access_token(identity=user.uuid)
    refresh_token = create_refresh_token(identity=user.uuid)
    
    response = make_response('Login success!', 200)
    
    response.set_cookie('access_token_cookie', access_token, secure=True, httponly=True, path='/')
    response.set_cookie('refresh_token_cookie', refresh_token, secure=True, httponly=True, 
                        path='/auth/refresh')

    return response



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



@jwt_required()
def logout():
    response = make_response()
    unset_jwt_cookies(response)

    return response
