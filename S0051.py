# Læs https://www.freecodecamp.org/news/the-python-handbook/#classesinpython

class Vehicle:

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an object of a class
        self.wheels = wheels  # wheels is called a property. A property is a variable that belongs to a class.
        self.max_speed = max_speed  # another property

    def drive(self):
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)
print(car1)
print(car1.wheels)
car1.drive()
