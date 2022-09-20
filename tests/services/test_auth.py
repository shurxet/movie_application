from unittest.mock import patch

import pytest

from project.dao.models.user import User
from project.services import AuthService


class TestAuthService:

    @pytest.fixture()
    @patch('project.dao.AuthDAO')
    def auth_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_email.return_value = User(
            id=1,
            email='email',
            password_hash='cc7Ihb6WLtUpJ94saFOQf/b0r/hyLf0+AeCSodmh8aA=',
            name='test_name',
            surname='test_surname',
            favourite_genre=1
        )

        return dao

    @pytest.fixture()
    def auth_service(self, auth_dao_mock):
        return AuthService(dao=auth_dao_mock)

    def test_registration(self, auth_service):
        email = 'email'
        password = '111'

        auth_service.registration(email, password)

    def test_generate_tokens(self, auth_service):
        email = 'email'
        password = '111'

        auth_service.generate_tokens(email, password)

    def test_approve_refresh_token(self, auth_service):
        refresh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwiZW1haWwiOiJlbWFpbCIsIm5hbWUiOm51bGwsInN1cm5hbWUiOm51bGwsImV4cCI6MTY3NDc5MjE0NH0.w2pWyHwDFabx-tlAET_j0BabsGOTYGW4GaO70F3SD-Q'

        auth_service.approve_refresh_token(refresh_token)
