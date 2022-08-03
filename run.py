"""Основной файл приложения"""

import os
os.environ['FLASK_ENV'] = 'development'
from project.config import config
from project.server import create_app, db


app = create_app(config)


if __name__ == '__main__':
    app.run(port=7777)
