from guests_app import db
from guests_app.models.base import BaseModel
from guests_app.models.mixins import CreateUpdateMixin


class PassRequest(CreateUpdateMixin, BaseModel):
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
