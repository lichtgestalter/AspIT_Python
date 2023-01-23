from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import danskcargo_data as dcd
import danskcargo_sql as dcsql

# One could argue that function1 and function2 should be in the SQL layer,
# because they interact with the database. But since they are specifically written for
# function3 and function4 respectively, and are not called by other functions,
# it is also a good choice to keep them in the function layer.

def booked_cargo(aircraft, date_):
    # returns the already booked cargo on an aircraft at a certain date
    with Session(dcsql.engine) as session:
        records = session.scalars(select(dcd.Transport).where(dcd.Transport.aircraft_id == aircraft.id).where(extract('day', dcd.Transport.date) == date_.day).where(extract('month', dcd.Transport.date) == date_.month).where(extract('year', dcd.Transport.date) == date_.year))
        weight = 0
        for record in records:
            weight += dcsql.get_record(dcd.Container, record.container_id).weight
    return weight


def capacity_available(aircraft, date_, new_container):
    # do the already booked cargo plus the new container weigh less than the aircraft's maximum cargo weight?
    booked = booked_cargo(aircraft, date_)
    # print(f'{aircraft.max_cargo_weight=} {booked=} {new_container.weight=}')
    return aircraft.max_cargo_weight >= booked + new_container.weight


def find_destination(aircraft, date_):
    # return an aircraft's destination at a certain date in the transport table
    with Session(dcsql.engine) as session:
        records = session.scalars(select(dcd.Transport).where(dcd.Transport.aircraft_id == aircraft.id).where(extract('day', dcd.Transport.date) == date_.day).where(extract('month', dcd.Transport.date) == date_.month).where(extract('year', dcd.Transport.date) == date_.year))
        for record in records:
            return dcsql.get_record(dcd.Container, record.container_id).destination
        return None


def max_one_destination(aircraft, date_, new_container):
    # is the aircraft's destination at a certain date identical to the new container's destination?
    destination = find_destination(aircraft, date_)
    return destination is None or destination == new_container.destination  # returns also True if aircraft had no destination yet
