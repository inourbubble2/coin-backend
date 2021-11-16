from flask_restplus import fields
from api.restplus import api
from api.cafes.model import LocationEnum


class Location(fields.Raw):
    def format(self, value):
        if value == LocationEnum.front:
            return "정문"
        elif value == LocationEnum.back:
            return "후문"
        elif value == LocationEnum.side:
            return "쪽문"
        elif value == LocationEnum.hoegi:
            return "회기"


cafe_response = api.model('Cafe', {
    'id': fields.String(readOnly=True),

    'name': fields.String(),
    'description': fields.String(),
    'address': fields.String(),
    'open_hour': fields.String(),
    'contact': fields.String(),
    'link': fields.String(),

    'location': Location(attribute='location'),
    'star': fields.Integer(),

    'kakao_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float(),

    'created_by': fields.String(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})
