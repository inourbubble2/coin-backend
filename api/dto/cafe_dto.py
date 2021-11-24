from flask_restx import fields
from api.restx import api
from database.cafe import LocationEnum
from api.dto.pagination_dto import meta


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


cafe = api.model('Cafe', {
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

    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

paginated_cafe = api.model('PaiginatedCafe', {
    "items": fields.Nested(cafe, skip_none=True),
    "meta": fields.Nested(meta, skip_none=True)
})

cafe_create_request = api.model('CafeCreateRequest', {
    'name': fields.String(required=True, example="964커피&너만보여크루아상 회기점"),
    'description': fields.String(example="#로스팅전문 #베이커리카페"),
    'address': fields.String(required=True, example="서울 동대문구 망우로21길 63 (우)02439"),
    'open_hour': fields.String(example="매일 08:00 ~ 22:00"),
    'contact': fields.String(example="02-1234-5678"),
    'link': fields.String(example="www.instagram.com/964__coffee"),

    'location': fields.String(example="front"),
    'star': fields.Integer(),

    'kakao_id': fields.String(required=True, example="682378583"),
    'latitude': fields.Float(example=127.052942),
    'longitude': fields.Float(example=37.5854582),

    'creator_id': fields.String(),
    'creator_nickname': fields.String(),
})

cafe_update_request = api.model('CafeUpdateRequest', {
    'name': fields.String(rexample="964커피&너만보여크루아상 회기점"),
    'description': fields.String(example="#로스팅전문 #베이커리카페"),
    'address': fields.String(example="서울 동대문구 망우로21길 63 (우)02439"),
    'open_hour': fields.String(example="매일 08:00 ~ 22:00"),
    'contact': fields.String(example="02-1234-5678"),
    'link': fields.String(example="www.instagram.com/964__coffee"),

    'location': fields.String(example="front"),
    'star': fields.Integer(),

    'kakao_id': fields.String(example="682378583"),
    'latitude': fields.Float(example=127.052942),
    'longitude': fields.Float(example=37.5854582),
})

kakao_cafe = api.model('KakaoCafe', {
    'address_name': fields.String(),
    'road_address_name': fields.String(),
    'category_name': fields.String(),
    'phone': fields.String(),
    'place_name': fields.String(),
    'place_url': fields.String(),
    'x': fields.Float(),
    'y': fields.Float(),
})