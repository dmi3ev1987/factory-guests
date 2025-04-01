from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128), nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    inviter = db.Column(db.String(128), nullable=False)
    place_to_visit = db.Column(db.String(128), nullable=False)
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    approved = db.Column(db.Boolean, default=False)


@app.route('/')
def my_index_view():
    quantity = Guest.query.count()
    if quantity == 0:
        return render_template('index.html')
    guests = Guest.query.all()
    result = [{guest.id: guest.full_name} for guest in guests]
    return jsonify(result)


@app.route('/request-form')
def request_form():
    return render_template('request_form.html')


if __name__ == '__main__':
    app.run()
