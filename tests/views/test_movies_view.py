import pytest

from project.setup.db.models import Movie, Genre, Director


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj = Movie(title="movie", description="description", trailer="trailer", year=2000, rating=8, genre_id=3, director_id=3)
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def genre3(self, db):
        obj = Genre(id=3, name="genre_№3")
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def director3(self, db):
        obj = Director(id=3, name="director_№3")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie, genre3, director3):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{"id": movie.id,
                                  "title": movie.title,
                                  "description": movie.description,
                                  "trailer": movie.trailer,
                                  "year": movie.year,
                                  "rating": movie.rating,
                                  "genre": {"id": movie.genre.id, "name": movie.genre.name},
                                  "director": {"id": movie.director.id, "name": movie.director.name}}]

    def test_movie_pages(self, client, movie):
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, movie, genre3, director3):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {"id": movie.id,
                                 "title": movie.title,
                                 "description": movie.description,
                                  "trailer": movie.trailer,
                                  "year": movie.year,
                                  "rating": movie.rating,
                                  "genre": {"id": movie.genre.id, "name": movie.genre.name},
                                  "director": {"id": movie.director.id, "name": movie.director.name}}

    def test_movie_not_found(self, client, movie):
        response = client.get("/movies/2/")
        assert response.status_code == 404
