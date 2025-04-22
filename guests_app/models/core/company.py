from guests_app import db
from guests_app.constants import MAX_STR_LENGTH
from guests_app.models.base import BaseModel


class CompanyName(BaseModel):
    """Название компании посетителя.

    Поля:
        name: название компании.
    """

    name = db.Column(db.String(MAX_STR_LENGTH), nullable=False)

    pass_requests = db.relationship(
        'PassRequest',
        back_populates='company_name',
    )
