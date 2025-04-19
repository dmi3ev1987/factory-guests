from wtforms.validators import ValidationError

from .constants import VALIDATION_MESSAGES
from .models import User


def validate_username_exists(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError(VALIDATION_MESSAGES['username_exists'])


def validate_username_not_exists(form, field):
    if not User.query.filter_by(username=field.data).first():
        raise ValidationError(VALIDATION_MESSAGES['username_not_exists'])


def validate_email_format(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError(VALIDATION_MESSAGES['email_exists'])
