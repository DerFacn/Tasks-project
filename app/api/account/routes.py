from flask import jsonify
from app.misc.models import User
from app.api import session
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity


@cross_origin()
@jwt_required()
def info():
    user_id = get_jwt_identity()
    user = session.query(User).filter_by(uuid=user_id).first()
    username = user.username
    passwd = user.password
    
    return jsonify([username, passwd])
