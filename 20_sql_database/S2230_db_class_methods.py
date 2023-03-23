"""
We add a few more methods to our class, which will be useful later on.

Run the program.
Read all the comments.
Understand the program code.
"""

from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select

Database = 'sqlite:///../data/my_first_sql_database.db'
Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Person({self.id=}    {self.name=}    {self.age=})"

    def convert_to_tuple(self):  # Convert Person to tuple
        # Soon we want to show the contents of our database in our gui in a treeview widget.
        # Each line that is fed into a treeview must be a tuple.
        # This function converts an object of type Person into a tuple.
        return self.id, self.name, self.age

    def valid(self):  # is this object a valid record of a person?
        # Check if the record contains data and is not considered "soft deleted" (negative age).
        # We explain "soft deleted" later.

        # If an error occurs while executing the code in a try block, instead of
        # the program ending with an error message, the except block gets executed.
        # Find more details on https://pythonbasics.org/try-except/.
        try:
            value = int(self.age)  # trying to convert self.age into an integer
        except ValueError:
            return False  # do this if the conversion produced an error
        return value >= 0  # only non-negative values are considered valid

    @staticmethod  # this is called a decorator
    def convert_from_tuple(tuple_):  # Convert tuple to Person
        # when reading data from our gui widgets, we typically get the data as a tuple
        # This function converts a tuple into an object of type Person.
        # the decorator declares the method to be static
        # a static method operates on the class, not on an object of the class
        # see https://www.geeksforgeeks.org/python-staticmethod/
        person = Person(id=tuple_[0], name=tuple_[1], age=tuple_[2])
        return person


def select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # in the background this creates the sql query "select * from persons" when called with classparam=Person
        result = []
        for record in records:  # convert the query result into a list of records
            result.append(record)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

# print(select_all(Person))
print(Person.convert_from_tuple((12, "test", 17)))
