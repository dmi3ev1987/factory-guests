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
    LABELS,
    MAX_STR_LENGTH,
    MAX_TEXT_LENGTH,
    SUBMIT_MESSAGE,
)


class GuestForm(FlaskForm):
    full_name = TextAreaField(
        LABELS['full_name'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_TEXT_LENGTH),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['full_name'],
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
    inviter = StringField(
        LABELS['inviter'],
        validators=[
            DataRequired(message=DATA_REQUIRED_MESSAGE),
            Length(max=MAX_STR_LENGTH),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': LABELS['inviter'],
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
