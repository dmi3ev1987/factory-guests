
## Как запустить проект
  
Cоздать и активировать виртуальное окружение:

* Если у вас Linux/macOS
  
```
python3 -m venv venv

source env/bin/activate
```

* Если у вас windows

```
python -m venv venv

source env/scripts/activate
```

Обновите менеджер пакетов pip:

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
  
## Создать БД sqlite (вручную)
  
```
flask shell
```

После входа в shell вести команды по очереди:

```
>>> from guests_app import db
>>> db.drop_all() # если нужно удалить предыдушую БД
>>> db.create_all()
>>> quit()
```

## Работа с миграциями

```
# Создать репозиторий сценариев миграций
flask db init

# Создать миграции
flask db migrate -m "Name of mirgration"

# Применить миграции
flask db upgrade
```

## Работа с Ruff linter and formatter

```
# Check and auto-fix all files in the project:
ruff check --fix

# Check/fix a specific file:
ruff check --fix path/to/file.py

# Preview fixes before applying:
ruff check --fix --diff

# For formatting, use:
ruff format
```


## Запуск приложения в контейнерах

1. Локальный запуск всего приложения:

```
sudo docker compose -f docker-compose.local.yml up --build
```

В .env файле нужно указать:

```
# для запуска всего проекта указать имя сервиса с postgres
POSTGRES_HOST=postgres
```

2. Локальный запуск только postgres в контейнере:

```
sudo docker compose -f docker-compose.local.postgres.yml up --build
```

В .env файле нужно указать:

```
# для запуска только postgres в контейнере
POSTGRES_HOST=localhost
```

Запустить прилоежение в терминале из папки backend:

```
cd backend/

flask run
```

3. Локальный запуск приложения без контенеров и с базой SQLite:

В файле settings.py прописать:
```
# backend/guests_app/settings.py

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
```

В .env файле прописать:

```
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
```

Запустить прилоежение в терминале из папки backend:

```
cd backend/

flask run
```

4. Команды docker для очистки системы:

```
# удалить все контейнеры и volumes
sudo docker compose -f docker-compose.local.yml down -v

# очистка системы от образов
sudo docker system prune -a --volumes
```
  

### Автор проекта

  

[Дмитриев Андрей](https://github.com/dmi3ev1987)