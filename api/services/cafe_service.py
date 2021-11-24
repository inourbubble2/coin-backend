import requests

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

        header = {'Authorization': 'KakaoAK e739d059fb281ac73a2ca928910f688d'}
        query = data['address'] + ' ' + data['name']
        url = f'https://dapi.kakao.com/v2/local/search/keyword.json?sort=accuracy&query={query}&category_group_code=CE7&size=1'
        response = requests.get(url, headers=header).json()

        data['name'] = response['documents'][0]['place_name']
        data['longitude'] = response['documents'][0]['x']
        data['latitude'] = response['documents'][0]['y']
        data['address'] = response['documents'][0]['road_address_name']
        data['kakao_id'] = response['documents'][0]['id']

        super().create(data)

    def find_with_pagination_and_arguments(self, page, per_page, name, location):
        cafes = self.repository.find_with_pagination_and_arguments(page, per_page, name, location)
        return cafes

