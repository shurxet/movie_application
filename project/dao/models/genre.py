from project.dao.models.base import BaseModel
from sqlalchemy import Column, String


class Genre(BaseModel):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)