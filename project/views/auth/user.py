from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user


api = Namespace('user')


@api.route('/')
class UserView(Resource):
    #@auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self):
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        return user_service.get_item(uid)

    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=206, description='OK')
    def patch(self):
        data_update = request.json
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        user_service.partial_update(uid, data_update)

        return ''


@api.route('/password/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=204, description='OK')
    def put(self):
        data_update = request.json
        token = request.headers['Authorization']
        user_data = user_service.token_decode(token)
        uid = user_data['id']

        user_service.update(uid, data_update)

        return ''





