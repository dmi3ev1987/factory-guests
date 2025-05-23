import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    MIGRATIONS_DIR = os.getenv('MIGRATIONS_DIR')
