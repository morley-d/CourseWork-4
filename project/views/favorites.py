from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service, user_service
from project.exceptions import ItemNotFound
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

favorites_ns = Namespace('favorites', description="Routes for working with films in the Favorites section")


@favorites_ns.route('/movies/')
class FavoritesView(Resource):
    @favorites_ns.expect(page_parser)
    @favorites_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get favorites movie.
        """
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = user_service.get_email_from_token(token)
            user = user_service.get_by_email(email)
        except ItemNotFound:
            pass
        # return movie_service.get_for_favorites(user)
        return user.favorite_movies


@favorites_ns.route('/movies/<int:mov_id>/')
class FavoriteView(Resource):
    @favorites_ns.response(404, 'Not Found')
    @favorites_ns.marshal_with(movie, code=200, description='OK')
    def post(self, mov_id: int):
        """
        Add movie in favorites.
        """
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = user_service.get_email_from_token(token)
            user = user_service.get_by_email(email)
        except ItemNotFound:
            pass
        return movie_service.add_in_favorites(user, mov_id)

    @favorites_ns.response(404, 'Not Found')
    @favorites_ns.marshal_with(movie, code=200, description='OK')
    def delete(self, mov_id: int):
        """
        Delete movie in favorites.
        """
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = user_service.get_email_from_token(token)
            user = user_service.get_by_email(email)
        except ItemNotFound:
            pass
        return movie_service.del_for_favorites(user, mov_id)
