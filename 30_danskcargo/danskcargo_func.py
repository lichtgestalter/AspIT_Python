from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract
import danskcargo_data as dcd
import danskcargo_sql as dcsql

def booked_cargo(aircraft, date_):
    with Session() as session:
        records = session.scalars(select(dcd.Transport)
                                  .where(dcd.Transport.aircraft_id == aircraft.id)
                                  .where(extract('day', dcd.Transport.date) == date_.day)
                                  .where(extract('month', dcd.Transport.date) == date_.month)
                                  .where(extract('year', dcd.Transport.date) == date_.year))
        weight = 0
        for record in records:
            weight += dcsql.get_weight(dcd.Container, record.container).weight
        return weight

def capacity_available(aircraft, date_, new_container):
    booked = booked_cargo(aircraft, date_)
    return aircraft.max_cargo_weight >= booked + new_container.weight

def find_destination(aircraft, date_):
    with Session() as session:
        records = session.scalars(select(dcd.Transport)
                                  .where(dcd.Transport.aircraft_id == aircraft.id)
                                  .where(extract('day', dcd.Transport.date) == date_.day)
                                  .where(extract('month', dcd.Transport.date) == date_.month)
                                  .where(extract('year', dcd.Transport.date) == date_.year))
        for record in records:
            return dcsql.get_record(dcd.Container, record.container_id).destination
        return None

def max_one_destination(aircraft, date_, new_container):
    destination = find_destination(aircraft, date_)
    return destination is None or destination == new_container.destination
