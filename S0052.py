# Læs https://www.freecodecamp.org/news/the-python-handbook/#classesinpython

class Vehicle:  #

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an object of a class
        self.wheels = wheels  # wheels is called a property. A property is a variable that belongs to a class.
        self.max_speed = max_speed  # another property

    def __repr__(self):
        return f"{self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):
        print("WROOOOOOOOM!")


class ElectricVehicle(Vehicle):  # class ElectricVehicle inherits from class Vehicle

    def __init__(self, wheels, max_speed, battery_capacity):
        super().__init__(wheels, max_speed)
        self.battery_capacity = battery_capacity

    def __repr__(self):
        return f"{self.wheels} wheels, {self.max_speed} km/h maximum speed, {self.battery_capacity} kW capacity"

    def drive(self):
        print("ssssssssss")


car1 = Vehicle(4, 160)
print(car1)
bigcar2 = ElectricVehicle(8, 100, 90)
print(bigcar2)
print(car1.wheels)
car1.drive()
bigcar2.drive()
