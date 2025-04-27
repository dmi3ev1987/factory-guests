from flask import render_template

from guests_app import app
from guests_app.routes.functions import get_guests


@app.route('/')
def index_view():
    """Главная страница приложения."""
    guests = get_guests()

    guests_list = [dict(guest._asdict()) for guest in guests]

    return render_template('index.html', guests=guests_list)
