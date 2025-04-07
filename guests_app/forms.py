from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length


class GuestForm(FlaskForm):
    full_name = TextAreaField(
        'ФИО посетителей',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=1000),
        ],
    )
    company_name = StringField(
        'Название организации',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    inviter = StringField(
        'Приглашающее лицо',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    place_to_visit = StringField(
        'Место посещения',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    time_start = DateTimeLocalField(
        'Дата и время начала',
        validators=[DataRequired(message='Обязательное поле')],
    )
    time_end = DateTimeLocalField(
        'Дата и время окончания',
        validators=[DataRequired(message='Обязательное поле')],
    )
    purpose = TextAreaField(
        'Цель визита',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=1000),
        ],
    )
    submit = SubmitField('Отправить заявку')
