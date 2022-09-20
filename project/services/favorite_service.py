from typing import Optional

from project.dao import FavoritesDAO
from project.dao.models.favorite import Favorite
from project.services.base import BaseService


class FavoritesService(BaseService[FavoritesDAO]):

    def add_favorite(self, user_id: int, movie_id: int):
        self.dao.create(user_id, movie_id)

    def get_all_favorites(self, uid: int, page: Optional[int] = None) -> list[Favorite]:
        return self.dao.get_all_favorites(uid=uid, page=page)

    def delete_favorites(self, uid: int, movie_id: int):
        self.dao.delete_favorites(uid, movie_id)


