import base64
import os
from pathlib import Path
from typing import Type

# DATABASE_PATH = os.path.join(os.getcwd(), 'data.db')


# class Config:
#
#     JWT_SECRET = 'secret key'
#     JSON_AS_ASCII = False
#
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
#
#     RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
#
#     TOKEN_EXPIRE_MINUTES = 15
#     TOKEN_EXPIRE_DAYS = 130
#
#     JWT_ALGO = 'HS256'
#     HASH_NAME = 'sha256'
#     HASH_SALT = 'salt'
#     HASH_ITERATIONS = 100_000


BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000

    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR.joinpath('data.db').as_posix()


class ProductionConfig(BaseConfig):
    DEBUG = False
    # TODO: дополнить конфиг


class ConfigFactory:
    os.environ['FLASK_ENV'] = "development" #'testing' #'development'
    flask_env = os.getenv('FLASK_ENV')

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:
        if cls.flask_env == 'development':
            return DevelopmentConfig
        elif cls.flask_env == 'production':
            return ProductionConfig
        elif cls.flask_env == 'testing':
            return TestingConfig
        raise NotImplementedError


config = ConfigFactory.get_config()
