from werkzeug.exceptions import BadRequest
from database.cafe import LocationEnum
import api.repositories.cafe_repository as cafe_repository


class Cafe:
    def create(self, data):
        for key, value in data.items():
            if key == 'star' and not (1 <= value <= 5):
                raise BadRequest('star is not valid range.')
            elif key == 'location' and not value in {'hoegi', 'front', 'side', 'back'}:
                raise BadRequest('location is not valid.')
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
