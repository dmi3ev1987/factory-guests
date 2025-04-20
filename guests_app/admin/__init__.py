from flask_admin import Admin

from guests_app import db
from guests_app.admin.base import MyAdminIndexView
from guests_app.models import User


def create_admin(app):
    return Admin(
        app,
        name='Guests',
        template_mode='bootstrap3',
        index_view=MyAdminIndexView(),
    )


def create_admin_user(app):
    admin_email = app.config['ADMIN_EMAIL']
    admin_user = User.query.filter_by(email=admin_email, is_admin=True).first()

    if not admin_user:
        admin_password = app.config['ADMIN_PASSWORD']
        admin_user = User(email=admin_email, is_approver=True)
        admin_user.set_password(admin_password)
        db.session.add(admin_user)
        db.session.commit()
