"""
Encapsulation:

Sometimes we want to keep attributes or methods private to a class.
This means these attributes or methods can only be used by the class that owns them.
In python a private attribute or method is marked by a leading single underscore (_).
In python it's technically possible to call private methods from outside their class, but it's considered unwise.
Private members are also called protected members.

Inspect the following code in detail. Find out what every row of code does.
For example by changing the code a bit and then running/debugging the program.

Read more about object oriented programming here:
https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

Then send this Teams message to your teacher: <filename> done

Thereafter go on with the next file.
"""


class Vehicle:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed

    def __repr__(self):
        return f"Vehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):
        print("WROOOOOOOOM!")
        self._top_secret()  # this is ok

    def _top_secret(self):
        print("Don't call this method from outside this class!")


car1 = Vehicle(4, 160)
car1.drive()
car1._top_secret()  # this is NOT ok!

