from . import db


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text, nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    inviter = db.Column(db.String(128), nullable=False)
    place_to_visit = db.Column(db.String(128), nullable=False)
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    approved = db.Column(db.Boolean, default=False)
