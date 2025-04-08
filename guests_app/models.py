from . import db
from .constants import MAX_STR_LENGTH


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text, nullable=False)
    company_name = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    inviter = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    place_to_visit = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    approved = db.Column(db.Boolean, default=False)
