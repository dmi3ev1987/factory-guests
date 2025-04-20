from flask_login import UserMixin

from guests_app import bcrypt, db
from guests_app.constants import MAX_STR_LENGTH
from guests_app.models.base import BaseModel


class User(UserMixin, BaseModel):
    username = db.Column(
        db.String(MAX_STR_LENGTH),
        nullable=False,
        unique=True,
    )
    password = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    email = db.Column(db.String(MAX_STR_LENGTH), nullable=False, unique=True)
    is_approver = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        """Хэширует пароль пользователя."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Проверяет пароль пользователя."""
        return bcrypt.check_password_hash(self.password, password)
