from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def add_in_favorites(self, user, mov_id):
        movie = self._db_session.query(self.__model__).get(mov_id)
        user.favorite_movies.append(movie)
        return self._db_session.commit()

    def del_for_favorites(self, user, mov_id):
        movie = self._db_session.query(self.__model__).get(mov_id)
        user.favorite_movies.remove(movie)
        return self._db_session.commit()

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page != None and status == "new":
            try:
                sort = stmt.order_by(self.__model__.year.desc())
                return sort.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        if status == "new" or status == "New":
            try:
                return stmt.order_by(self.__model__.year.desc()).all()
            except NotFound:
                return []
        return stmt.all()

    def get_by_email(self, email):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        return stmt.filter(self.__model__.email == email).first()

    def create_user(self, data):
        user = self.__model__(**data)
        self._db_session.add(user)
        self._db_session.commit()
        return user

    def update_user(self, user_data, email):
        user = self.get_by_email(email)
        user.name = user_data.get("name")
        user.surname = user_data.get("surname")
        user.favorite_genre = user_data.get("favorite_genre")
        self._db_session.add(user)
        self._db_session.commit()

    def update_password(self, user_data, user):
        user.password = user_data.get("password")
        self._db_session.add(user)
        self._db_session.commit()
