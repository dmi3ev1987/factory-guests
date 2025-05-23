from flask import redirect, url_for
from flask_admin import AdminIndexView
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_view'))

    def is_visible(self):
        """Скрыть ссылку "Home" в админке."""
        return False
