"""
First read /misc/SQL.docx and do what it says.

Just to get us going we create some test data. We need to do this only once.
"""

from sqlalchemy.orm import declarative_base  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

Database = 'sqlite:///data/my_first_sql_database.db'  # first part: database type, second part: file path
Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.


class Person(Base):
    # this class declaration does 2 important things at once:
    # 1. as usual, it declares a class we can store data in, inside our python program.
    # 2. it creates a table in a sql database with the specified columns
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Persons({self.id=:4}    {self.name=:16}    {self.age=})"


def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Person(name="peter", age=18))
        new_items.append(Person(name="susan", age=19))
        new_items.append(Person(name="jane", age=21))
        new_items.append(Person(name="harry", age=20))
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


engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
Base.metadata.create_all(engine)
# create_test_data()
answer = select_all(Person)
print(answer)
# print(get_record(Container, 2))
# print(get_record(Aircraft, 3))
# update_example(engine)
# delete_example(engine)
# insert_example(engine)
# select_text(engine)
