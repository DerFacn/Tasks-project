from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, \
    unset_jwt_cookies, jwt_required, get_jwt_identity
from flask import render_template, make_response

bp = Blueprint('account', __name__, url_prefix='/account')

@bp.route('/info', methods=['GET', 'POST'])
@cross_origin()
@jwt_required()
def info():
    user_id = get_jwt_identity()
    user_data = User.query.filter_by(uuid=user_id).one_or_none()
    username = user_data.username
    passwd = user_data.password
    
    return jsonify([username, passwd])