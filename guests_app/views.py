from flask import render_template

from . import app, db
from .forms import PassRequestForm
from .models import (
    CompanyName,
    GuestFullName,
    InviterFullName,
    PassRequest,
    PlaceToVisit,
)


@app.route('/')
def index_view():
    guests = (
        PassRequest.query.join(GuestFullName)
        .join(CompanyName)
        .join(InviterFullName)
        .join(PlaceToVisit)
        .with_entities(
            GuestFullName.first_name.label('guest_first_name'),
            GuestFullName.surname.label('guest_surname'),
            GuestFullName.patronymic.label('guest_patronymic'),
            InviterFullName.first_name.label('inviter_first_name'),
            InviterFullName.surname.label('inviter_surname'),
            InviterFullName.patronymic.label('inviter_patronymic'),
            CompanyName.company_name.label('company_name'),
            PlaceToVisit.place.label('place_to_visit'),
            PassRequest.time_start,
            PassRequest.time_end,
            PassRequest.purpose,
            PassRequest.approved,
        )
        .all()
    )

    guests_list = [dict(guest._asdict()) for guest in guests]

    return render_template('index.html', guests=guests_list)


@app.route('/request-form', methods=['GET', 'POST'])
def request_form_view():
    form = PassRequestForm()
    if form.validate_on_submit():
        guest = PassRequest(
            guest_first_name=form.guest_first_name.data,
            guest_surname=form.guest_surname.data,
            guest_patronymic=form.guest_patronymic.data,
            inviter_first_name=form.inviter_first_name.data,
            inviter_surname=form.inviter_surname.data,
            inviter_patronymic=form.inviter_patronymic.data,
            company_name=form.company_name.data,
            place_to_visit=form.place_to_visit.data,
            time_start=form.time_start.data,
            time_end=form.time_end.data,
            purpose=form.purpose.data,
        )
        db.session.add(guest)
        db.session.commit()
        return 'Заявка отправлена'
    return render_template('request_form.html', form=form)
