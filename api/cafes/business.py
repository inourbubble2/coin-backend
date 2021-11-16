from database import use_database
from database.models import Cafe


@use_database
def create_cafe(db, data):
    cafe = Cafe(
        name=data.get('name'),
        description=data.get('description'),
        address=data.get('address'),
        open_hour=data.get('open_hour'),
        contact=data.get('contact'),
        link=data.get('link'),
        location=data.get('location'),
        star=data.get('star'),
        kakao_id=data.get('kakao_id'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude')
    )
    db.add(cafe)
    db.commit()


@use_database
def read_cafe(db, cafe_id):
    cafe = db.query(Cafe)\
        .filter(Cafe.id == cafe_id)\
        .one()

    return cafe


@use_database
def read_cafes(db, data, page, per_page):
    query = db.query(Cafe)

    if 'name' in data:
        query = query.filter(Cafe.name.like(data.get('name')))
    if 'location' in data:
        query = query.filter(Cafe.location.is_(data.get('location')))

    cafes = query.offset((page - 1) * per_page)\
        .limit(per_page)\
        .all()

    return cafes


@use_database
def update_cafe(db, cafe_id, data):
    pass


@use_database
def delete_cafe(db, cafe_id):
    cafe = db.query(Cafe)\
        .filter(Cafe.id == cafe_id)\
        .one()

    db.delete(cafe)
    db.commit()
