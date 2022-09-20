from sqlalchemy.orm import relationship

from project.dao.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey

from project.dao.models.director import Director
from project.dao.models.genre import Genre


class Movie(BaseModel):
    __tablename__ = 'movies'

    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(100), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float(100), nullable=False)
    genre_id = Column(Integer, ForeignKey(Genre.id))
    genre = relationship(Genre)
    director_id = Column(Integer, ForeignKey(Director.id))
    director = relationship(Director)

