from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service
from project.dao.serialization.auth import AuthRegistrationRequest


api = Namespace('auth')



@api.route("/register/")
class RegistrationView(Resource):
    def post(self):
        data = request.json
        validated_data = AuthRegistrationRequest().load(data)

        auth_service.registration(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return '', 201


@api.route("/login/")
class LoginView(Resource):
    def post(self):
        data = request.json
        validated_data = AuthRegistrationRequest().load(data)

        tokens = auth_service.generate_tokens(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return tokens, 200


    def put(self):
        data = request.json
        token = data.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 204


