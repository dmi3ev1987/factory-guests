from flask import render_template

from . import app, db, login_manager
from .forms import LoginForm, PassRequestForm, RegistrationForm
from .models import (
    CompanyName,
    GuestFullName,
    InviterFullName,
    PassRequest,
    PlaceToVisit,
    User,
)


@login_manager.user_loader
def load_user(user_id):
    """Загрузка пользователя по идентификатору."""
    return User.query.get(int(user_id))


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
            CompanyName.name.label('company_name'),
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
        return 'Заявка отправлена'
    return render_template('request_form.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    form = RegistrationForm()
    return render_template('register.html', form=form)
