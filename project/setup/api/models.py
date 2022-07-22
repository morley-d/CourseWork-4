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
    'genre_id': fields.Integer(required=True, max_length=100, example=1),
    'director_id': fields.Integer(required=True, max_length=100, example=2),
})
