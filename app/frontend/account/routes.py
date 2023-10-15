from flask import jsonify, render_template
from app.misc.models import User
from app import session
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def info():

    id = get_jwt_identity()

    return render_template('/auth_required/account/info.html', id=id)
