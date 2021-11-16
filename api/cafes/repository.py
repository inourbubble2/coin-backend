from database import use_database
from api.cafes.model import Cafe


@use_database
def create(db, data):
    cafe = Cafe()

    for key, value in data.items():
        setattr(cafe, key, value)

    db.add(cafe)
    db.commit()


@use_database
def select_one(db, cafe_id):
    cafe = db.query(Cafe)\
        .filter(Cafe.id == cafe_id)\
        .one()

    return cafe


@use_database
def select_all(db, page, per_page, name, location):
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
    cafe = select_one(cafe_id)

    for key, value in data.items():
        setattr(cafe, key, value)

    db.add(cafe)
    db.commit()


@use_database
def delete(db, cafe_id):
    cafe = select_one(cafe_id)

    db.delete(cafe)
    db.commit()
