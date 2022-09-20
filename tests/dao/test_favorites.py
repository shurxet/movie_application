import pytest

from project.dao import FavoritesDAO
from project.dao.models.favorite import Favorite
from project.dao.models.movie import Movie


class TestFavoritesDAO:

    @pytest.fixture
    def favorites_dao(self, db):
        return FavoritesDAO(db.session)

    @pytest.fixture
    def favorite_1(self, db):
        f = Favorite(
            user_id=1,
            movie_id=1
        )
        db.session.add(f)
        db.session.commit()

        return f

    @pytest.fixture
    def movie_1(self, db):
        m = Movie(
            title="Первый фильм",
            description="описание первого фильма",
            trailer="Трейлер первого фильма",
            year=2021,
            rating=7.5,
            genre_id=1,
            director_id=1
        )
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def user_id(self, db):
        uid = 1

        return uid

    @pytest.fixture
    def movie_id(self, db):
        mid = 1

        return mid


    def test_create(self, user_id, movie_id, favorites_dao):
        assert favorites_dao.create(user_id, movie_id)

    def test_get_all_favorites(self, user_id, movie_1, favorite_1, favorites_dao):
        assert favorites_dao.get_all_favorites(favorite_1.user_id) == [movie_1]

    def test_get_one_favorite(self, user_id, movie_id, favorite_1, favorites_dao):
        assert favorites_dao.get_one_favorite(user_id, movie_id) == favorite_1

    def test_get_one_favorite_not_found(self, favorites_dao):
        assert not favorites_dao.get_one_favorite(1, 1)

    def test_delete_favorites(self, user_id, movie_id, favorite_1, favorites_dao):
        favorites_dao.delete_favorites(user_id, movie_id)

