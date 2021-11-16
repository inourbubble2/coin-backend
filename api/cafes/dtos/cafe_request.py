from flask_restplus import fields
from api.restplus import api


cafe_request = api.model('CafeRequest', {
    'name': fields.String(required=True, example="964커피&너만보여크루아상 회기점"),
    'description': fields.String(example="#로스팅전문 #베이커리카페"),
    'address': fields.String(example="서울 동대문구 망우로21길 63 (우)02439"),
    'open_hour': fields.String(example="매일 08:00 ~ 22:00"),
    'contact': fields.String(example="02-1234-5678"),
    'link': fields.String(example="www.instagram.com/964__coffee"),

    'location': fields.String(example="front"),
    'star': fields.Integer(),

    'kakao_id': fields.String(required=True, example="682378583"),
    'latitude': fields.Float(example=127.052942),
    'longitude': fields.Float(example=37.5854582),
})