from guests_app import db
from guests_app.constants import MAX_STR_LENGTH
from guests_app.models.base import BaseModel


class PlaceToVisit(BaseModel):
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
