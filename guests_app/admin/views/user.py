from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField
from wtforms.validators import InputRequired

from guests_app.constants import DESCRIPTIONS, LABELS


class UserAdminView(ModelView):
    column_exclude_list = ['password']
    column_filters = ['username']

    form_overrides = {
        'password': PasswordField,
    }

    form_extra_fields = {
        'new_password': PasswordField(
            LABELS['new_password'],
            description=DESCRIPTIONS['new_password'],
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
            'label': LABELS['username'],
            'description': DESCRIPTIONS['username'],
        },
        'email': {
            'label': LABELS['email'],
            'description': DESCRIPTIONS['email'],
        },
        'password': {
            'label': LABELS['password'],
            'validators': [InputRequired()],
            'description': DESCRIPTIONS['password'],
        },
        'is_admin': {
            'label': LABELS['is_admin'],
            'description': DESCRIPTIONS['is_admin'],
        },
        'is_approver': {
            'label': LABELS['is_approver'],
            'description': DESCRIPTIONS['is_approver'],
        },
    }

    def on_model_change(self, form, model, is_created):
        if is_created and form.password.data:
            model.set_password(form.password.data)
        elif not is_created and form.new_password.data:
            model.set_password(form.new_password.data)
