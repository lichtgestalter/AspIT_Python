from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox


Base = declarative_base()

class Container(Base):
    __tablename__ = 'container'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    destination = Column(String)

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

class Aircraft(Base):
    __tablename__ = 'aircraft'
    id = Column(Integer, primary_key=True)
    max_cargo_weight = Column(Integer)
    registration = Column(String)

    def __repr__(self):
        return f"Container({self.id=:4}    {self.max_cargo_weight=:5}    {self.registration=})"

    def convert_to_tuple(self):
        return self.id, self.max_cargo_weight, self.registration

    def valid(self):
        try:
            value = int(self.max_cargo_weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        container = Aircraft(id=tuple_[0], max_cargo_weight=tuple_[1], registration=tuple_[2])
        return container

class Transport(Base):
    __tablename__ = 'transport'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    container_id = Column(Integer, ForeignKey('container.id'), nullable=False)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'), nullable=False)

    def __repr__(self):
        return f"Container({self.id=:4}    {self.date=:5}    {self.container_id=}   {self.aircraft_id=})"

    def convert_to_tuple(self):
        return self.id, self.date, self.container_id, self.aircraft_id

    def valid(self):
        return True
    @staticmethod
    def convert_from_tuple(tuple_):
        try:
            if tuple_[0] != '':  # unnecessary precaution?
                id_ = int(tuple_[0])
            else:
                id_ = 0
            date = parser.parse(tuple_[1])
            container_id = int(tuple_[2])
            aircraft_id = int(tuple_[3])
            # transport = Transport(id=tuple_[0], date=date, container_id=tuple_[2], aircraft_id=tuple_[3])  # unnecessary precaution?
            transport = Transport(id=id_, date=date, container_id=container_id, aircraft_id=aircraft_id)
            return transport
        except:
            messagebox.showwarning("", "Entries could not be converted to transport!")