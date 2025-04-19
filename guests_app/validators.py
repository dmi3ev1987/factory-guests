import re

from wtforms.validators import ValidationError

from .constants import (
    EMAIL_DOMAIN,
    MAX_USERNAME_LENGTH,
    MIN_USERNAME_LENGTH,
    VALIDATION_MESSAGES,
)
from .models import User


def validate_username(form, field):
    if (
        len(field.data) < MIN_USERNAME_LENGTH
        or len(field.data) > MAX_USERNAME_LENGTH
    ):
        raise ValidationError(VALIDATION_MESSAGES['username_length'])
    if not re.fullmatch(r'^[A-Za-z0-9.]+$', field.data):
        raise ValidationError(VALIDATION_MESSAGES['username'])


def validate_username_exists(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError(VALIDATION_MESSAGES['username_exists'])


def validate_username_not_exists(form, field):
    if not User.query.filter_by(username=field.data).first():
        raise ValidationError(VALIDATION_MESSAGES['username_not_exists'])


def validate_email_is_corporate(form, field):
    if not field.data.endswith('@' + EMAIL_DOMAIN):
        raise ValidationError(VALIDATION_MESSAGES['email_not_corporate'])


def validate_email_exists(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError(VALIDATION_MESSAGES['email_exists'])
