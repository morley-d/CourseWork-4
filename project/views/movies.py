from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

movies_ns = Namespace('movies', description="Routes for working with movies")


@movies_ns.route('/')
class DirectorsView(Resource):
    @movies_ns.doc(description='Get all movies')
    @movies_ns.expect(page_parser)
    @movies_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        return movie_service.get_all(**page_parser.parse_args())


@movies_ns.route('/<int:dir_id>/')
class DirectorView(Resource):
    @movies_ns.doc(description='Get movie by id')
    @movies_ns.response(404, 'Not Found')
    @movies_ns.marshal_with(movie, code=200, description='OK')
    def get(self, dir_id: int):
        return movie_service.get_item(dir_id)
