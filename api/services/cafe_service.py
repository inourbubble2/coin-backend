import requests

from werkzeug.exceptions import BadRequest, NotFound, Conflict

from api.services.service import Service
from api.repositories.cafe_repository import CafeRepository


class CafeService(Service):
    def __init__(self):
        self.repository = CafeRepository()
        super().__init__(self.repository)

    def find_by_kakao_id(self, kakao_id):
        return self.repository.find_by_kakao_id(kakao_id)

    def create(self, data):
        for key, value in data.items():
            if key == 'star' and not (1 <= value <= 5):
                raise BadRequest('star is not valid range.')
            elif key == 'location' and not value in {'hoegi', 'front', 'side', 'back'}:
                raise BadRequest('location is not valid.')

        documents = self.find_cafe_from_kakao(data['name'], data['address'])

        data['address'] = documents[0]['road_address_name']
        data['name'] = documents[0]['place_name']
        data['latitude'] = documents[0]['x']
        data['longitude'] = documents[0]['y']
        data['link'] = documents[0]['place_url']
        data['kakao_id'] = documents[0]['id']

        super().create(data)

    def find_cafe_from_kakao(self, name, address):
        header = {'Authorization': 'KakaoAK e739d059fb281ac73a2ca928910f688d'}
        query = f'{address} {name}'
        url = f'https://dapi.kakao.com/v2/local/search/keyword.json?sort=accuracy&query={query}&category_group_code=CE7&size=1'
        response = requests.get(url, headers=header).json()

        if len(response['documents']) == 0:
            raise NotFound

        return response['documents']

    def find_with_pagination_and_arguments(self, page, per_page, name, location):
        cafes = self.repository.find_with_pagination_and_arguments(page, per_page, name, location)
        return cafes

