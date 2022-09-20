from typing import Optional, List

from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.dao.models.favorite import Favorite
from project.dao.models.movie import Movie


class FavoritesDAO(BaseDAO[Favorite]):
    __model__ = Favorite

    def create(self, user_id: int, movie_id: int):
        new_favorite = Favorite(
            user_id=user_id,
            movie_id=movie_id,
        )

        self._db_session.add(new_favorite)
        self._db_session.commit()

        return new_favorite

    def get_all_favorites(self, uid: int, page: Optional[int] = None) -> List[Movie]:
        stmt: BaseQuery = self._db_session.query(Movie).join(Favorite).filter(Favorite.user_id == uid)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_one_favorite(self, user_id: int, movie_id: int):

        favorite = self._db_session.query(
            Favorite
        ).filter(
            Favorite.user_id == user_id
            and
            Favorite.movie_id == movie_id
        ).first()

        return favorite

        # if favorite is not None:
        #     return favorite
        #
        # return None


    def delete_favorites(self, uid: int, movie_id: int):
        favorite = self.get_one_favorite(uid, movie_id)

        self._db_session.delete(favorite)
        self._db_session.commit()

