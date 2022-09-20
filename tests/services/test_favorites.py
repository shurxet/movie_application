from unittest.mock import patch

import pytest

from project.dao.models.favorite import Favorite
from project.dao.models.movie import Movie
from project.exceptions import ItemNotFound
from project.services import FavoritesService


class TestFavoritesService:

    @pytest.fixture()
    @patch('project.dao.FavoritesDAO')
    def favorites_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_all_favorites.return_value = [
            Movie(
                id=1,
                title='test_title_1',
                description='test_description_1',
                trailer='test_trailer_1',
                year=2021,
                rating=7.2,
                genre_id=2,
                director_id=2
            ),
            Movie(
                id=2,
                title='test_title_2',
                description='test_description_2',
                trailer='test_trailer_2',
                year=2022,
                rating=7.3,
                genre_id=3,
                director_id=3
            )
        ]
        return dao

    @pytest.fixture()
    def favorites_service(self, favorites_dao_mock):
        return FavoritesService(dao=favorites_dao_mock)

    @pytest.fixture
    def favorite(self, db):
        obj = Favorite(user_id=1, movie_id=1)
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_favorites(self, favorites_dao_mock, favorites_service, favorite):
        favorite = favorites_service.get_all_favorites(favorite.user_id)
        assert len(favorite) == 2
        assert favorite == favorites_dao_mock.get_all_favorites.return_value

    def test_add_favorite(self, favorites_service, favorite):
        favorites_service.add_favorite(favorite.user_id, favorite.movie_id)

    def test_delete_favorites(self, favorites_service, favorite):
        favorites_service.delete_favorites(favorite.user_id, favorite.movie_id)

