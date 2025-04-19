from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from guests_app.admin import create_admin
from settings import Config

app = Flask(__name__, static_folder='static_dir')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
admin = create_admin(app)

from . import views  # noqa: F401
