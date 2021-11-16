from werkzeug.exceptions import NotFound, BadRequest
from database import use_database
from database.cafe import Cafe


@use_database
def create(db, data):
    cafe = Cafe()

    for key, value in data.items():
        if not getattr(cafe, key):
            raise BadRequest()
        setattr(cafe, key, value)

    db.add(cafe)
    db.commit()


@use_database
def find_one(db, cafe_id):
    cafe = db.query(Cafe)\
        .filter(Cafe.id == cafe_id)\
        .one()

    if not cafe:
        raise NotFound()

    return cafe


@use_database
def find(db, page, per_page, name, location):
    query = db.query(Cafe)

    if name:
        query = query.filter(Cafe.name.like(name))
    if location:
        query = query.filter(Cafe.location == location)

    cafes = query.offset((page - 1) * per_page)\
        .limit(per_page)\
        .all()

    return cafes


@use_database
def update(db, cafe_id, data):
    cafe = find_one(cafe_id)

    for key, value in data.items():
        if not getattr(cafe, key):
            raise BadRequest()
        setattr(cafe, key, value)

    db.add(cafe)
    db.commit()


@use_database
def remove(db, cafe_id):
    cafe = find_one(cafe_id)

    db.delete(cafe)
    db.commit()
