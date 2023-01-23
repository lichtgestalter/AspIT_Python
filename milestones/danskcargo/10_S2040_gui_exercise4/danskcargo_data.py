from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer

Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.


class Container(Base):
    __tablename__ = "container"
    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    destination = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Container({self.id=:4}    {self.weight=:5}    {self.destination=})"

    def convert_to_tuple(self):  # Convert Container to tuple
        return self.id, self.weight, self.destination

    def valid(self):
        try:  # https://www.w3schools.com/python/python_try_except.asp
            value = int(self.weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Container
        container = Container(id=tuple_[0], weight=tuple_[1], destination=tuple_[2])
        return container
