
__all__ = [
    'GenresDAO',
    'DirectorsDAO',
    'MoviesDAO',
    'UsersDAO',
    'AuthDAO',
    'FavoritesDAO'
]

from project.dao.auth_dao import AuthDAO
from project.dao.director_dao import DirectorsDAO
from project.dao.favorite_dao import FavoritesDAO
from project.dao.genre_dao import GenresDAO
from project.dao.movie_dao import MoviesDAO
from project.dao.user_dao import UsersDAO
