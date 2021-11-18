from werkzeug.exceptions import NotFound

from api.repositories.pagination_repository import pagination


class Repository:
    def __init__(self, obj, db):
        self.object = obj
        self.db = db

    def create(self, data):
        item = self.object()

        for key, value in data.items():
            setattr(item, key, value)

        self.db.add(item)
        self.db.commit()

        return item

    def find(self):
        query = self.db.query(self.object) \

        if self.object.created_at:
            query = query.order_by(self.object.created_at.desc())

        items = query.all()

        return items

    def find_one(self, id):
        item = self.db.query(self.object) \
            .filter(self.object.id == id) \
            .one()

        if not item:
            raise NotFound

        return item

    def find_with_pagination(self, page, limit):
        query = self.db.query(self.object)

        if self.object.created_at:
            query = query.order_by(self.object.created_at.desc())

        return pagination(query, page, limit)

    def update(self, id, data):
        item = self.find_one(id)

        for key, value in data.items():
            setattr(item, key, value)

        self.db.add(item)
        self.db.commit()

    def remove(self, id):
        item = self.find_one(id)

        self.db.delete(item)
        self.db.commit()
