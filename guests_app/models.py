from flask_login import UserMixin
from sqlalchemy.ext.declarative import declared_attr

from . import bcrypt, db
from .constants import MAX_STR_LENGTH


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(MAX_STR_LENGTH),
        nullable=False,
        unique=True,
    )
    password = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    is_approver = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        """Хэширует пароль пользователя."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Проверяет пароль пользователя."""
        return bcrypt.check_password_hash(self.password, password)


class BaseMixin(db.Model):
    """Базовая модель для всех моделей приложения.

    Поля:
        id: уникальный идентификатор и первичный ключ;
        created_at: дата и время создания записи;
        updated_at: дата и время последнего обновления записи;
        updated_by: кто обновил запись.
    """

    __abstract__ = True

    @classmethod
    def _get_tablename(cls):
        """Конвертирует имя класса из CamelCase в snake_case.

        Добавляет 's' в конец имени класса, чтобы получить имя таблицы в
        множественном числе.
        Например, для класса GuestFullName вернет 'guest_full_names'.
        """
        name = ''.join(
            [
                '_' + character.lower() if character.isupper() else character
                for character in cls.__name__
            ],
        ).lstrip('_')
        return f'{name}s'

    @declared_attr
    def __tablename__(cls):
        """Возвращает имя таблицы для модели."""
        return cls._get_tablename()

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=db.func.now())
    updated_by = db.Column(db.String(MAX_STR_LENGTH), nullable=True)


class FullNameMixin(BaseMixin):
    """Миксин для хранения ФИО.

    Поля:
        id: уникальный идентификатор;
        first_name: имя;
        surname: фамилия;
        patronymic: отчество.
    """

    __abstract__ = True

    first_name = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    surname = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    patronymic = db.Column(db.String(MAX_STR_LENGTH), nullable=True)


class GuestFullName(FullNameMixin):
    """ФИО посетителя."""

    pass_requests = db.relationship(
        'PassRequest',
        back_populates='guest_full_name',
    )


class InviterFullName(FullNameMixin):
    """ФИО приглашающего лица."""

    pass_requests = db.relationship(
        'PassRequest',
        back_populates='inviter_full_name',
    )


class CompanyName(BaseMixin):
    """Название компании посетителя.

    Поля:
        name: название компании.
    """

    name = db.Column(db.String(MAX_STR_LENGTH), nullable=False)

    pass_requests = db.relationship(
        'PassRequest',
        back_populates='company_name',
    )


class PlaceToVisit(BaseMixin):
    """Место посещения.

    Поля:
        place: название места.
    """

    __tablename__ = 'places_to_visit'

    place = db.Column(db.String(MAX_STR_LENGTH), nullable=False)

    pass_requests = db.relationship(
        'PassRequest',
        back_populates='place_to_visit',
    )


class PassRequest(BaseMixin):
    """Заявка на посещение.

    Поля:
        guest_full_name_id: идентификатор посетителя;
        inviter_full_name_id: идентификатор приглашающего лица;
        company_name_id: идентификатор компании;
        place_to_visit_id: идентификатор места посещения;

        guest_full_name: ФИО посетителя;
        inviter_full_name: ФИО приглашающего лица;
        company_name: название компании;
        place_to_visit: место посещения;

        time_start: дата и время начала посещения;
        time_end: дата и время окончания посещения;
        purpose: цель посещения;
        approved: статус одобрения заявки;
    """

    guest_full_name_id = db.Column(
        db.Integer,
        db.ForeignKey('guest_full_names.id'),
    )
    inviter_full_name_id = db.Column(
        db.Integer,
        db.ForeignKey('inviter_full_names.id'),
    )
    company_name_id = db.Column(db.Integer, db.ForeignKey('company_names.id'))
    place_to_visit_id = db.Column(
        db.Integer,
        db.ForeignKey('places_to_visit.id'),
    )

    guest_full_name = db.relationship(
        'GuestFullName',
        back_populates='pass_requests',
    )
    inviter_full_name = db.relationship(
        'InviterFullName',
        back_populates='pass_requests',
    )
    company_name = db.relationship(
        'CompanyName',
        back_populates='pass_requests',
    )
    place_to_visit = db.relationship(
        'PlaceToVisit',
        back_populates='pass_requests',
    )

    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    approved = db.Column(db.Boolean, default=None, nullable=True)
