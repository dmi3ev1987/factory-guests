from flask_login import UserMixin

from . import bcrypt, db
from .constants import MAX_STR_LENGTH
from .mixins import BaseMixin, CreateUpdateMixin, FullNameMixin


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


class PassRequest(CreateUpdateMixin, BaseMixin):
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


class User(BaseMixin, UserMixin, db.Model):
    username = db.Column(
        db.String(MAX_STR_LENGTH),
        nullable=False,
        unique=True,
    )
    password = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    email = db.Column(db.String(MAX_STR_LENGTH), nullable=False, unique=True)
    is_approver = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        """Хэширует пароль пользователя."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Проверяет пароль пользователя."""
        return bcrypt.check_password_hash(self.password, password)
