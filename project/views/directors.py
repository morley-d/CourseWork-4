from flask import request
from flask_restx import Namespace, Resource
from project.container import director_service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser

directors_ns = Namespace('directors', description="Routes for working with directors")


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.doc(description='Get all directors')
    @directors_ns.expect(page_parser)
    @directors_ns.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        # a = request.args
        return director_service.get_all(**page_parser.parse_args())


@directors_ns.route('/<int:dir_id>/')
class DirectorView(Resource):
    @directors_ns.doc(description='Get director by id')
    @directors_ns.response(404, 'Not Found')
    @directors_ns.marshal_with(director, code=200, description='OK')
    def get(self, dir_id: int):
        return director_service.get_item(dir_id)

