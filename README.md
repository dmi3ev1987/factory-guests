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
flask db init  # Создать репозиторий сценариев миграций.

flask db migrate -m "Name of mirgration"  # Создать миграции.

flask db upgrade  # Применить миграции.
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


### Автор проекта

[Дмитриев Андрей](https://github.com/dmi3ev1987)
