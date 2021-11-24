from database import Database
from database.user import User
from api.repositories.repository import Repository


class UserRepository(Repository):
    def __init__(self):
        self.obj = User
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)

    def find_by_kakao_id(self, kakao_id):
        user = self.db.query(User) \
            .filter(User.kakao_id == kakao_id) \
            .first()
        if user:
            return user
        else:
            return None
