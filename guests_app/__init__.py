from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from guests_app.admin import create_admin_panel
from settings import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, static_folder='static_dir')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .cli_commands import init_cli_commands

    init_cli_commands(app)

    return app


app = create_app()
admin = create_admin_panel(app)

from . import views  # noqa: F401
