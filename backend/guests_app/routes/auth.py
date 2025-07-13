from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user

from guests_app import app, db, login_manager
from guests_app.constants import FLASH_MESSAGES
from guests_app.forms import LoginForm, RegistrationForm
from guests_app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index_view'))
        flash(FLASH_MESSAGES['login_error'], 'error')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_view():
    logout_user()
    return redirect(url_for('login_view'))


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(FLASH_MESSAGES['register_success'], 'success')
        return redirect(url_for('login_view'))
    return render_template('register.html', form=form)
