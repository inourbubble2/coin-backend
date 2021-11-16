from flask_restplus import fields
from api.restplus import api

cafe = api.model('Cafe', {
    'id': fields.String(readOnly=True),

    'name': fields.String(),
    'description': fields.String(),
    'address': fields.String(),
    'open_hour': fields.String(),
    'contact': fields.String(),
    'link': fields.String(),

    'location': fields.String(),
    'star': fields.Integer(),

    'kakao_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float(),

    'created_by': fields.String(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

cafe_request = api.model('CafeRequest', {
    'name': fields.String(),
    'description': fields.String(),
    'address': fields.String(),
    'open_hour': fields.String(),
    'contact': fields.String(),
    'link': fields.String(),

    'location': fields.String(),
    'star': fields.Integer(),

    'kakao_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float(),
})