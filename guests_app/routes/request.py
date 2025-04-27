from flask import flash, render_template

from guests_app import app, db
from guests_app.constants import FLASH_MESSAGES
from guests_app.forms import PassRequestForm
from guests_app.models import (
    CompanyName,
    GuestFullName,
    InviterFullName,
    PassRequest,
    PlaceToVisit,
)


@app.route('/request', methods=['GET', 'POST'])
def request_view():
    form = PassRequestForm()
    if form.validate_on_submit():
        guest_full_name = GuestFullName(
            first_name=form.guest_first_name.data,
            surname=form.guest_surname.data,
            patronymic=form.guest_patronymic.data,
        )
        db.session.add(guest_full_name)
        db.session.commit()

        inviter_full_name = InviterFullName(
            first_name=form.inviter_first_name.data,
            surname=form.inviter_surname.data,
            patronymic=form.inviter_patronymic.data,
        )
        db.session.add(inviter_full_name)
        db.session.commit()

        place_to_visit = PlaceToVisit(place=form.place_to_visit.data)
        db.session.add(place_to_visit)
        db.session.commit()

        company_name = CompanyName(name=form.company_name.data)
        db.session.add(company_name)
        db.session.commit()

        guest = PassRequest(
            guest_full_name_id=guest_full_name.id,
            inviter_full_name_id=inviter_full_name.id,
            company_name_id=company_name.id,
            place_to_visit_id=place_to_visit.id,
            time_start=form.time_start.data,
            time_end=form.time_end.data,
            purpose=form.purpose.data,
        )
        db.session.add(guest)
        db.session.commit()
        flash(FLASH_MESSAGES['request_success'], 'success')
    return render_template('request.html', form=form)
