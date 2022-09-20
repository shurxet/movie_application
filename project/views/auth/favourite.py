from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, favorite_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

api = Namespace('favorites')


@api.route("/movies/")
class FavoritesView(Resource):
    #@auth_required
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all favorites.
        """
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        return favorite_service.get_all_favorites(uid, **page_parser.parse_args())


@api.route("/movies/<int:movie_id>/")
class FavoriteView(Resource):
    #@auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def post(self, movie_id: int):
        """
        Add favorite.
        """
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        favorite_service.add_favorite(uid, movie_id)

        return '', 200

    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def delete(self, movie_id: int):
        """
        Delete favorite.
        """

        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        return favorite_service.delete_favorites(uid=uid, movie_id=movie_id)










