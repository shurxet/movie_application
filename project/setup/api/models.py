from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Название жанра'),
})


director: Model = api.model('Режиссёр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Имя и Фамилия Режиссёра'),
})


movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название фильма'),
    'description': fields.String(required=True, max_length=1000, example='Сюжет фильма'),
    'trailer': fields.String(required=True, max_length=100, example='Трейлер к фильму'),
    'year': fields.Integer(required=True, max_length=100, example='Год выхода фильма в прокат'),
    'rating': fields.Float(required=True, max_length=100, example='Рейтинг фильма'),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
    # 'genre': fields.String(attribute='genre.name'),
    # 'director': fields.String(attribute='director.name')
})


user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='Почта пользователя'),
    'name': fields.String(required=True, max_length=100, example='Имя пользователя'),
    'surname': fields.String(required=True, max_length=100, example='Фамилия пользователя'),
    'favourite_genre': fields.Integer()
})

# favorite: Model = api.model('Избранное', {
#     'id': fields.Integer(required=True, example=1),
#     'movie_id': fields.String(attribute='movie.name'),
#     'user_id': fields.Integer()
# })


