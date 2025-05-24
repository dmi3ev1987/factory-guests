import click
from flask.cli import with_appcontext


def init_cli_commands(app):
    """Добавляет команды командной строки."""

    @app.cli.command('create-admin')
    @with_appcontext
    def create_admin_user() -> None:
        """Создает пользователя c правами администратора."""
        from . import db
        from .models import User

        email = app.config['ADMIN_EMAIL']
        user = User.query.filter_by(email=email).first()

        if user is None:
            username = app.config['ADMIN_USERNAME']
            password = app.config['ADMIN_PASSWORD']
            user = User(username=username, email=email, is_admin=True)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            click.echo(f'Admin user {email} created successfully')
        else:
            click.echo('Admin user already exists')
