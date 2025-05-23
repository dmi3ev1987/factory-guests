from guests_app import db
from guests_app.models.mixins import FullNameMixin


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
