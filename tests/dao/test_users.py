import pytest

from project.dao import UsersDAO
from project.dao.models.user import User


class TestUsersDAO:

    @pytest.fixture
    def users_dao(self, db):
        return UsersDAO(db.session)

    @pytest.fixture
    def user_1(self, db):
        u = User(
            email="Почта пользователя",
            password_hash="Хеш пользователя",
            name="Имя пользователя",
            surname="Фамилия пользователя",
            favourite_genre=1
        )
        db.session.add(u)
        db.session.commit()
        return u


    def test_get_user_by_id(self, user_1, users_dao):
        assert users_dao.get_by_id(user_1.id) == user_1

    def test_get_user_by_id_not_found(self, users_dao):
        assert not users_dao.get_by_id(1)

    def test_update(self, user_1, users_dao):
        users_dao.update(user_1)


