from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length

app = Flask(__name__, static_folder='static_dir')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'SECRET KEY'

db = SQLAlchemy(app)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128), nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    inviter = db.Column(db.String(128), nullable=False)
    place_to_visit = db.Column(db.String(128), nullable=False)
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    approved = db.Column(db.Boolean, default=False)


class GuestForm(FlaskForm):
    full_name = StringField(
        'ФИО посетителя',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    company_name = StringField(
        'Название организации',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    inviter = StringField(
        'Приглашающее лицо',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    place_to_visit = StringField(
        'Место посещения',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=128),
        ],
    )
    time_start = DateTimeLocalField(
        'Дата и время начала',
        validators=[DataRequired()],
    )
    time_end = DateTimeLocalField(
        'Дата и время окончания',
        validators=[DataRequired()],
    )
    purpose = TextAreaField('Цель визита', validators=[DataRequired()])
    submit = SubmitField('Отправить заявку')


@app.route('/')
def index_view():
    quantity = Guest.query.count()
    if quantity == 0:
        return render_template('index.html')
    guests = Guest.query.all()
    result = [{guest.id: guest.full_name} for guest in guests]
    return jsonify(result)


@app.route('/request-form')
def request_form_view():
    form = GuestForm()
    return render_template('request_form.html', form=form)


if __name__ == '__main__':
    app.run()
