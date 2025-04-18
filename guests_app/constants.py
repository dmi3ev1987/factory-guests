# Length constants
MAX_STR_LENGTH = 128
MAX_TEXT_LENGTH = 1000
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 20

# Message constants
SUBMIT = {
    'submit_request': 'Отправить заявку',
    'submit_registration': 'Зарегистрироваться',
    'submit_login': 'Войти',
}
DATA_REQUIRED_MESSAGE = 'Обязательное поле'
FLASH_MESSAGES = {
    'login_error': 'Неправильный логин или пароль',
    'register_success': 'Вы успешно зарегистрировались',
}

# Labels
LABELS = {
    'first_name': 'Имя',
    'surname': 'Фамилия',
    'patronymic': 'Отчество',
    'company_name': 'Название организации',
    'place_to_visit': 'Место посещения',
    'time_start': 'Дата и время начала посещения',
    'time_end': 'Дата и время окончания посещения',
    'purpose': 'Цель посещения',
    'username': 'Имя пользователя',
    'email': 'Электронная почта',
    'password': 'Пароль',
    'confirm_password': 'Подтвердите пароль',
}

# Error messages
ERROR_MESSAGES = {
    'email_exists': 'Пользователь с таким email уже зарегистрирован',
    'username': (
        'Имя пользователя может состоять только из латинских букв и цифр'
    ),
    'username_length': (
        'Длина имени пользователя должна быть от 3 до 20 символов'
    ),
    'username_exists': 'Пользователь с таким именем уже зарегистрирован',
}
