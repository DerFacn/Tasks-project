from flask import render_template, make_response, url_for, redirect
from flask_jwt_extended import (
    jwt_required,
    unset_jwt_cookies, 
    get_jwt_identity
)

def registration():
    return render_template('registration.html')

def login():
    return render_template('login.html')

# @jwt_required()
def logout():
    response = redirect(url_for('index.start_page'))
    unset_jwt_cookies(response)

    return response

@jwt_required(optional=True)
def start_page():
    #если не вошёл или токен не валид
    if get_jwt_identity() is None:
        return render_template('login.html')
    
    #если есть и валид
    return render_template('/auth_required/main.html')