from flask import render_template

from . import app, db
from .forms import GuestForm
from .models import PassRequest


@app.route('/')
def index_view():
    guests = PassRequest.query.with_entities(
        PassRequest.guest_full_name.label('guest_full_name'),
        PassRequest.company_name.label('company_name'),
        PassRequest.inviter_full_name.label('inviter_full_name'),
        PassRequest.place_to_visit.label('place_to_visit'),
        PassRequest.time_start.label('time_start'),
        PassRequest.time_end.label('time_end'),
        PassRequest.purpose.label('purpose'),
    ).all()
    guests_list = [dict(guest._asdict()) for guest in guests]
    return render_template('index.html', guests=guests_list)


@app.route('/request-form', methods=['GET', 'POST'])
def request_form_view():
    form = GuestForm()
    if form.validate_on_submit():
        guest = Guest(
            full_name=form.full_name.data,
            company_name=form.company_name.data,
            inviter=form.inviter.data,
            place_to_visit=form.place_to_visit.data,
            time_start=form.time_start.data,
            time_end=form.time_end.data,
            purpose=form.purpose.data,
        )
        db.session.add(guest)
        db.session.commit()
        return 'Заявка отправлена'
    return render_template('request_form.html', form=form)
