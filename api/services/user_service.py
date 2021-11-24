import requests

from werkzeug.exceptions import BadRequest, NotFound, Conflict

from api.services.service import Service
from api.repositories.user_repository import UserRepository


class UserService(Service):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__(self.repository)

    def create(self, data):
        if self.repository.find_by_kakao_id(data['kakao_id']):
            raise Conflict

        return super().create(data)