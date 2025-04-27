from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from guests_app import app, db
from guests_app.admin.functions import create_admin_panel
from guests_app.admin.views import UserAdminView
from guests_app.models import PassRequest, User

admin = create_admin_panel(app)
admin.add_link(
    MenuLink(
        name='Вернуться на сайт',
        url='/',
    ),
)

admin.add_view(UserAdminView(User, db.session, name='Пользователи'))

# Убрать на продакшене или доработать
admin.add_view(ModelView(PassRequest, db.session, name='Заявки'))
