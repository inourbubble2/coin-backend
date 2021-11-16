import logging

from flask import request
from flask_restplus import Resource
from api.restaurants.business import read_restaurants, read_restaurant, create_restaurant, update_restaurant, delete_restaurant
from api.restaurants.serializers import restaurant, restaurant_create_request, restaurant_update_request
from api.restaurants.parsers import pagination_arguments
from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('restaurants', description='Operations related to restaurants')


@ns.route('/')
class RestaurantCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(restaurant)
    def get(self):
        data = request.json or {}

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        restaurants = read_restaurants(data, page, per_page)
        return restaurants

    @api.expect(restaurant_create_request)
    @api.response(201, 'Restaurant successfully created.')
    def post(self):
        data = request.json or {}
        create_restaurant(data)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Restaurant not found.')
class RestaurantItem(Resource):

    @api.marshal_with(restaurant)
    def get(self, id):
        restaurant = read_restaurant(id)
        return restaurant

    @api.expect(restaurant_update_request)
    @api.response(204, 'Restaurant successfully updated.')
    def patch(self, id):
        data = request.json or {}
        update_restaurant(id, data)
        return None, 204

    @api.response(204, 'Restaurant successfully deleted.')
    def delete(self, id):
        delete_restaurant(id)
        return None, 204

