from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField
from wtforms.validators import InputRequired


class UserAdminView(ModelView):
    column_exclude_list = ['password']
    column_filters = ['username']

    form_overrides = {
        'password': PasswordField,
    }

    form_extra_fields = {
        'new_password': PasswordField(
            'Новый пароль',
            description='Оставьте пустым, чтобы сохранить текущий пароль',
            validators=[],
        ),
    }

    form_create_rules = [
        'username',
        'email',
        'password',
        'is_approver',
        'is_admin',
    ]

    form_edit_rules = [
        'username',
        'email',
        'new_password',
        'is_approver',
        'is_admin',
    ]

    form_args = {
        'username': {
            'label': 'Логин',
            'description': 'Уникальное имя пользователя',
        },
        'email': {
            'label': 'Электронная почта',
            'description': 'Действующий email адрес',
        },
        'password': {
            'label': 'Пароль',
            'validators': [InputRequired()],
            'description': 'Пароль должен быть надежным',
        },
        'is_admin': {
            'label': 'Администратор',
            'description': 'Дает полный доступ к системе',
        },
        'is_approver': {
            'label': 'Аппрувер',
            'description': 'Может подтверждать действия',
        },
    }

    def on_model_change(self, form, model, is_created):
        if is_created and form.password.data:
            model.set_password(form.password.data)
        elif not is_created and form.new_password.data:
            model.set_password(form.new_password.data)
