import logging

from flask import request
from flask_restplus import Resource
from api.cafes.business import read_cafes, read_cafe, create_cafe, update_cafe, delete_cafe
from api.cafes.dtos.cafe_response import cafe_response
from api.cafes.dtos.cafe_request import cafe_request
from api.cafes.parsers import pagination_arguments, cafe_search_arguments
from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('cafes', description='Operations related to cafes')


@ns.route('/')
class CafeCollecton(Resource):

    @api.expect(pagination_arguments, cafe_search_arguments)
    @api.marshal_list_with(cafe_response)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 20)

        args = cafe_search_arguments.parse_args(request)
        name = args.get('name')
        location = args.get('location')

        cafes = read_cafes(page, per_page, name, location)
        return cafes

    @api.expect(cafe_request)
    @api.response(201, 'Cafe successfully created.')
    def post(self):
        data = request.json or {}
        create_cafe(data)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Cafe not found.')
class CafeItem(Resource):

    @api.marshal_with(cafe_response)
    def get(self, id):
        cafe = read_cafe(id)
        return cafe

    @api.expect(cafe_request)
    @api.response(204, 'Cafe successfully updated.')
    def patch(self, id):
        data = request.json or {}
        update_cafe(id, data)
        return None, 204

    @api.response(204, 'Cafe successfully deleted.')
    def delete(self, id):
        delete_cafe(id)
        return None, 204






