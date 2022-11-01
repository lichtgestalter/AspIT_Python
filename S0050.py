# every class in python has a function __repr__ that defines the output when you print an object of this class

class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an object of a class
        self.wheels = wheels  # wheels is called a property. A property is a variable that belongs to a class.
        self.max_speed = max_speed  # another property

    def __repr__(self):
        return f"{self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)  # car1 is now defined as an object of type Vehicle. Also its properties are already defined.
car1.drive()  # the method drive of the class Vehicle is called on the object car1

print(1, type(car1))
print(2, car1)
