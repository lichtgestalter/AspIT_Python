from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

from danskcargo_data import Container, Base

Database = 'sqlite:///danskcargo.db'  # first part: database type, second part: file path


def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Container(weight=1200, destination="Oslo"))
        new_items.append(Container(weight=700, destination="Helsinki"))
        new_items.append(Container(weight=1800, destination="Helsinki"))
        new_items.append(Container(weight=1000, destination="Helsinki"))
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


if __name__ == "__main__":  # Executed when invoked directly
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
    # create_test_data()
    print(select_all(Container))
    print(get_record(Container, 2))
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
