"""
Input:
Write a python program that uses sqlalchemy to create a sqlite database with a table named
customers containig the columns id (primary key), name and age. The program creates 4 test
datasets for this table, writes them into the database and uses tkinter in order to display
the table's content.

Output:
Sure, here's a python program that creates a SQLite database using SQLAlchemy and then creates
a table called "customers" with columns "id" (primary key), "name", and "age". It then inserts
four test datasets into the table and uses Tkinter to display the table's content.

When you run this program, it should create a SQLite database called "customers.db" in your
current working directory, create a table called "customers" with the specified columns, insert
four test datasets into the table, and display the table's content using Tkinter.
"""

from tkinter import *
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create database
engine = create_engine('sqlite:///customers.db', echo=True)

# Create table
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

# Insert test datasets
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Customer(name='Alice', age=25),
    Customer(name='Bob', age=30),
    Customer(name='Charlie', age=35),
    Customer(name='Dave', age=40)
])

session.commit()

# Display table content using Tkinter
root = Tk()
root.title("Customers Table")

# Create scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create table
table = Listbox(root, yscrollcommand=scrollbar.set)
table.pack(side=LEFT, fill=BOTH, expand=1)

# Add table headers
table.insert(END, "ID\tName\tAge")

# Query and add rows to table
for customer in session.query(Customer):
    table.insert(END, f"{customer.id}\t{customer.name}\t{customer.age}")

# Set scrollbar to table
scrollbar.config(command=table.yview)

root.mainloop()
