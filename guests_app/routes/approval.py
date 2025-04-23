from flask import render_template

from guests_app import app
from guests_app.routes.functions import get_guests


@app.route('/approval')
def approval_view():
    """Страница одобрения заявок на пропуска."""
    guests = get_guests()

    guests_list = [dict(guest._asdict()) for guest in guests]

    return render_template('approval.html', guests=guests_list)
