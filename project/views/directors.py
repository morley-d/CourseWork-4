from flask import request, make_response
from flask_restx import Resource, Namespace
from sqlalchemy.orm.exc import UnmappedInstanceError

# from app.dao.model.director import DirectorSchema
# from app.decorators import auth_required, admin_required
# from app.implemented import director_service
from project.container import director_service

director_ns = Namespace('directors')

"""Роуты для режисеров"""

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Получение всех режиссеров"""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        """Добавление нового режиссера"""
        req_json = request.json
        new_director = director_service.create(req_json)
        response = make_response("", 201)
        response.headers['location'] = f"/{director_ns.path}/{new_director.id}"
        return response


@director_ns.route('/<int:dir_id>')
class DirectorView(Resource):
    def get(self, dir_id: int):
        """Получение режиссера по id"""
        r = director_service.get_one(dir_id)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, dir_id: int):
        """Обновление режиссера"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = dir_id
        director_service.update(req_json)
        return "", 204

    def delete(self, dir_id: int):
        """Удаление режиссера по id"""
        try:
            director_service.delete(dir_id)
        except UnmappedInstanceError:
            return "Такого режиссера нет", 404
        return "", 204

#####

from flask_restx import Namespace, Resource

from project.container import director_service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.expect(page_parser)
    @director_ns.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return director_service.get_all(**page_parser.parse_args())


@director_ns.route('/<int:dir_id>/')
class DirectorView(Resource):
    @director_ns.response(404, 'Not Found')
    @director_ns.marshal_with(director, code=200, description='OK')
    def get(self, dir_id: int):
        """
        Get director by id.
        """
        return director_service.get_item(dir_id)

