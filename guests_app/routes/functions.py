from guests_app.models import (
    CompanyName,
    GuestFullName,
    InviterFullName,
    PassRequest,
    PlaceToVisit,
)


def get_guests():
    return (
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
