class Service:
    def __init__(self, repository):
        self.repository = repository

    def create(self, data):
        return self.repository.create(data)

    def find(self):
        return self.repository.find()

    def find_one(self, id):
        return self.repository.find_one(id)

    def find_with_pagination(self, page, limit):
        return self.repository.find_with_pagination(page, limit)

    def update(self, id, data):
        self.repository.update(id, data)

    def remove(self, id):
        self.repository.remove(id)

