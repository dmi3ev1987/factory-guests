from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


@app.route('/')
def my_index_view():
    return 'Это мой первый Flask-проект'


if __name__ == '__main__':
    app.run()
