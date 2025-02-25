from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from danskcargo_data import Container, Aircraft, Transport, Base

from sqlalchemy.engine import Engine
from sqlalchemy import event
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

Database = 'sqlite:///danskcargo.db'

def create_test_data():
    with Session(engine) as session:
        new_items = []
        #new_items.append(Container(weight=1200, destination="Oslo"))
        #new_items.append(Container(weight=700, destination="Helsinki"))
        #new_items.append(Container(weight=1800, destination="Helsinki"))
        #new_items.append(Container(weight=1000, destination="Helsinki"))
        new_items.append(Aircraft(max_cargo_weight=2000, registration="OY-CBS"))
        new_items.append(Aircraft(max_cargo_weight=3000, registration="OY-THR"))
        a_date = date(day=10, month=12, year=2022)
        new_items.append(Transport(date=a_date, container_id=2, aircraft_id=1))
        session.add_all(new_items)
        session.commit()

def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result

def get_record(classparam, record_id):
    with Session(engine) as session:
        records = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return records


def create_record(record):
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()


# region container
def update_container(container):
    with Session(engine) as session:
        session.execute(update(Container).where(Container.id == container.id).values(weight=container.weight, destination=container.destination))
        session.commit()

def delete_hard_container(container):
    with Session(engine) as session:
        session.execute(delete(Container).where(Container.id == container.id))
        session.commit()

def delete_soft_container(container):
    with Session(engine) as session:
        session.execute(update(Container).where(Container.id == container.id).values(weight=-1, destination=container.destination))
        session.commit()

# endregion container

# region aircraft
def update_aircraft(aircraft):
    with Session(engine) as session:
        session.execute(update(Aircraft).where(Aircraft.id == aircraft.id).values(max_cargo_weight=aircraft.max_cargo_weight, registration=aircraft.registration))
        session.commit()

def delete_hard_aircraft(aircraft):
    with Session(engine) as session:
        session.execute(delete(Aircraft).where(Aircraft.id == aircraft.id))
        session.commit()

def delete_soft_aircraft(aircraft):
    with Session(engine) as session:
        session.execute(update(Aircraft).where(Aircraft.id == aircraft.id).values(max_cargo_weight=-1, registration=aircraft.registration))
        session.commit()

# endregion aircraft

# region transport
def update_transport(transport):
    with Session(engine) as session:
        session.execute(update(Transport).where(Transport.id == transport.id).values(date=transport.date, container_id=transport.container_id, aircraft_id=transport.aircraft_id))
        session.commit()

def delete_hard_transport(transport):
    with Session(engine) as session:
        session.execute(delete(Transport).where(Transport.id == transport.id))
        session.commit()

def delete_soft_Transport(transport):
    with Session(engine) as session:
        session.execute(update(Transport).where(Transport.id == transport.id).values(date=-1, container_id=transport.container_id, aircraft_id=transport.aircraft_id))
        session.commit()

# endregion transport



if __name__ == '__main__':
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    #create_test_data()
    print(select_all(Container))
    print(get_record(Container, 2))
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
