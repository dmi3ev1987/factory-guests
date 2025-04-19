from flask_admin import Admin

from .base import AdminBaseView


def create_admin(app):
    return Admin(
        app,
        name='Guests',
        template_mode='bootstrap3',
        index_view=AdminBaseView(),
    )
