from unittest.mock import patch

import pytest


from project.dao.models.user import User
from project.exceptions import ItemNotFound
from project.services import UsersService


class TestUsersService:

    @pytest.fixture()
    @patch('project.dao.UsersDAO')
    def users_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = User(
            id=1,
            email='email',
            password_hash='cc7Ihb6WLtUpJ94saFOQf/b0r/hyLf0+AeCSodmh8aA=',
            name='test_name',
            surname='test_surname',
            favourite_genre=1
        )

        return dao

    @pytest.fixture()
    def users_service(self, users_dao_mock):
        return UsersService(dao=users_dao_mock)

    @pytest.fixture
    def user(self, db):
        obj = User(
            email='email',
            password_hash='hash',
            name='user_name',
            surname='user_surname',
            favourite_genre=1,
        )
        db.session.add(obj)
        db.session.commit()
        return obj


    def test_get_user(self, user, users_service):
        assert users_service.get_item(user.id)

    def test_user_not_found(self, users_dao_mock, users_service):
        users_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            users_service.get_item(10)

    def test_user_update(self, user, users_service):
        data = {
            'new_password': '222',
            'old_password': '111',
        }
        users_service.update(user.id, data)

    def test_user_token_decode(self, users_service):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwiZW1haWwiOiJlbWFpbCIsIm5hbWUiOm51bGwsInN1cm5hbWUiOm51bGwsImV4cCI6MTY3NDc5MjE0NH0.w2pWyHwDFabx-tlAET_j0BabsGOTYGW4GaO70F3SD-Q"
        assert users_service.token_decode(token)


