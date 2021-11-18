from database import Database
from database.cafe import Cafe
from api.repositories.pagination_repository import pagination
from api.repositories.repository import Repository


class CafeRepository(Repository):
    def __init__(self):
        self.obj = Cafe
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)

    def find_with_pagination_and_arguments(self, page, per_page, name, location):
        query = self.db.query(Cafe)

        if name:
            query = query.filter(Cafe.name.like(f'%{name}%'))
        if location:
            query = query.filter(Cafe.location == location)

        cafes = pagination(query, page, per_page)

        return cafes
