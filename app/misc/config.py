class Config(object):
    SECRET_KEY = 'flask_secret_key_here'
    JWT_SECRET_KEY = 'jwt_secret_key_here'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SECURE = True