"""Модели сущностей, наследуемые от базовой модели"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from project.setup.db import base_model
from project.setup.db import db


class Genre(base_model.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(base_model.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


favorites = db.Table('favorites',
                     Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                     Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)
                     )


class Movie(base_model.Base):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    description = Column(String(100))
    trailer = Column(String(100))
    year = Column(Integer)
    rating = Column(Integer, nullable=False)

    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)

    genre = relationship("Genre")
    director = relationship("Director")


class User(base_model.Base):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(20))
    surname = Column(String(20))
    favorite_genre = Column(ForeignKey(Genre.id))
    favorite_movies = relationship('Movie', secondary=favorites, backref=backref('users'))
