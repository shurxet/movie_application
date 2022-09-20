import pytest

from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            title='test_title_1',
            description='test_description_1',
            trailer='test_trailer_1',
            year=2021,
            rating=7.2,
            genre_id=1,
            director_id=1
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def genre(self, db):
        obj = Genre(name="genre")
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def director(self, db):
        obj = Director(name="director")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie, genre, director):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [
            {
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "trailer": movie.trailer,
                "year": movie.year,
                "rating": movie.rating,
                "genre": {'id': movie.genre_id, 'name': genre.name},
                "director": {'id': movie.director_id, 'name': director.name}
            }
        ]

    def test_movie_pages(self, client, movie):
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, movie, genre, director):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "trailer": movie.trailer,
            "year": movie.year,
            "rating": movie.rating,
            "genre": {'id': movie.genre_id, 'name': genre.name},
            "director": {'id': movie.director_id, 'name': director.name}
        }

    def test_movie_not_found(self, client, movie):
        response = client.get("/movies/2/")
        assert response.status_code == 404
