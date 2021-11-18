from werkzeug.exceptions import BadRequest

from api.services.service import Service
from api.repositories.cafe_repository import CafeRepository


class CafeService(Service):
    def __init__(self):
        self.repository = CafeRepository()
        super().__init__(self.repository)

    def create(self, data):
        for key, value in data.items():
            if key == 'star' and not (1 <= value <= 5):
                raise BadRequest('star is not valid range.')
            elif key == 'location' and not value in {'hoegi', 'front', 'side', 'back'}:
                raise BadRequest('location is not valid.')
        super().create(data)

    def find_with_pagination_and_arguments(self, page, per_page, name, location):
        cafes = self.repository.find_with_pagination_and_arguments(page, per_page, name, location)
        return cafes

