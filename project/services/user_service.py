import base64
import hashlib
import hmac

import jwt
from flask import abort

from project.constant import HASH_ALGO, HASH_SALT, HASH_ITERATIONS, JWT_SECRET, JWT_ALGO
from project.dao import UsersDAO

from project.dao.models.user import User
from project.exceptions import ItemNotFound, WrongPassword
from project.services.base import BaseService


class UsersService(BaseService[UsersDAO]):

    def token_decode(self, data):
        token = data.split("Bearer ")[-1]
        try:
            token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return token

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def partial_update(self, uid, data):
        #pk = uid['id']
        user = self.get_item(uid)

        if data.get('name'):
            user.name = data.get('name')
        if data.get('surname'):
            user.surname = data.get('surname')
        if data.get('favourite_genre'):
            user.favourite_genre = data.get('favourite_genre')

        self.dao.update(user)

    @staticmethod
    def __get_hash(password: str) -> str:

        hash_digest = hashlib.pbkdf2_hmac(
            HASH_ALGO,
            password.encode('utf-8'),
            HASH_SALT.encode('utf-8'),
            HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest).decode('utf-8')

    def update(self, uid, data):
        #pk = uid['id']
        user = self.get_item(uid)

        new_password = data.get('new_password')
        old_password = data.get('old_password')

        new_password_hash = self.__get_hash(password=new_password)
        print(f"новый сгенерированный хеш {new_password_hash}")
        print(f"cтарый хеш лежащий у пользователя {user.password_hash}")
        print(f"старый пароль который будет генерироваться в хеш и сравниватся с хешем юсера {old_password}")

        if not self.__compare_passwords(user.password_hash, old_password):
            raise WrongPassword

        user.password_hash = new_password_hash

        self.dao.update(user)



    @staticmethod
    def __compare_passwords(password_hash: str, old_password: str) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            HASH_ALGO,
            old_password.encode('utf-8'),
            HASH_SALT.encode('utf-8'),
            HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
