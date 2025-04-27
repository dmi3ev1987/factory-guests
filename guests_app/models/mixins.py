from guests_app import db
from guests_app.constants import MAX_STR_LENGTH
from guests_app.models.base import BaseModel


class CreateUpdateMixin(db.Model):
    """Миксин для хранения даты и времени создания и обновления записи.

    Поля:
        created_at: дата и время создания записи;
        updated_at: дата и время последнего обновления записи;
        updated_by: кто обновил запись.
    """

    __abstract__ = True

    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=db.func.now())
    updated_by = db.Column(db.String(MAX_STR_LENGTH), nullable=True)


class FullNameMixin(BaseModel):
    """Миксин для хранения ФИО.

    Поля:
        id: уникальный идентификатор;
        first_name: имя;
        surname: фамилия;
        patronymic: отчество.
    """

    __abstract__ = True

    first_name = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    surname = db.Column(db.String(MAX_STR_LENGTH), nullable=False)
    patronymic = db.Column(db.String(MAX_STR_LENGTH), nullable=True)
