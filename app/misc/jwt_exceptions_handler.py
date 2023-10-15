from app import jwt as JWTManager
from flask import redirect, url_for, request

@JWTManager.expired_token_loader
@JWTManager.expired_token_loader
def redirect_to_refresh(*args):
    return redirect(url_for('api.auth.refresh')+f'?redirect-to={request.path}')