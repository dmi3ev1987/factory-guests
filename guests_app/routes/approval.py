from flask import redirect, render_template, url_for
from flask_login import current_user, login_required

from guests_app import app, db
from guests_app.models import PassRequest
from guests_app.routes.functions import get_guests


@app.route('/approval')
def approval_view():
    """Страница одобрения заявок на пропуска."""
    guests = get_guests(approval_status='pending')

    guests_list = [dict(guest._asdict()) for guest in guests]

    return render_template('approval.html', guests=guests_list)


@app.route('/approve_request/<request_id>', methods=['POST'])
@login_required
def approve_request(request_id):
    if current_user.is_approver:
        pass_request = PassRequest.query.get(request_id)
        pass_request.approved = True
        db.session.commit()
    return redirect(url_for('approval_view'))


@app.route('/reject_request/<request_id>', methods=['POST'])
@login_required
def reject_request(request_id):
    if current_user.is_approver:
        pass_request = PassRequest.query.get(request_id)
        pass_request.approved = False
        db.session.commit()
    return redirect(url_for('approval_view'))
