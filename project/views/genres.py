from flask import request
from flask_restx import Namespace, Resource

from project.container import genre_service
from project.setup.api.models import genre
from project.setup.api.parsers import page_parser

genres_ns = Namespace('genres', description="Routes for working with genres")


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.doc(description='Get all genres')
    @genres_ns.expect(page_parser)
    @genres_ns.response(404, 'Not Found')
    @genres_ns.marshal_with(genre, as_list=True, code=200, description='Success')
    def get(self):
        return genre_service.get_all(**page_parser.parse_args())


@genres_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @genres_ns.doc(description='Get genre by id')
    @genres_ns.response(404, 'Not Found')
    @genres_ns.marshal_with(genre, code=200, description='Success')
    def get(self, genre_id: int):
        return genre_service.get_item(genre_id)
