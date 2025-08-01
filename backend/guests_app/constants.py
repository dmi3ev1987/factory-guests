import os

# Length constants
MAX_STR_LENGTH = 128
MAX_TEXT_LENGTH = 1000
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 20

# email domain
EMAIL_DOMAIN = os.getenv('EMAIL_DOMAIN')

# Message constants
SUBMIT = {
    'submit_request': 'Отправить заявку',
    'submit_registration': 'Зарегистрироваться',
    'submit_login': 'Войти',
    'submit_edit': 'Сохранить изменения',
}
DATA_REQUIRED_MESSAGE = 'Обязательное поле'
FLASH_MESSAGES = {
    'login_error': 'Неправильный логин или пароль',
    'register_success': 'Вы успешно зарегистрировались',
    'request_success': (
        'Ваша заявка успешно отправлена и находится на рассмотрении'
    ),
    'request_deleted': 'Ваша заявка успешно удалена',
    'request_updated': 'Ваша заявка успешно обновлена',
    'request_approved': 'Заявка успешно одобрена',
    'request_rejected': 'Заявка отклонена',
}

# Labels
LABELS = {
    'first_name': 'Имя',
    'surname': 'Фамилия',
    'patronymic': 'Отчество',
    'company_name': 'Название организации',
    'place_to_visit': 'Место посещения',
    'time_start': 'Начало посещения',
    'time_end': 'Завершение посещения',
    'purpose': 'Цель посещения',
    'username': 'Имя пользователя',
    'email': 'Электронная почта',
    'password': 'Пароль',
    'new_password': 'Новый пароль',
    'confirm_password': 'Подтвердите пароль',
    'is_admin': 'Администратор',
    'is_approver': 'Аппрувер',
}
DESCRIPTIONS = {
    'new_password': 'Оставьте пустым, чтобы сохранить текущий пароль',
    'username': 'Уникальное имя пользователя',
    'email': 'Действующий email адрес',
    'password': 'Пароль должен быть надежным',
    'is_admin': 'Дает полный доступ к системе',
    'is_approver': 'Может одобрять заявки',
}

# Error messages
VALIDATION_MESSAGES = {
    'username': (
        'Имя пользователя может состоять только из латинских букв и цифр'
    ),
    'username_length': (
        'Длина имени пользователя должна быть от 3 до 20 символов'
    ),
    'username_exists': 'Пользователь с таким именем уже зарегистрирован',
    'username_not_exists': 'Пользователь с таким именем не зарегистрирован',
    'email_exists': 'Пользователь с таким email уже зарегистрирован',
    'email_not_corporate': 'email должен завершаться на ' + EMAIL_DOMAIN,
    'end_time_earlier': 'Время окончания должно быть позже времени начала',
}
VALUE_ERRORS = {
    'DB_USER': 'DB_USER переменная окружения не установлена',
}

# Password check
PASSWORD_CHECK = {
    'one_digit': 'минимум 1 цифру',
    'upper_case': 'минимум 1 заглавную букву',
    'lower_case': 'минимум 1 строчную букву',
    'special_character': 'минимум 1 спецсимвол',
    'min_length': 'минимум 8 символов',
    'error_text': 'Пароль должен содержать: ',
}
