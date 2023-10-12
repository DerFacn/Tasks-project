from flask import jsonify
from app.misc.models import User
from app import session
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def info():
    pass
