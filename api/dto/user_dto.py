from flask_restx import fields
from api.restx import api

user = api.model('User', {
    'id': fields.String(),
    'kakao_id': fields.String(),
    'nickname': fields.String(),
    'student_type': fields.String(),
    'student_year': fields.String(),

    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime(),
})

user_create_request = api.model('UserCreateRequest', {
    'kakao_id': fields.String(),
    'nickname': fields.String(),
})