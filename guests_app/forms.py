import re

from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    ValidationError,
)

from .constants import (
    DATA_REQUIRED_MESSAGE,
    ERROR_MESSAGES,
    LABELS,
    MAX_STR_LENGTH,
    MAX_TEXT_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_USERNAME_LENGTH,
    SUBMIT,
)
from .models import User


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
            'class': 'form-control',
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
            'class': 'form-control',
            'placeholder': LABELS['place_to_visit'],
        },
    )
    time_start = DateTimeLocalField(
        LABELS['time_start'],
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE)],
        render_kw={
            'class': 'form-control',
        },
    )
    time_end = DateTimeLocalField(
        LABELS['time_end'],
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE)],
        render_kw={
            'class': 'form-control',
        },
    )
    purpose = TextAreaField(
        LABELS['purpose'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['purpose'],
        },
    )
    submit = SubmitField(
        SUBMIT['submit_request'],
        render_kw={'class': 'btn primary small'},
    )


class RegistrationForm(FlaskForm):
    username = StringField(
        LABELS['username'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['username'],
        },
    )
    email = StringField(
        LABELS['email'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            Email(),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['email'],
        },
    )
    password = StringField(
        LABELS['password'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['password'],
        },
    )
    confirm_password = StringField(
        'Подтвердите пароль',
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            EqualTo('password', message='Пароли не совпадают'),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
        },
    )
    submit = SubmitField(
        SUBMIT['submit_registration'],
        render_kw={'class': 'btn primary small'},
    )

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(ERROR_MESSAGES['email_exists'])

    def validate_username(self, username):
        if (
            len(username.data) < MIN_USERNAME_LENGTH
            or len(username.data) > MAX_USERNAME_LENGTH
        ):
            raise ValidationError(ERROR_MESSAGES['username_length'])
        if not re.fullmatch(r'^[A-Za-z0-9.]+$', username.data):
            raise ValidationError(ERROR_MESSAGES['username'])
        if User.query.filter_by(username=username.data).first():
            raise ValidationError(ERROR_MESSAGES['username_exists'])


class LoginForm(FlaskForm):
    email = StringField(
        LABELS['email'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
            Email(),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['email'],
        },
    )
    password = StringField(
        LABELS['password'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['password'],
        },
    )
    submit = SubmitField(
        SUBMIT['submit_login'],
        render_kw={'class': 'btn primary small'},
    )
