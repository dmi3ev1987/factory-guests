from flask import render_template, request

from guests_app import app
from guests_app.models import GuestFullName
from guests_app.routes.functions import get_guests


@app.route('/')
def index_view():
    """Главная страница приложения."""
    search_query = request.args.get('search_query')
    guests = (
        get_guests(date='today', search_query=search_query)
        .order_by(GuestFullName.surname.asc())
        .all()
    )

    guests_list = [dict(guest._asdict()) for guest in guests]

    return render_template('index.html', guests=guests_list)
