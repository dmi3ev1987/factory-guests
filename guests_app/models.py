from . import db
from .constants import MAX_STR_LENGTH


class PassRequest(db.Model):
    """Заявка на посещение."""

    id = db.Column(db.Integer, primary_key=True)
    guest_full_name_id = db.Column(
        db.Integer,
        db.ForeignKey('guest_full_name.id'),
    )
    company_name_id = db.Column(db.Integer, db.ForeignKey('company_name.id'))
    inviter_full_name_id = db.Column(
        db.Integer,
        db.ForeignKey('inviter_full_name.id'),
    )
    place_to_visit_id = db.Column(
        db.Integer,
        db.ForeignKey('place_to_visit.id'),
    )
    guest_full_name = db.relationship(
        'GuestFullName',
        back_populates='pass_requests',
    )
    company_name = db.relationship(
        'CompanyName',
        back_populates='pass_requests',
    )
    inviter_full_name = db.relationship(
        'InviterFullName',
        back_populates='pass_requests',
    )
    place_to_visit = db.relationship(
        'PlaceToVisit',
        back_populates='pass_requests',
    )
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)


class CompanyName(db.Model):
    """Название компании посетителя."""

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    pass_requests = db.relationship(
        'PassRequest',
        back_populates='company_name',
    )


class PlaceToVisit(db.Model):
    """Место посещения."""

    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    pass_requests = db.relationship(
        'PassRequest',
        back_populates='place_to_visit',
    )


class FullNameMixin(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
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
