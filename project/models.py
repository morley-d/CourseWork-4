from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)

    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)

    genre = relationship("Genre")
    director = relationship("Director")


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)
    name = Column(String(20))
    surname = Column(String(20))
    favorite_genre = Column(ForeignKey(Genre.id))
