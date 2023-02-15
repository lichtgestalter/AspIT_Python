from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from danskcargo_data import Container, Aircraft, Transport, Base

# add the following 7 lines to make foreign key constraints work  https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#sqlite-foreign-keys
from sqlalchemy.engine import Engine
from sqlalchemy import event
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///danskcargo.db'  # first part: database type, second part: file path


def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        # new_items.append(Container(weight=1200, destination="Oslo"))
        # new_items.append(Container(weight=700, destination="Helsinki"))
        # new_items.append(Container(weight=1800, destination="Helsinki"))
        # new_items.append(Container(weight=1000, destination="Helsinki"))
        new_items.append(Aircraft(max_cargo_weight=2000, registration="OY-CBS"))
        new_items.append(Aircraft(max_cargo_weight=3000, registration="OY-THR"))
        a_date = date(day=10, month=12, year=2022)
        new_items.append(Transport(date=a_date, container_id=2, aircraft_id=1))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # very useful for converting into our data class
        result = []
        for record in records:
            # print(record)
            result.append(record)
    return result


def get_record(classparam, record_id):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return the record in classparams table with a certain id
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()  # very useful for converting into our data class
    return record


def create_record(record):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # create a record in the database
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()  # makes changes permanent in database


# region container
def update_container(container):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the container table
    with Session(engine) as session:
        session.execute(update(Container).where(Container.id == container.id).values(weight=container.weight, destination=container.destination))
        session.commit()  # makes changes permanent in database


def delete_hard_container(container):
    # delete a record in the container table
    with Session(engine) as session:
        session.execute(delete(Container).where(Container.id == container.id))
        session.commit()  # makes changes permanent in database


def delete_soft_container(container):
    # soft delete a record in the container table by setting its weight to -1 (see also method "valid" in the container class)
    with Session(engine) as session:
        session.execute(update(Container).where(Container.id == container.id).values(weight=-1, destination=container.destination))
        session.commit()  # makes changes permanent in database
# endregion container


# region aircraft
def update_aircraft(aircraft):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the aircraft table
    with Session(engine) as session:
        session.execute(update(Aircraft).where(Aircraft.id == aircraft.id).values(max_cargo_weight=aircraft.max_cargo_weight, registration=aircraft.registration))
        session.commit()  # makes changes permanent in database


def delete_hard_aircraft(aircraft):
    # delete a record in the aircraft table
    with Session(engine) as session:
        session.execute(delete(Aircraft).where(Aircraft.id == aircraft.id))
        session.commit()  # makes changes permanent in database


def delete_soft_aircraft(aircraft):
    # soft delete a record in the aircraft table by setting its max_cargo_weight to -1 (see also method "valid" in the aircraft class)
    with Session(engine) as session:
        session.execute(update(Aircraft).where(Aircraft.id == aircraft.id).values(max_cargo_weight=-1, registration=aircraft.registration))
        session.commit()  # makes changes permanent in database
# endregion aircraft


# region transport
def update_transport(transport):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the transport table
    with Session(engine) as session:
        session.execute(update(Transport).where(Transport.id == transport.id).values(date=transport.date, container_id=transport.container_id, aircraft_id=transport.aircraft_id))
        session.commit()  # makes changes permanent in database


def delete_hard_transport(transport):
    # delete a record in the transport table
    with Session(engine) as session:
        session.execute(delete(Transport).where(Transport.id == transport.id))
        session.commit()  # makes changes permanent in database
# endregion transport


# region examples
# def select_container():  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
#     with Session(engine) as session:
#         print("\nsession.scalars(select(Container).where(Container.id >= '4'))")
#         containers = session.scalars(select(Container))  # very useful for converting into our data class
#         result = []
#         for container in containers:
#             print(container)
#             result.append(container)
#     return result


# def update_example():  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
#     with Session(engine) as session:
#         print("\nsession.execute(update(Container).where(Container.id == 5).values(name='new name'))")
#         session.execute(update(Container).where(Container.id == 5).values(name="new name"))
#         # session.execute(update(Container).where(Container.id == 5).values(name="sandy"))
#         print("\nsession.scalars(select(Container).where(Container.id >= '0'))")
#         containers = session.scalars(select(Container).where(Container.id >= "0"))  # very useful for converting into our data class
#         for container in containers:
#             print(container, type(container))
#         # session.commit()  # makes changes permanent in database


# def delete_example():  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-delete-statements
#     with Session(engine) as session:
#         print("\nsession.execute(delete(Container).where(Container.id == 5))")
#         session.execute(delete(Container).where(Container.id == 5))
#         print("\nsession.scalars(select(Container).where(Container.id >= '0'))")
#         print("\nsession.scalars(select(Container).where(Container.id >= '0'))")
#         containers = session.scalars(select(Container).where(Container.id >= "0"))  # very useful for converting into our data class
#         for container in containers:
#             print(container, type(container))
#         # session.commit()  # makes changes permanent in database


# def insert_example():  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-delete-statements
#     with Session(engine) as session:
#         krabs = Container(name="ehkrabs", fullname="Eugene H. Krabs")
#         squidward = Container(name="squidward", fullname="Squidward Tentacles")
#         session.add(squidward)
#         session.add(krabs)
#         # session.flush()
#         session.commit()  # makes changes permanent in database
#         containers = session.scalars(select(Container).where(Container.id >= "0"))  # very useful for converting into our data class
#         for container in containers:
#             print(container, type(container), type(containers))
# endregion examples

if __name__ == "__main__":  # Executed when invoked directly
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
    # create_test_data()
    # select_all(Container)
    # select_all(Aircraft)
    select_all(Transport)
    print(get_record(Container, 2))
    print(get_record(Aircraft, 3))
    # update_example(engine)
    # delete_example(engine)
    # insert_example(engine)
    # select_text(engine)
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
