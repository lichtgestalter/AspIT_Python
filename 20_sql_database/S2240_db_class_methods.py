"""
Sometimes we don't want to read all records from a table.
Instead we just want a single record with a certain id.
For this, we add a function get_record.

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
        return self.id, self.name, self.age

    def valid(self):  # is this object a valid record of a person?
        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Person
        person = Person(id=tuple_[0], name=tuple_[1], age=tuple_[2])
        return person


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

# print(select_all(Person))
# print(Person.convert_from_tuple((12, "test", 17)))
print(get_record(Person, 1))

