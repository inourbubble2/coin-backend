import functools
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/coin-database', connect_args={'connect_timeout': 10},
    pool_size=2, max_overflow=50,
    json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False)
)


Session = sessionmaker(bind=engine)


class Database:
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()


def use_database(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        with Database() as db:
            return f(db, *args, **kwargs)
    return deco