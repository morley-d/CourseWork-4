"""Создание и настройка эеземпляра Flask приложения"""

from flask import Flask, jsonify, render_template
# from flask_cors import CORS
from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup.db import db
from project.views.auth import auth_ns
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from project.views.movies import movies_ns
from project.views.user import user_ns
from project.views.favorites import favorites_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')

    # CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favorites_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
