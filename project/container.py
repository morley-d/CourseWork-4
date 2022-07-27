from project.dao import GenresDAO, DirectorsDAO
from project.dao.main import MoviesDAO
from project.dao.user import UserDAO

from project.services import GenresService, DirectorsService
from project.services.auth import AuthService
from project.services.movies_service import MoviesService
from project.services.user import UserService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)

