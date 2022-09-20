import json

import pytest

from project.dao.models.director import Director
from project.dao.models.favorite import Favorite
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.dao.models.user import User


class TestFavoritesView:
    @pytest.fixture
    def favorite(self, db):
        obj = Favorite(user_id=1, movie_id=1)
        db.session.add(obj)
        db.session.commit()
        return obj

    # @pytest.fixture
    # def user(self, db):
    #     obj = User(
    #         email='email',
    #         password_hash='hash',
    #         name='user_name',
    #         surname='user_surname',
    #         favourite_genre=1,
    #     )
    #     db.session.add(obj)
    #     db.session.commit()
    #     return obj

    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            title='test_title_2',
            description='test_description_2',
            trailer='test_trailer_2',
            year=2022,
            rating=7.3,
            genre_id=3,
            director_id=3
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

    def test_many(self, client, favorite, movie, genre, director):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{
                "id": favorite.movie_id,
                "title": movie.title,
                "description": movie.description,
                "trailer": movie.trailer,
                "year": movie.year,
                "rating": movie.rating,
                "genre": {'id': None, 'name': None},
                "director": {'id': None, 'name': None}
            }]


    def test_favorite(self, client, movie, genre, director, favorite):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {
            "id": favorite.movie_id,
            "title": movie.title,
            "description": movie.description,
            "trailer": movie.trailer,
            "year": movie.year,
            "rating": movie.rating,
            "genre": {'id': None, 'name': None},
            "director": {'id': None, 'name': None}}

    def test_favorite_not_found(self, client, favorite):
        response = client.get("/movies/2/")
        assert response.status_code == 404



