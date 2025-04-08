from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length

from .constants import (
    DATA_REQUIRED_MESSAGE,
    MAX_STR_LENGTH,
    MAX_TEXT_LENGTH,
    SUBMIT_MESSAGE,
)


class GuestForm(FlaskForm):
    full_name = TextAreaField(
        'ФИО посетителей',
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
    )
    company_name = StringField(
        'Название организации',
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
    )
    inviter = StringField(
        'Приглашающее лицо',
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
    )
    place_to_visit = StringField(
        'Место посещения',
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
    )
    time_start = DateTimeLocalField(
        'Дата и время начала',
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE)],
    )
    time_end = DateTimeLocalField(
        'Дата и время окончания',
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE)],
    )
    purpose = TextAreaField(
        'Цель визита',
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
    )
    submit = SubmitField(SUBMIT_MESSAGE)
