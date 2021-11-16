import api.repositories.cafe_repository as cafe_repository


class Cafe:
    def create(self, data):
        cafe_repository.create(data)

    def find_one(self, cafe_id):
        cafe = cafe_repository.find_one(cafe_id)
        return cafe

    def find(self, page, per_page, name, location):
        cafes = cafe_repository.find(page, per_page, name, location)
        return cafes

    def update(self, cafe_id, data):
        cafe_repository.update(cafe_id, data)

    def remove(self, cafe_id):
        cafe_repository.remove(cafe_id)
