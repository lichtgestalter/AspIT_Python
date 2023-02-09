from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox

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
        try:
            value = int(self.weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Container
        container = Container(id=tuple_[0], weight=tuple_[1], destination=tuple_[2])
        return container


class Aircraft(Base):
    __tablename__ = "aircraft"
    id = Column(Integer, primary_key=True)
    max_cargo_weight = Column(Integer)
    registration = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Aircraft ({self.id=:4},   {self.max_cargo_weight=:6},  {self.registration=})"

    def convert_to_tuple(self):  # Convert aircraft to tuple
        return self.id, self.max_cargo_weight, self.registration

    def valid(self):
        try:
            value = int(self.max_cargo_weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to aircraft
        try:
            # if tuple_[0] != '':  # unnecessary precaution
            #     id_ = int(tuple_[0])
            # else:
            #     id_ = 0
            max_cargo_weight = int(tuple_[1])
            if max_cargo_weight < 0:
                messagebox.showwarning("", "Max. Cargo Weight must not be negative!")
            else:
                aircraft = Aircraft(id=tuple_[0], max_cargo_weight=max_cargo_weight, registration=tuple_[2])
                # aircraft = Aircraft(id=id_, max_cargo_weight=max_cargo_weight, registration=tuple_[2])
                return aircraft
        except:
            messagebox.showwarning("", "Entries could not be converted to aircraft!")


class Transport(Base):
    __tablename__ = "transport"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    container_id = Column(Integer, ForeignKey("container.id"), nullable=False)
    aircraft_id = Column(Integer, ForeignKey("aircraft.id"), nullable=False)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Transporter({self.id=}, {self.date=}, {self.container_id=}, {self.aircraft_id=})"

    def convert_to_tuple(self):  # Convert transport to tuple
        return self.id, self.date, self.container_id, self.aircraft_id

    def valid(self):
        try:
            value = int(self.container_id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to transport
        try:
            if tuple_[0] != '':
                id_ = int(tuple_[0])
            else:
                id_ = 0
            date = parser.parse(tuple_[1])
            container_id = int(tuple_[2])
            aircraft_id = int(tuple_[3])
            transport = Transport(id=id_, date=date, container_id=container_id, aircraft_id=aircraft_id)
            return transport
        except:
            messagebox.showwarning("", "Entries could not be converted to transport!")
