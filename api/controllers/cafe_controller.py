import logging

from flask import request
from flask_restx import Resource
from api.services.cafe_service import CafeService
from api.dto.cafe_dto import cafe, paginated_cafe, cafe_update_request, cafe_create_request, kakao_cafe
from api.parser import pagination_arguments, cafe_search_arguments, kakao_cafe_search_arguments
from api.restx import api

log = logging.getLogger(__name__)
cafe_service = CafeService()

ns = api.namespace('cafes', description='Operations related to cafes')


@ns.route('/')
class CafeCollection(Resource):

    @api.expect(pagination_arguments, cafe_search_arguments)
    @api.marshal_with(paginated_cafe)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 20)

        args = cafe_search_arguments.parse_args(request)
        name = args.get('name')
        location = args.get('location')

        cafes = cafe_service.find_with_pagination_and_arguments(page, per_page, name, location)
        return cafes

    @api.expect(cafe_create_request, validate=True)
    @api.response(201, 'Cafe successfully created.')
    def post(self):
        data = request.json or {}
        cafe_service.create(data)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Cafe not found.')
class CafeItem(Resource):

    @api.marshal_with(cafe)
    def get(self, id):
        cafe = cafe_service.find_one(id)
        return cafe

    @api.expect(cafe_update_request, validate=True)
    @api.response(204, 'Cafe successfully updated.')
    def patch(self, id):
        data = request.json or {}
        cafe_service.update(id, data)
        return None, 204

    @api.response(204, 'Cafe successfully deleted.')
    def delete(self, id):
        cafe_service.remove(id)
        return None, 204


@ns.route('/kakao')
@api.response(404, 'Kakao Cafe not found.')
class KakaoCafeItem(Resource):

    @api.expect(kakao_cafe_search_arguments)
    @api.marshal_list_with(kakao_cafe)
    def get(self):
        args = kakao_cafe_search_arguments.parse_args()
        name = args.get('name', '')

        cafes = cafe_service.find_cafe_from_kakao(name)
        return cafes, 200


