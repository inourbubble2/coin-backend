from flask_restplus import fields
from api.restplus import api

restaurant = api.model('Restaurant', {
    'id': fields.String(readOnly=True),
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

restaurant_create_request = api.model('RestaurantCreate', {
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float()
})

restaurant_update_request = api.model('RestaurantUpdate', {
    'id': fields.String(readOnly=True),
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float()
})