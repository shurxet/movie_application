from project.dao import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO, AuthDAO, FavoritesDAO

from project.data_base import db

from project.services import GenresService, DirectorsService, MoviesService, UsersService, AuthService, FavoritesService

# DAO


genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
auth_dao = AuthDAO(db.session)
favorite_dao = FavoritesDAO(db.session)

# Services
genre_service = GenresService(genre_dao)
director_service = DirectorsService(director_dao)
movie_service = MoviesService(movie_dao)
user_service = UsersService(user_dao)
auth_service = AuthService(auth_dao)
favorite_service = FavoritesService(favorite_dao)
