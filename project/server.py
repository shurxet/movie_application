from flask import Flask, jsonify, render_template
from flask_cors import CORS

from project.data_base import db
from project.exceptions import BaseServiceError
from project.setup.api import api

from project.views import auth_ns, genres_ns, user_ns, directors_ns, movies_ns, favorite_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.app_context().push()

    @app.route('/')
    def index():
        return render_template('index.html')

    #CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(favorite_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
