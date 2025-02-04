from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer

Base = declarative_base()

class Container(Base):
    __tablename__ = 'container'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    destination = Column(Integer)

    def __repr__(self):
        return f"Container({self.id=:4}    {self.weight=:5}    {self.destination=})"

    def convert_to_tuple(self):
        return self.id, self.weight, self.destination

    def valid(self):
        try:
            value = int(self.weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        container = Container(id=tuple_[0], weight=tuple_[1], destination=tuple_[2])
        return container

