from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from guests_app.admin import UserAdminView, create_admin_panel
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


from flask_admin.menu import MenuLink

from . import views  # noqa: F401
from .models import User

admin = create_admin_panel(app)
admin.add_view(UserAdminView(User, db.session, name='Пользователи'))
admin.add_link(
    MenuLink(
        name='Вернуться на сайт',
        url='/',
    ),
)
