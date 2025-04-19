from sqlalchemy.ext.declarative import declared_attr

from . import db
from .constants import MAX_STR_LENGTH


class BaseMixin(db.Model):
    """Базовая модель для всех моделей приложения.

    Поля:
        id: уникальный идентификатор и первичный ключ;
    """

    __abstract__ = True

    @classmethod
    def _get_tablename(cls):
        """Конвертирует имя класса из CamelCase в snake_case.

        Добавляет 's' в конец имени класса, чтобы получить имя таблицы в
        множественном числе.
        Например, для класса GuestFullName вернет 'guest_full_names'.
        """
        name = ''.join(
            [
                '_' + character.lower() if character.isupper() else character
                for character in cls.__name__
            ],
        ).lstrip('_')
        return f'{name}s'

    @declared_attr
    def __tablename__(cls):
        """Возвращает имя таблицы для модели."""
        return cls._get_tablename()

    id = db.Column(db.Integer, primary_key=True)


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


class FullNameMixin(BaseMixin):
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
