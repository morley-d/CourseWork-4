from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Тарантино'),
    'description': fields.String(required=True, max_length=100, example='Описание фильма'),
    'trailer': fields.String(required=True, max_length=100, example='Трейлер'),
    'year': fields.Integer(required=True, max_length=100, example=2012),
    'rating': fields.Integer(required=True, max_length=100, example=10),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user_api_model: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='xxx@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='12345'),
    'name': fields.String(required=True, max_length=100, example='Тина'),
    'surname': fields.String(required=True, max_length=100, example='Тарантино'),
    'favorite_genre': fields.String(required=True, max_length=100, example='Комедия'),
})
