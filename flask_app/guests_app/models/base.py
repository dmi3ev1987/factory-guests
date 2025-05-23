from sqlalchemy.ext.declarative import declared_attr

from guests_app import db


class BaseModel(db.Model):
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
