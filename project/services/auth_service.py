import base64
import calendar
import datetime
import hashlib
import hmac
from typing import Optional, Dict

import jwt
from flask import abort

from project.constant import JWT_SECRET, JWT_ALGO, HASH_ALGO, HASH_SALT, HASH_ITERATIONS
from project.dao.auth_dao import AuthDAO
from project.dao.serialization.auth import AuthUserSchema
from project.exceptions import UserNotFound, WrongPassword
from project.services.base import BaseService


class AuthService(BaseService[AuthDAO]):

    @staticmethod
    def __get_hash(password: str) -> str:

        hash_digest = hashlib.pbkdf2_hmac(
            HASH_ALGO,
            password.encode('utf-8'),
            HASH_SALT.encode('utf-8'),
            HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest).decode('utf-8')

    def registration(self, email: str, password: str) -> AuthUserSchema:

        password_hash = self.__get_hash(password=password)

        return self.dao.create(email=email, password_hash=password_hash)

    def generate_tokens(self, email: str, password: str, is_refresh=False):

        user = self.dao.get_by_email(email=email)
        if user is None:
            raise UserNotFound  # abort(404)
        if not is_refresh:

            if not self.__compare_passwords(user.password_hash, password):
                raise WrongPassword  # abort(400)

        data = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "surname": user.surname
        }
        # 30 min access_token TTL (time to live)
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        # 130 days for refresh_token TTL (time to live)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    @staticmethod
    def __compare_passwords(password_hash: str, other_password: str) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            HASH_ALGO,
            other_password.encode('utf-8'),
            HASH_SALT.encode('utf-8'),
            HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGO])
        email = data.get("email")

        return self.generate_tokens(email, None, is_refresh=True)


