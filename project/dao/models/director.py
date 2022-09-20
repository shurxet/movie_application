from project.dao.models.base import BaseModel
from sqlalchemy import Column, String


class Director(BaseModel):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)
