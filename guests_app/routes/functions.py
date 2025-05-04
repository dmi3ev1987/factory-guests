from datetime import datetime, timedelta

from guests_app.models import (
    CompanyName,
    GuestFullName,
    InviterFullName,
    PassRequest,
    PlaceToVisit,
)


def get_guests(approval_status='all', date='all', request_id=None):
    """Получение списка заявок на посещение с учетом статуса одобрения.

    Args:
        approval_status (str): Статус одобрения заявки.
            Может быть:
            'all' - все заявки,
            'approved' - одобренные заявки,
            'rejected' - отклоненные заявки,
            'pending' - ожидающие.

        request_id (int): ID заявки, которую нужно получить.
        date (str): Дата, для которой нужно получить заявки.

    Returns:
        query: SQLAlchemy query object.

    """
    query = (
        PassRequest.query.join(GuestFullName)
        .join(CompanyName)
        .join(InviterFullName)
        .join(PlaceToVisit)
    )

    if approval_status != 'all':
        if approval_status == 'approved':
            query = query.filter(PassRequest.approved.is_(True))
        elif approval_status == 'rejected':
            query = query.filter(PassRequest.approved.is_(False))
        elif approval_status == 'pending':
            query = query.filter(PassRequest.approved.is_(None))
        else:
            message = f'Неверный статус одобрения: {approval_status}'
            raise ValueError(message)

    if date == 'today':
        today_start = datetime.now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )
        today_end = today_start + timedelta(days=1)
        query = query.filter(
            PassRequest.time_start < today_end,
            PassRequest.time_end > today_start,
        )

    if request_id:
        query = query.filter(PassRequest.id == request_id)

    return query.with_entities(
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
        PassRequest.id,
    )
