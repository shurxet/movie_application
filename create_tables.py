from project.config import config
from project.data_base import db
from project.server import create_app


if __name__ == '__main__':
    with create_app(config).app_context():
        db.create_all()
