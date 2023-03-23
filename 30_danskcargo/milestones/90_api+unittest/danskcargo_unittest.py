import unittest
from datetime import date
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine
import danskcargo_gui as dcg
import danskcargo_data as dcd
import danskcargo_sql as dcsql

class TestStringMethods(unittest.TestCase):  # basic example from https://docs.python.org/3/library/unittest.html

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestEmptyEntries(unittest.TestCase):

    def test_empty_container_entries(self):
        # arrange
        Database = 'sqlite:///danskcargo.db'  # first part: database type, second part: file path
        Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.
        engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            new_items = []
            new_items.append(dcd.Container(weight=1234, destination="Oslo"))  # add new container to database
            new_items.append(dcd.Aircraft(max_cargo_weight=1000, registration="OY-THR"))  # add new aircraft to database
            session.add_all(new_items)
            session.commit()
        a_date = "8888-11-22"
        record = ("", a_date, dcsql.max_id(dcd.Container), dcsql.max_id(dcd.Aircraft))  # create a tuple using the newly added container and aircraft (because they have been newly added, they each have the highest id in their table)
        # act
        dcg.create_transport(dcg.tree_transport, record)
        # assert
        self.assertEqual(dcg.INTERNAL_ERROR_CODE, 1)  # container weighs more than the aircraft's


if __name__ == '__main__':
    unittest.main()
