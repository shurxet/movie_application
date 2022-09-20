import pytest

from project.dao import AuthDAO
from project.dao.models.user import User


class TestAuthDAO:

    @pytest.fixture
    def auth_dao(self, db):
        return AuthDAO(db.session)

    @pytest.fixture
    def user_1(self, db):
        u = User(
            email="Почта пользователя",
            password_hash="Хеш пользователя"
        )
        db.session.add(u)
        db.session.commit()

        return u

    @pytest.fixture
    def user_email(self, db):
        email = "user@mail.ru"

        return email

    @pytest.fixture
    def user_password_hash(self, db):
        password_hash = "хеш"

        return password_hash

    def test_create(self, user_email, user_password_hash, auth_dao):
        assert auth_dao.create(user_email, user_password_hash)

    def test_get_by_email(self, user_1, auth_dao):
        assert auth_dao.get_by_email(user_1.email) == user_1

    def test_get_by_email_not_found(self, auth_dao):

        assert not auth_dao.get_by_email('')
