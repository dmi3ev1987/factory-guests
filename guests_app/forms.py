from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
)

from .constants import (
    DATA_REQUIRED_MESSAGE,
    LABELS,
    MAX_STR_LENGTH,
    MAX_TEXT_LENGTH,
    SUBMIT,
)
from .validators import (
    validate_email_exists,
    validate_email_is_corporate,
    validate_username,
    validate_username_exists,
    validate_username_not_exists,
)


class PassRequestForm(FlaskForm):
    guest_first_name = StringField(
        LABELS['first_name'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-name',
            'placeholder': LABELS['first_name'],
        },
    )
    guest_surname = StringField(
        LABELS['surname'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-name',
            'placeholder': LABELS['surname'],
        },
    )
    guest_patronymic = StringField(
        LABELS['patronymic'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-name',
            'placeholder': LABELS['patronymic'],
        },
    )
    inviter_first_name = StringField(
        LABELS['first_name'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-name',
            'placeholder': LABELS['first_name'],
        },
    )
    inviter_surname = StringField(
        LABELS['surname'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-name',
            'placeholder': LABELS['surname'],
        },
    )
    inviter_patronymic = StringField(
        LABELS['patronymic'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-name',
            'placeholder': LABELS['patronymic'],
        },
    )
    company_name = StringField(
        LABELS['company_name'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-full',
            'placeholder': LABELS['company_name'],
        },
    )
    place_to_visit = StringField(
        LABELS['place_to_visit'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-full',
            'placeholder': LABELS['place_to_visit'],
        },
    )
    time_start = DateTimeLocalField(
        LABELS['time_start'],
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE)],
        render_kw={
            'class': 'form-control-name',
        },
    )
    time_end = DateTimeLocalField(
        LABELS['time_end'],
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE)],
        render_kw={
            'class': 'form-control-name',
        },
    )
    purpose = TextAreaField(
        LABELS['purpose'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-full',
            'placeholder': LABELS['purpose'],
            'rows': 3,
            'style': 'height: auto !important;',
        },
    )
    submit = SubmitField(
        SUBMIT['submit_request'],
        render_kw={'class': 'btn primary small form-control-center'},
    )


class RegistrationForm(FlaskForm):
    username = StringField(
        LABELS['username'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            validate_username,
            validate_username_exists,
        ],
        render_kw={
            'class': 'form-control form-control-center',
            'placeholder': LABELS['username'],
        },
    )
    email = StringField(
        LABELS['email'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            Email(),
            validate_email_is_corporate,
            validate_email_exists,
        ],
        render_kw={
            'class': 'form-control form-control-center',
            'placeholder': LABELS['email'],
        },
    )
    password = PasswordField(
        LABELS['password'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-center',
            'placeholder': LABELS['password'],
        },
    )
    confirm_password = PasswordField(
        LABELS['confirm_password'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            EqualTo('password', message='Пароли не совпадают'),
        ],
        render_kw={
            'class': 'form-control form-control-center',
            'placeholder': LABELS['confirm_password'],
        },
    )
    submit = SubmitField(
        SUBMIT['submit_registration'],
        render_kw={'class': 'btn primary small form-control-center'},
    )


class LoginForm(FlaskForm):
    username = StringField(
        LABELS['username'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            validate_username_not_exists,
        ],
        render_kw={
            'class': 'form-control form-control-center',
            'placeholder': LABELS['username'],
        },
    )
    password = PasswordField(
        LABELS['password'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control form-control-center',
            'placeholder': LABELS['password'],
        },
    )
    submit = SubmitField(
        SUBMIT['submit_login'],
        render_kw={'class': 'btn primary small login'},
    )
