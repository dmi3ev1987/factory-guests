from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, ValidationError

from .constants import (
    DATA_REQUIRED_MESSAGE,
    ERROR_MESSAGES,
    LABELS,
    MAX_STR_LENGTH,
    MAX_TEXT_LENGTH,
    SUBMIT_MESSAGE,
    SUBMIT_REGISTRATION,
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
        SUBMIT_MESSAGE,
        render_kw={'class': 'btn primary small'},
    )


class RegistrationForm(FlaskForm):
    email = StringField(
        LABELS['email'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
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
        SUBMIT_REGISTRATION,
        render_kw={'class': 'btn primary small'},
    )

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(ERROR_MESSAGES['email_exists'])
