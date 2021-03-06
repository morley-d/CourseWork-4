"""Класс DAO для фильмов"""

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.setup.db.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def add_in_favorites(self, user, mov_id):
        return self.dao.add_in_favorites(user, mov_id)

    def del_for_favorites(self, user, mov_id):
        return self.dao.del_for_favorites(user, mov_id)


    def get_all(self, **kwargs) -> list[Movie]:
        return self.dao.get_all(**kwargs)
