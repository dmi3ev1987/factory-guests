from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__, static_folder='static_dir')
app.config.from_object(Config)
db = SQLAlchemy(app)

from . import views  # noqa: F401
