from project.dao.models.movie import Movie
from project.dao.models.user import User
from project.data_base import db


class Favorite(db.Model):
    __tablename__ = 'favorites'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    user = db.relationship(User)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id, ondelete='CASCADE'), primary_key=True)
    movie = db.relationship(Movie)

