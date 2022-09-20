from project.config import config
from project.dao.models.director import Director
from project.dao.models.favorite import Favorite
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.data_base import db
from project.server import create_app

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "Favorite": Favorite
    }


if __name__ == '__main__':
    app.run(port=25000, debug=True)
