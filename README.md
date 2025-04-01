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

## Создать БД sqlite

```
flask shell
```

После вход в shell вести команды по очереди:

```
>>> from guests_app import db
>>> db.create_all()
>>> quit()
```


### Автор проекта

[Дмитриев Андрей](https://github.com/dmi3ev1987)
