"""
__repr__ and f-strings:

Every class in python has a function __repr__ that defines the output of printing an object of this class.
Every class in python has automatically some useful functions, which begin and end with to underscores.
We can override these functions.
They are called magic functions or dunder functions.
In this example we are using so called f-strings. They are very handy.
Read more about f-strings here: https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python

Inspect the following code in detail. Find out what every row of code does.
For example by changing the code a bit and then running/debugging the program.

Thereafter go on with the next file.
"""


class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an instance/object of a class
        self.wheels = wheels  # wheels is called an attribute. A attribute is a variable that belongs to an object of a class.
        self.max_speed = max_speed  # Another attribute.

    def __repr__(self):
        return f"Vehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)  # car1 is now defined as an instance/object of type Vehicle. Also its attributes are already defined.
car2 = Vehicle(8, 100)

print(car1)
print(car2)
car1.drive()  # the method drive of the class Vehicle is called on the object car1
