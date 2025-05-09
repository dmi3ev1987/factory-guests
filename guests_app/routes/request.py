from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from guests_app import app, db
from guests_app.constants import FLASH_MESSAGES
from guests_app.forms import PassRequestEditForm, PassRequestForm
from guests_app.models import (
    CompanyName,
    GuestFullName,
    InviterFullName,
    PassRequest,
    PlaceToVisit,
)
from guests_app.routes.functions import get_guests, get_pass_request_by_id


@app.route('/request', methods=['GET', 'POST'])
def request_create_view():
    """Создание заявки на пропуск."""
    form = PassRequestForm()
    if form.validate_on_submit():
        guest_full_name = GuestFullName(
            first_name=form.guest_first_name.data,
            surname=form.guest_surname.data,
            patronymic=form.guest_patronymic.data,
        )
        inviter_full_name = InviterFullName(
            first_name=form.inviter_first_name.data,
            surname=form.inviter_surname.data,
            patronymic=form.inviter_patronymic.data,
        )
        place_to_visit = PlaceToVisit(place=form.place_to_visit.data)
        company_name = CompanyName(name=form.company_name.data)

        db.session.add(guest_full_name)
        db.session.add(inviter_full_name)
        db.session.add(place_to_visit)
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
            created_by=current_user.username,
        )

        db.session.add(guest)
        db.session.commit()
        flash(FLASH_MESSAGES['request_success'], 'success')
    return render_template('request.html', form=form)


@app.route('/my_requests')
@login_required
def my_requests_view():
    """Отображение моих заявок."""
    guests = (
        get_guests(creator_username=current_user.username)
        .order_by(
            PassRequest.created_at.desc(),
        )
        .all()
    )
    return render_template('my_requests.html', guests=guests)


@app.route('/request/<int:request_id>')
def request_detail_view(request_id):
    """Отображение информации о заявке."""
    guest = get_guests(request_id=request_id).first()
    return render_template('request_detail.html', guest=guest)


@app.route('/delete_request/<int:request_id>', methods=['POST'])
@login_required
def request_delete_view(request_id):
    """Удаление заявки."""
    guest = PassRequest.query.get_or_404(request_id)
    db.session.delete(guest)
    db.session.commit()
    flash(FLASH_MESSAGES['request_deleted'], 'delete')
    return redirect(url_for('my_requests_view'))


@app.route('/edit_request/<int:request_id>', methods=['GET', 'POST'])
@login_required
def request_edit_view(request_id):
    """Редактирование заявки."""
    guest = get_guests(request_id=request_id).first()
    form = PassRequestEditForm(obj=guest)
    if form.validate_on_submit():
        pass_request = get_pass_request_by_id(request_id)

        pass_request.guest_full_name.first_name = form.guest_first_name.data
        pass_request.guest_full_name.surname = form.guest_surname.data
        pass_request.guest_full_name.patronymic = form.guest_patronymic.data

        pass_request.inviter_full_name.first_name = (
            form.inviter_first_name.data
        )
        pass_request.inviter_full_name.surname = form.inviter_surname.data
        pass_request.inviter_full_name.patronymic = (
            form.inviter_patronymic.data
        )

        pass_request.company_name.name = form.company_name.data

        pass_request.place_to_visit.place = form.place_to_visit.data

        pass_request.time_start = form.time_start.data
        pass_request.time_end = form.time_end.data
        pass_request.purpose = form.purpose.data

        db.session.add(pass_request)
        db.session.commit()
        flash(FLASH_MESSAGES['request_updated'], 'success')
        return redirect(url_for('my_requests_view'))

    return render_template('request_edit.html', form=form, guest=guest)
