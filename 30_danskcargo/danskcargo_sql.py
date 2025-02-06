from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from danskcargo_data import Container, Base

from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy import create_engine, select, update, delete

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

Database = 'sqlite:///danskcargo.db'

def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Container(weight=1200, destination="Oslo"))
        new_items.append(Container(weight=700, destination="Helsinki"))
        new_items.append(Container(weight=1800, destination="Helsinki"))
        new_items.append(Container(weight=1000, destination="Helsinki"))
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



if __name__ == '__main__':
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    print(select_all(Container))
    print(get_record(Container, 2))
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
