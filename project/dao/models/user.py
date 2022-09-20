from sqlalchemy import Column, String, ForeignKey, Integer


from project.dao.models.base import BaseModel
from project.dao.models.genre import Genre


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String)
    surname = Column(String)
    favourite_genre = Column(ForeignKey(Genre.id))
