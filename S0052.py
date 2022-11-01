# Encapsulation:

# sometimes we want to keep properties or methods private to a class
# this means these properties or methods can only be used by the class that owns them
# in python a private property or method is marked by a leading single underscore (_)
# in python it's technically possible to use private methods outside their class, but it's considered very unwise

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

# read more about object oriented programming here:
# https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/