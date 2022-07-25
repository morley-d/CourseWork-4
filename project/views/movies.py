from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class DirectorsView(Resource):
    @movie_ns.expect(page_parser)
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        return movie_service.get_all(**page_parser.parse_args())


@movie_ns.route('/<int:dir_id>/')
class DirectorView(Resource):
    @movie_ns.response(404, 'Not Found')
    @movie_ns.marshal_with(movie, code=200, description='OK')
    def get(self, dir_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(dir_id)
