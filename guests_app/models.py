from sqlalchemy.ext.declarative import declared_attr

from . import db
from .constants import MAX_STR_LENGTH


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

        Например, для класса GuestFullName вернет 'guest_full_name'.
        """
        return ''.join(
            [
                '_' + character.lower() if character.isupper() else character
                for character in cls.__name__
            ],
        ).lstrip('_')

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
        db.ForeignKey('guest_full_name.id'),
    )
    inviter_full_name_id = db.Column(
        db.Integer,
        db.ForeignKey('inviter_full_name.id'),
    )
    company_name_id = db.Column(db.Integer, db.ForeignKey('company_name.id'))
    place_to_visit_id = db.Column(
        db.Integer,
        db.ForeignKey('place_to_visit.id'),
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
