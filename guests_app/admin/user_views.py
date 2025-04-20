from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField


class UserAdminView(ModelView):
    name = 'Пользователи'
    column_exclude_list = ['password']
    column_filters = ['username']

    form_extra_fields = {'new_password': PasswordField('Новый пароль')}
    form_excluded_columns = ['password']
    form_args = {
        'username': {'label': 'Логин'},
        'email': {'label': 'Электронная почта'},
        'is_admin': {'label': 'Администратор'},
        'is_approver': {'label': 'Аппрувер'},
    }

    def on_model_change(self, form, model, is_created):
        if form.new_password.data:
            model.set_password(form.new_password.data)
