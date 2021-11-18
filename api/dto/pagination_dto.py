from flask_restx import fields
from api.restx import api

meta = api.model('meta', {
    "current_page": fields.Integer(),
    "items_per_page": fields.Integer(),
    'item_count': fields.Integer(),
    'total_items': fields.Integer(),
    'total_pages': fields.Integer(),
})

href = api.model('href', {
    'href': fields.String(),
})

_links = api.model('_links', {
    'self': fields.Nested(href, skip_none=True),
    'prev': fields.Nested(href, skip_none=True),
    'next': fields.Nested(href, skip_none=True)
})