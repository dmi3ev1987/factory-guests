from flask_admin import Admin

from .base import MyAdminIndexView
from .user_views import UserAdminView  # noqa: F401


def create_admin_panel(app):
    """Создает панель администратора."""
    return Admin(
        app,
        name='Администрирование',
        url='/admin/',
        template_mode='bootstrap3',
        index_view=MyAdminIndexView(),
    )
