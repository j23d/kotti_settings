from sqlalchemy import Column
from sqlalchemy import Integer

from kotti import Base
from kotti.sqla import JsonType

from kotti_settings.sqla import MutableDict


class Settings(Base):
    __tablename__ = 'settings'

    id = Column('id', Integer, primary_key=True)
    data = Column(MutableDict.as_mutable(JsonType))

    def __init__(self, data):
        self.data = data
