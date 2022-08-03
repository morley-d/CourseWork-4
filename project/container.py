"""Создание объектов DAO и сервисов, который далее будет импортироваться
    в другие модули"""

from project.dao import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO
from project.services import GenresService, DirectorsService, MoviesService, UserService
from project.services.auth import AuthService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)

