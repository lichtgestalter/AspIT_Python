from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from danskcargo_data import Container, Base

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






if __name__ == '__main__':
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    print(select_all(Container))
    print(get_record(Container, 2))
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
