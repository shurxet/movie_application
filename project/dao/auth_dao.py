from project.dao.base import BaseDAO
from project.dao.models.user import User
from project.dao.serialization.auth import AuthUserSchema


class AuthDAO(BaseDAO):

    def create(self, email: str, password_hash: str) -> AuthUserSchema:
        new_user = User(
            email=email,
            password_hash=password_hash,
        )

        self._db_session.add(new_user)
        self._db_session.commit()

        return AuthUserSchema().dump(new_user)


    def get_by_email(self, email: str):
        user = self._db_session.query(User).filter(User.email == email).one_or_none()

        if user is not None:
            return user

        return None
