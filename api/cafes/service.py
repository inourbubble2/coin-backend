import api.cafes.repository as cafe_repository


def create(data):
    cafe_repository.create(data)


def find_one(cafe_id):
    cafe = cafe_repository.select_one(cafe_id)
    return cafe


def find_all(page, per_page, name, location):
    cafes = cafe_repository.select_all(page, per_page, name, location)
    return cafes


def update(cafe_id, data):
    cafe_repository.update(cafe_id, data)


def delete(cafe_id):
    cafe_repository.delete(cafe_id)
