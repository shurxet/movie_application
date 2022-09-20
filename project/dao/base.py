from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery


from sqlalchemy.orm import scoped_session, Session
from werkzeug.exceptions import NotFound

from project.dao.models.base import BaseModel



T = TypeVar('T', bound=BaseModel)

# class BaseDAO:
#     def __int__(self, session: Session):
#         self.session = session

class BaseDAO(Generic[T]):
    __model__ = BaseModel

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def get_all(self, page: Optional[int] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all() #order_by(desc(self.__model__.year)).all()


    # def get_by_email(self, email):
    #     return self._db_session.query(self.__model__).filter(self.__model__.email == email).first()


    def update(self, data):
        self._db_session.add(data)
        self._db_session.commit()

        return data



    # def delete(self, uid):
    #     user = self.get_by_id(uid)
    #
    #     self._db_session.delete(user)
    #     self._db_session.commit()
