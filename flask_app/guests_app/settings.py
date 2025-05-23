import os
from urllib.parse import quote_plus

from guests_app.constants import VALUE_ERRORS


class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DB_USER = os.getenv('POSTGRES_USER')
    if not DB_USER:
        raise ValueError(VALUE_ERRORS['POSTGRES_USER'])

    DB_PASSWORD = quote_plus(os.getenv('POSTGRES_PASSWORD', ''))
    DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '5432')
    DB_NAME = os.getenv('POSTGRES_DB', 'db_dev')

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )

    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    MIGRATIONS_DIR = os.getenv('MIGRATIONS_DIR')
