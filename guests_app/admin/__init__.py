from flask_admin import Admin

from .base import MyAdminIndexView


def create_admin_panel(app):
    """Создает панель администратора."""
    return Admin(
        app,
        name='Guests',
        template_mode='bootstrap3',
        index_view=MyAdminIndexView(),
    )
