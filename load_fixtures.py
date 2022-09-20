from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from project.config import config
from project.dao.models.base import BaseModel
from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.data_base import db

from project.server import create_app
from utils import read_json


def load_data(data: List[Dict[str, Any]], model: Type[BaseModel]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['genres'], Genre)

        with suppress(IntegrityError):
            db.session.commit()

    with app.app_context():
        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['directors'], Director)

        with suppress(IntegrityError):
            db.session.commit()

    with app.app_context():
        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['movies'], Movie)

        with suppress(IntegrityError):
            db.session.commit()
