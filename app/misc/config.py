from os.path import abspath

class Config(object):
    SECRET_KEY = 'flask_secret_key_here'
    JWT_SECRET_KEY = 'jwt_secret_key_here'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SECURE = True
    
    SEND_FILE_MAX_AGE_DEFAULT = 1
    TEMPLATE_ABS = abspath('../frontend/templates')