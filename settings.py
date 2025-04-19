import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH')
