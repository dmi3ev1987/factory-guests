from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from guests_app.cli_commands import init_cli_commands
from settings import Config

app = Flask(__name__, static_folder='static_dir')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
init_cli_commands(app)


from . import (  # noqa: F401
    admin,
    routes,
)
