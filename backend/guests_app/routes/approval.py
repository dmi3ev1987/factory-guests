from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from guests_app import app, db
from guests_app.constants import FLASH_MESSAGES
from guests_app.models import PassRequest
from guests_app.routes.functions import get_guests


@app.route('/approval')
def approval_view():
    """Страница одобрения заявок на пропуска."""
    search_query = request.args.get('search_query')
    guests = get_guests(
        approval_status='pending',
        search_query=search_query,
    ).all()

    guests_list = [dict(guest._asdict()) for guest in guests]

    return render_template('approval.html', guests=guests_list)


@app.route('/approve_request/<request_id>', methods=['POST'])
@login_required
def approve_request_view(request_id):
    if current_user.is_approver:
        pass_request = PassRequest.query.get(request_id)
        pass_request.approved = True
        db.session.commit()
        flash(FLASH_MESSAGES['request_approved'], 'approve')
    return redirect(url_for('approval_view'))


@app.route('/reject_request/<request_id>', methods=['POST'])
@login_required
def reject_request_view(request_id):
    if current_user.is_approver:
        pass_request = PassRequest.query.get(request_id)
        pass_request.approved = False
        db.session.commit()
        flash(FLASH_MESSAGES['request_rejected'], 'reject')
    return redirect(url_for('approval_view'))
