import logging

from flask import request
from flask_restx import Resource
from api.services.user_service import UserService
from api.dto.user_dto import user, user_create_request
from api.restx import api

log = logging.getLogger(__name__)
service = UserService()

ns = api.namespace('users', description='Operations related to users')


@ns.route('/')
class UserCollection(Resource):

    @api.expect(user_create_request)
    @api.marshal_with(user)
    def post(self):
        data = request.json or {}
        user = service.create(data)

        return user, 201