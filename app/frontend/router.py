from flask import render_template, make_response, url_for
from flask_jwt_extended import jwt_required, unset_jwt_cookies

def registration():
    return render_template('registration.html')

def login():
    return render_template('login.html')

@jwt_required()
def logout():
    response = make_response()
    unset_jwt_cookies(response)

    response['Location'] = url_for('index')
    return response, 302