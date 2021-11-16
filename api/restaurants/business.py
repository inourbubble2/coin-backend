from database import use_database
from database.models import Restaurant


@use_database
def create_restaurant(db, data):
    name = data.get('name')
    kakaomap_id = data.get('kakaomap_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    restaurant = Restaurant(
        name=name,
        kakaomap_id=kakaomap_id,
        latitude=latitude,
        longitude=longitude
    )

    db.add(restaurant)
    db.commit()


@use_database
def read_restaurant(db, restaurant_id):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).one()
    return restaurant


@use_database
def read_restaurants(db, data, page, per_page):
    query = db.query(Restaurant)

    if 'name' in data:
        query = query.filter(Restaurant.name.like(data.get('name')))

    restaurants = query.offset((page - 1) * per_page).limit(per_page).all()

    return restaurants


@use_database
def update_restaurant(db, restaurant_id, data):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).one()

    if 'kakaomap_id' in data:
        restaurant.kakaomap_id = data.get('kakaomap_id')
    if 'name' in data:
        restaurant.name = data.get('name')
    if 'latitude' in data:
        restaurant.latitude = data.get('latitude')
    if 'longitude' in data:
        restaurant.longitude = data.get('longitude')

    db.add(restaurant)
    db.commit()


@use_database
def delete_restaurant(db, restaurant_id):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).one()
    db.delete(restaurant)
    db.commit()
