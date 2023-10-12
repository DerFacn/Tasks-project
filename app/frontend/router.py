from flask import render_template, redirect, url_for
from flask_jwt_extended import jwt_required

def registration():
    return render_template('registration.html')

def login():
    return render_template('login.html')

@jwt_required()
def logout():
    return redirect(url_for('api.auth.logout'))